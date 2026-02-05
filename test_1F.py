from floodsystem.station import inconsistent_typical_range_stations

class MockStation:
    """minimal mock MonitoringStation object for unit testin"""

    def __init__(self, name, typical_range):
        self.name = name
        self.typical_range = typical_range

    def typical_range_consistent(self):
        """mock consistency check matching the real method behaviour"""
        if self.typical_range is None:
            return False
        low, high = self.typical_range
        return low <= high


def test_none_typical_range_is_inconsistent():
    """test that a station with no typical range data
    is classified as inconsistent"""
    stations = [MockStation("Station A", None),MockStation("Station B", (0.1, 1.0)),]

    result = inconsistent_typical_range_stations(stations)

    assert result == ["Station A"]


def test_low_greater_than_high_is_inconsistent():
    """est that a station where the typical low range
    is greater than the typical high range is inconsistent."""
    stations = [MockStation("Station A", (1.2, 0.4)),MockStation("Station B", (0.0, 2.0)),]

    result = inconsistent_typical_range_stations(stations)

    assert result == ["Station A"]


def test_consistent_stations_excluded():
    """test that stations with consistent typical range dataare not included in the result"""
    stations = [MockStation("Station A", (0.0, 1.0)),MockStation("Station B", (0.5, 2.5)),]

    result = inconsistent_typical_range_stations(stations)

    assert result == []


def test_multiple_inconsistent_stations_sorted():
    """test that multiple inconsistent stations are returned in alphabetical order"""
    stations = [MockStation("Zeta", None),MockStation("Alpha", (2.0, 1.0)),MockStation("Beta", (0.0, 1.0)),]

    result = inconsistent_typical_range_stations(stations)

    assert result == ["Alpha", "Zeta"]


def test_empty_station_list():
    """test that an empty list of stations returns an empty list"""
    stations = []

    result = inconsistent_typical_range_stations(stations)

    assert result == []

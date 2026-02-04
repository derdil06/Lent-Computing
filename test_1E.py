from Task1E import rivers_by_station_number
from floodsystem.stationdata import build_station_list

class MockStation:
    """minimal mock MonitoringStation object for unit testing"""
    def __init__(self, river):
        self.river = river


def test_typical_case():
    """test that the function correctly identifies the rivers with thegreatest number of stations in a typical, mixed case"""
    stations = [MockStation("River Cam"),MockStation("River Cam"),MockStation("River Thames"),MockStation("River Thames"),MockStation("River Thames"),MockStation("River Ouse"),]

    result = rivers_by_station_number(stations, 2)

    assert result == [("River Thames", 3),("River Cam", 2),]


def test_include_ties_at_cutoff():
    """test that all rivers tied with the Nth river are included
    in the returned list"""
    stations = [MockStation("A"),MockStation("A"),MockStation("B"),MockStation("B"),MockStation("C"),MockStation("C"),]

    result = rivers_by_station_number(stations, 1)

    assert len(result) == 3
    assert all(count == 2 for _, count in result)


def test_n_greater_than_number_of_rivers():
    """test that when N is greater than the number of rivers,all rivers are returned"""
    stations = [MockStation("Cam"),MockStation("Cam"),MockStation("Thames"),]

    result = rivers_by_station_number(stations, 10)

    assert result == [("Cam", 2),("Thames", 1),]


def test_ignore_empty_river_names():
    """test that stations with empty or None river names are ignored when counting rivers"""
    stations = [MockStation("Cam"),MockStation(""),MockStation(None),MockStation("Cam"),MockStation("Thames"),]

    result = rivers_by_station_number(stations, 2)

    assert result == [("Cam", 2),("Thames", 1),]


def test_empty_station_list():
    """test that an empty station list returns an empty result"""
    stations = []

    result = rivers_by_station_number(stations, 5)

    assert result == []
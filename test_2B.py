from floodsystem.station import MonitoringStation
from floodsystem.station import stations_level_over_threshold


def test_relative_water_level_typical():
    """tests relative water level for consistent range"""

    s = MonitoringStation(
        station_id="test-id",
        measure_id="test-measure",
        label="Test Station",
        coord=(0.0, 0.0),
        typical_range=(0.0, 10.0),
        river="Test River",
        town="Test Town"
    )

    s.latest_level = 5.0
    assert s.relative_water_level() == 0.5


def test_relative_water_level_none_typical_range():
    """tests relative water level when typical range is missing"""

    s = MonitoringStation(
        "id", "measure", "label", (0, 0), None, "river", "town"
    )

    s.latest_level = 5.0
    assert s.relative_water_level() is None


def test_relative_water_level_inconsistent_range():
    """tests relative water level for inconsistent typical range"""

    s = MonitoringStation(
        "id", "measure", "label", (0, 0), (10.0, 5.0), "river", "town"
    )

    s.latest_level = 7.0
    assert s.relative_water_level() is None


def test_stations_over_threshold_basic():
    """test stations correctly filtered and sorted out"""

    s1 = MonitoringStation("id1", "m1", "Station 1", (0, 0), (0.0, 10.0), "r", "t")
    s2 = MonitoringStation("id2", "m2", "Station 2", (0, 0), (0.0, 10.0), "r", "t")
    s3 = MonitoringStation("id3", "m3", "Station 3", (0, 0), (0.0, 10.0), "r", "t")

    s1.latest_level = 9.0   # relative = 0.9
    s2.latest_level = 7.0   # relative = 0.7
    s3.latest_level = 8.5   # relative = 0.85

    stations = [s1, s2, s3]
    result = stations_level_over_threshold(stations, 0.8)

    assert len(result) == 2
    assert result[0][0].name == "Station 1"
    assert result[1][0].name == "Station 3"


def test_stations_over_threshold_ignores_bad_data():
    """test stations with weird data are ignored"""

    s_good = MonitoringStation("id1", "m1", "Good", (0, 0), (0.0, 10.0), "r", "t")
    s_bad = MonitoringStation("id2", "m2", "Bad", (0, 0), (10.0, 5.0), "r", "t")

    s_good.latest_level = 9.0
    s_bad.latest_level = 9.0

    result = stations_level_over_threshold([s_good, s_bad], 0.8)

    assert len(result) == 1
    assert result[0][0].name == "Good"

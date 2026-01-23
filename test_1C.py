from floodsystem.geo import stations_within_radius
from floodsystem.station import MonitoringStation


def test_stations_within_radius_basic():
    """tests if stations are correctly identified within a given radius"""
    centre = (52.2053, 0.1218)

    s1 = MonitoringStation("id1", "m1", "Station 1",(centre),None, "River A", "Town A")
    s2 = MonitoringStation("id2", "m2", "Station 2",(0.0, 0.0),None, "River B", "Town B")

    stations = [s1, s2]

    result = stations_within_radius(stations, centre, 5)

    assert s1 in result
    assert s2 not in result


def test_stations_within_radius_all_included():
    """test all stations are returned when radius is large enough"""
    centre = (52.2053, 0.1218)

    s1 = MonitoringStation("id1", "m1", "Station 1",(52.0, 0.0),None, "River A", "Town A")
    s2 = MonitoringStation("id2", "m2", "Station 2",(53.0, 1.0),None, "River B", "Town B")

    stations = [s1, s2]

    result = stations_within_radius(stations, centre, 1000)

    assert set(result) == set(stations)

def test_stations_within_radius_empty():
    """Test empty station list returns an empty list"""
    centre = (52.2053, 0.1218)

    result = stations_within_radius([], centre, 10)

    assert result == []


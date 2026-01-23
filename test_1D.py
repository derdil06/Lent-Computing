from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river


from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.station import MonitoringStation


def test_rivers_with_station():
    """test rivers_with_station returns unique river names"""

    stations = [ #fake station names
        MonitoringStation("id1", "m1", "s1", (0, 0), "River Cam", "Town1"),
        MonitoringStation("id2", "m2", "s2", (0, 0), "River Cam", "Town2"),
        MonitoringStation("id3", "m3", "s3", (0, 0), "River Thames", "Town3"),]

    rivers = rivers_with_station(stations)
    assert isinstance(rivers, set)
    assert rivers == {"River Cam", "River Thames"}


def test_stations_by_river():
    """test stations_by_river groups stations correctly"""

    s1 = MonitoringStation("id1", "m1", "Cambridge", (0, 0), "River Cam", "Cambridge")
    s2 = MonitoringStation("id2", "m2", "Jesus Lock", (0, 0), "River Cam", "Cambridge") #i miss rowing on the cam :/
    s3 = MonitoringStation("id3", "m3", "Oxford", (0, 0), "River Thames", "Oxford")
    stations = [s1, s2, s3]
    rivers_dict = stations_by_river(stations)
    assert isinstance(rivers_dict, dict)
    assert set(rivers_dict.keys()) == {"River Cam", "River Thames"}

    cam_names = [station.name for station in rivers_dict["River Cam"]] 
    thames_names = [station.name for station in rivers_dict["River Thames"]]

    assert cam_names == ["Cambridge", "Jesus Lock"]
    assert thames_names == ["Oxford"]

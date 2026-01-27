from floodsystem.station import stations_highest_rel_level
from floodsystem.station import MonitoringStation


def test_stations_highest_rel_level():
    """test that stations_highest_rel_level returns the correct stations
    in descending order of relative water level"""

    s1 = MonitoringStation(station_id="s1",measure_id="m1",label="Station 1",coord=(0, 0),typical_range=(0.0, 1.0),river="River A",town="Town A")
    s2 = MonitoringStation(station_id="s2",measure_id="m2",label="Station 2",coord=(0, 0),typical_range=(0.0, 2.0),river="River B",town="Town B")
    s3 = MonitoringStation(station_id="s3",measure_id="m3",label="Station 3",coord=(0, 0),typical_range=(1.0, 3.0),river="River C",town="Town C")

    s1.latest_level = 0.9   #relative level = 0.9
    s2.latest_level = 1.0   #relative level = 0.5
    s3.latest_level = 3.0   #relative level = 1.0

    stations = [s1, s2, s3]
    result = stations_highest_rel_level(stations, 2)
    assert len(result) == 2 #check correct number of stations returned
    assert result[0].name == "Station 3" #Check ordering (highest relative level first)
    assert result[1].name == "Station 1"
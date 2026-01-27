from datetime import datetime, timedelta
from floodsystem.station import plot_water_levels
from floodsystem.station import MonitoringStation


def test_plot_water_levels_runs_without_error():
    """test plot_water_levels executes without raising an exception"""

    #create a fake monitoringStation
    station = MonitoringStation(station_id="test-id",measure_id="test-measure",label="Test Station",coord=(0.0, 0.0),typical_range=(0.2, 1.2),river="Test River",town="Test Town")

    dates = [datetime.now() - timedelta(days=i) for i in range(5)]
    levels = [0.3, 0.5, 0.7, 0.6, 0.4]

    plot_water_levels(station, dates, levels)


def test_station_relative_water_level_sorting():
    """test that stations are correctly sorted by relative water level"""

    s1 = MonitoringStation("id1", "m1", "Station 1", (0, 0),typical_range=(0.0, 1.0),river="R1", town="T1")
    s2 = MonitoringStation("id2", "m2", "Station 2", (0, 0),typical_range=(0.0, 2.0),river="R2", town="T2")
    s3 = MonitoringStation("id3", "m3", "Station 3", (0, 0),typical_range=None,river="R3",town="T3")    # invalid

    s1.latest_level = 0.5    # relative = 0.5
    s2.latest_level = 1.5    # relative = 0.75
    s3.latest_level = 1.0    # relative = None
    stations = [s1, s2, s3]

    #filter out invalid stations
    stations = [s for s in stations if s.relative_water_level() is not None]

    stations.sort(key=lambda s: s.relative_water_level(),reverse=True)

    #ordering
    assert stations[0].name == "Station 2"
    assert stations[1].name == "Station 1"
    assert len(stations) == 2

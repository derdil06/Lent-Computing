from datetime import timedelta, datetime

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import plot_water_levels
from floodsystem.station import MonitoringStation


def run():
    stations = build_station_list() #build station list and update latest water levels
    update_water_levels(stations)
    stations = [s for s in stations if s.relative_water_level() is not None] #remove stations with no relative water level
    stations.sort(key=lambda s: s.relative_water_level(),reverse=True) #sort by relative water level (descending)
    top_stations = [s for s in stations if s.relative_water_level() is not None][:5] #select top 5 stations with valid relative water levels

    dt = timedelta(days=10) ## time range (past 10 days)
    now = datetime.utcnow()

    for station in top_stations:    #plot water levels
        dates, levels = fetch_measure_levels(station.measure_id,dt=dt)
        plot_water_levels(station, dates, levels)
if __name__ == "__main__":
    run()

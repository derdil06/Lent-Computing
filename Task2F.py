import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from datetime import timedelta
from floodsystem import station
from floodsystem.station import polyfit
from floodsystem.station import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    
    stations = build_station_list()
    update_water_levels(stations)

    stations = [s for s in stations if s.relative_water_level() is not None]
    stations.sort(key=lambda s: s.relative_water_level(), reverse=True)
    top5 = stations[:5]

    for station in top5:

        dates, levels = fetch_measure_levels(
            station.measure_id,
            dt=timedelta(days=2))

        if dates and levels:
            plot_water_level_with_fit(station, dates, levels, 4)


if __name__ == "__main__":
    run()
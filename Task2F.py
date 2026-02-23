import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from datetime import timedelta
from floodsystem.station import polyfit
from floodsystem.station import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)

    station = None
    for s in stations:
        if s.latest_level is not None:
            station = s
            break

    if station is None:
        print('No station with data found.')
        return
    
    dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=2))

    degree = 4

    poly, d0 = polyfit(dates, levels, degree)
    plt.plot(dates, levels, '.', label="Actual")
    x_float = matplotlib.dates.date2num(dates) - d0
    y_fit = poly(x_float)
    plt.plot(dates, y_fit, '-', label=f"fit (deg={degree})")

    plt.xlabel('Date')
    plt.ylabel('Water level (m)')
    plt.title(station.name)
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run()


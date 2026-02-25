import matplotlib
import matplotlib.pyplot as plt
from datetime import timedelta
import numpy as np
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import polyfit

def get_risk_assessment(n=10):
    stations = build_station_list()
    update_water_levels(stations)

    risk_list = []

    for st in stations:
        if st.latest_level is None:
            continue

        rel = st.relative_water_level()
        if rel is None:
            continue

        dates, levels = fetch_measure_levels(st.measure_id, dt=timedelta(days=2))

        p, d0 = polyfit(dates, levels, 4)

        x_last = matplotlib.dates.date2num(dates[-1]) - d0
        slope = np.polyder(p)(x_last)

        risk = rel + slope

        risk_list.append((st.name, risk))

    risk_list.sort(key=lambda x: x[1], reverse=True)

    return [name for name, r in risk_list[:n]]
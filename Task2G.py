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

    #first filter valid stations
    stations = [s for s in stations
        if s.latest_level is not None
        and s.relative_water_level() is not None]

    #sort by current relative level first
    stations.sort(key=lambda s: s.relative_water_level(), reverse=True)

    #only examine top 20 for trend analysis 
    stations = stations[:20]

    town_risk = {}

    for st in stations:

        rel = st.relative_water_level()

        dates, levels = fetch_measure_levels(
            st.measure_id,
            dt=timedelta(days=2)
        )

        if not dates or len(dates) < 2:
            continue

        p, d0 = polyfit(dates, levels, 4)

        x_last = matplotlib.dates.date2num(dates[-1]) - d0
        slope = np.polyder(p)(x_last)
        slope = max(min(slope, 5), -5)

        risk = rel + slope

        if st.town:
            if st.town not in town_risk:
                town_risk[st.town] = risk
            else:
                town_risk[st.town] = max(town_risk[st.town], risk)

    sorted_towns = sorted(
        town_risk.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_towns[:n]

def run():
    results = get_risk_assessment(10)

    print("Top towns at risk of flooding:\n")

    for town, score in results:
        print(f"{town}: {score:.3f}")


if __name__ == "__main__":
    run()
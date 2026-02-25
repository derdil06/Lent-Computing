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
    town_risk = {}

    for st in stations:
        if st.latest_level is None:
            continue

        rel = st.relative_water_level()
        if rel is None:
            continue

        dates, levels = fetch_measure_levels(st.measure_id, dt=timedelta(days=2))

        if len(dates) < 2:
            continue

        p, d0 = polyfit(dates, levels, 4)

        x_last = matplotlib.dates.date2num(dates[-1]) - d0
        slope = np.polyder(p)(x_last)

        risk = rel + slope

        if st.town:
            if st.town not in town_risk:
                town_risk[st.town] = risk
            else:
                town_risk[st.town] = max(town_risk[st.town], risk)

    sorted_towns = sorted(town_risk.items(), key=lambda x: x[1], reverse=True)

    return sorted_towns[:n]


def classify_risk(score):
    """classify numerical risk into warning category"""
    if score > 2:
        return "Severe"
    elif score > 1.5:
        return "High"
    elif score > 1:
        return "Moderate"
    else:
        return "Low"

def run():
    results = get_risk_assessment(10)
    print("Top towns at risk of flooding:\n")
    for town, score in results:
        category = classify_risk(score)
        print(f"{town}: {category} (risk score = {score:.3f})")


if __name__ == "__main__":
    run()
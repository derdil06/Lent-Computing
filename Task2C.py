from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import stations_highest_rel_level


def run():
    """build station list, update water levels, and print the 10 stations with
    the highest relative water levels"""
    stations = build_station_list() #build list of stations and update water levels
    update_water_levels(stations)

    highest_stations = stations_highest_rel_level(stations, 10) #get the 10 stations most at risk

    for station in highest_stations:
        print(station.name, station.relative_water_level())

if __name__ == "__main__":
    run()
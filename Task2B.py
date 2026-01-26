from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import stations_level_over_threshold


def run():

    stations = build_station_list()
    update_water_levels(stations)

    tol = 0.8 #this is quite low, returns a lot of stations, might be worth putting higher (or might just be a rainy day)
    stations_over = stations_level_over_threshold(stations, tol)

    for station, rel_level in stations_over:
        print(f"{station.name} {rel_level}")


if __name__ == "__main__":
    run()

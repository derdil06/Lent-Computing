from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius


def run():
    """print stations within 10 km of Cambridge city centre."""
    stations = build_station_list()
    cambridge_centre = (52.2053, 0.1218)

    nearby_stations = stations_within_radius(stations, cambridge_centre, 10)

    station_names = sorted(station.name for station in nearby_stations)
    print(station_names)
fhrnfrg

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()

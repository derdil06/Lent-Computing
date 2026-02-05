from haversine import haversine

from floodsystem.stationdata import build_station_list #from1a
from floodsystem.utils import sorted_by_key

def stations_by_distance(stations, p):
    """return a list of (station, distance in km) tuples, sorted by distance"""

    stations_dist = []

    for station in stations: #loops through stations
        dist = haversine(p, station.coord) #finds distance, p is distance in km
        stations_dist.append((station, dist))

    stations_dist = sorted_by_key(stations_dist, 1)
    return stations_dist


def run():
    """print the 10 closest and 10 furthest stations from Cambridge city centre."""
    stations = build_station_list() #makes list
    cambridge_centre = (52.2053, 0.1218)

    stations_dist = stations_by_distance(stations, cambridge_centre)

    print("10 closest stations:")
    for station, dist in stations_dist[:10]:
        print((station.name, station.town, dist))

    print("\n10 furthest stations:")
    for station, dist in stations_dist[-10:]:
        print((station.name, station.town, dist))


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
    print("test")

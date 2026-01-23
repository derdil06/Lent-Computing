from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river


def run():
    """demonstration program for Task 1D."""
    stations = build_station_list()  # list of stations

    rivers = rivers_with_station(stations) #rivers with at least one station
    rivers_sorted = sorted(rivers)

    print(f"{len(rivers_sorted)} rivers. First 10 - {rivers_sorted[:10]}")


    rivers_dict = stations_by_river(stations) #stations by river

    rivers_to_print = ["River Aire", "River Cam", "River Thames"]

    for river in rivers_to_print:
        stations_on_river = rivers_dict.get(river, [])
        station_names = sorted(station.name for station in stations_on_river)
        print(f"\nStations on {river}:")
        print(station_names)


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()

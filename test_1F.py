from floodsystem.stationdata import build_station_list
from Task1F import inconsistent_typical_range_stations

def run():
    """Demonstration program for Task 1F."""
    stations = build_station_list()

    inconsistent = inconsistent_typical_range_stations(stations)

    print("Stations with inconsistent typical range data:")
    for name in inconsistent:
        print(name)

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()

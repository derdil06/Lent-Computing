from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    """Demonstration program for Task 1E."""
    stations = build_station_list()

    # Set N = 9 as required
    N = 9
    result = rivers_by_station_number(stations, N)

    print(f"Rivers with the greatest number of stations when N = {N}:")
    for river, count in result:
        print((river, count))

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()

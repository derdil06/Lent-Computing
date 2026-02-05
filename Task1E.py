from floodsystem.stationdata import build_station_list

def rivers_by_station_number(stations, N):

    # Count how many stations each river has
    river_counts = {}
    for station in stations:
        river = station.river
        # Only count if river is not empty
        if river:
            river_counts[river] = river_counts.get(river, 0) + 1

    # Convert into a list of tuples (river, count)
    sorted_rivers = sorted(river_counts.items(), key=lambda x: x[1], reverse=True)

    # If N is greater than number of rivers, just return everything
    if N >= len(sorted_rivers):
        return sorted_rivers

    # Find the cutoff count (count of the Nth river)
    cutoff_count = sorted_rivers[N - 1][1]

    # Include all rivers with count >= cutoff_count
    result = [item for item in sorted_rivers if item[1] >= cutoff_count]

    return result

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

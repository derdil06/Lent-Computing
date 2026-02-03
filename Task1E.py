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
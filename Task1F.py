def inconsistent_typical_range_stations(stations):
    """Return a sorted list of station names that have inconsistent typical range data.
    A station is inconsistent if: - typical_range is None, or - typical_range_low > typical_range_high"""

    inconsistent = []
    for station in stations:
        # typical_range expected to be a tuple (low, high)
        tr = station.typical_range
        if tr is None:
            inconsistent.append(station.name)
        else:
            low, high = tr
            if low > high:
                inconsistent.append(station.name)

    # return sorted list of names
    return sorted(inconsistent)
# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine


def stations_within_radius(stations, centre, r):
    """return a list of stations within radius r of centre in km"""
    stations_in_radius = []

    for station in stations:
        dist = haversine(centre, station.coord)
        if dist <= r:
            stations_in_radius.append(station)

    return stations_in_radius

def rivers_with_station(stations):
    """returns a set of river names that have at least one monitoring station on them"""

    rivers = set()

    for station in stations:
        rivers.add(station.river)

    return rivers


def stations_by_river(stations):
    """return a dictionary mapping river names to a list of stations on that river"""

    rivers_dict = {}

    for station in stations:
        river = station.river

        if river not in rivers_dict:
            rivers_dict[river] = []

        rivers_dict[river].append(station)

    return rivers_dict

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
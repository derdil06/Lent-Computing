# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine


def stations_within_radius(stations, centre, r):
    """return a list of stations within r of centre."""
    stations_in_radius = []

    for station in stations:
        dist = haversine(centre, station.coord)
        if dist <= r:
            stations_in_radius.append(station)

    return stations_in_radius

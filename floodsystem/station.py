# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):
        """Create a monitoring station."""

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d


    def relative_water_level(self):
        """returns the latest water level as a fraction of the typical range"""

        if self.latest_level is None: #check data availability
            return None

        if self.typical_range is None:
            return None

        typical_low, typical_high = self.typical_range

        if typical_low >= typical_high: #check for inconsistent typical range
            return None

        return (self.latest_level - typical_low) / (typical_high - typical_low)
    
def stations_level_over_threshold(stations, tol):
    """return stations where relative water level exceeds a given threshold"""

    stations_over_tol = []

    for station in stations:
        rel_level = station.relative_water_level()
        if rel_level is not None and rel_level > tol:
            stations_over_tol.append((station, rel_level))

    stations_over_tol.sort(key=lambda x: x[1], reverse=True)

    return stations_over_tol


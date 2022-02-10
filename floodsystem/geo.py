# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

from haversine import haversine

def stations_within_radius(stations,centre,r):
    valid_stations = []
    
    for station in stations:
       distance = haversine(station.coord, centre)
       if distance <= r:
        valid_stations.append(station.name)
        sorted_valid_stations = sorted(valid_stations)
    return(sorted_valid_stations)

def stations_by_distance(stations, p):
    stations_distances = []
    for i in stations:
        location = stations[i]
        distance = haversine(p, location[1])
        stations_distances.append(distance,location[0])
    sorted_stations = utils.sort_by_key(stations_distances)

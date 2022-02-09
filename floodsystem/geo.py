# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.stationdata import build_station_list
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

def rivers_by_station_number(stations, N):
    river_tuples_list = [("none",0)]
    river_dict = {}
    river_list = []
    for station in stations:
        river = station.river
        if river not in river_list:
            river_list.append(station.river)
            river_dict[river] = 1
        else:
            river_dict[river] += 1
    for river in river_dict:
        river_count = river_dict[river]
        for i in range(0,min(len(river_tuples_list),N)):
            if river_count >= river_tuples_list[i][1]:
                river_tuples_list.insert(i, (river,river_count))
                break
    for i in range(N,len(river_tuples_list)):
        if river_tuples_list[i][1] != river_tuples_list[N-1][1]:
            break      
    return river_tuples_list[0:i]

def stations_by_distance(stations, p):
    stations_distances = []
    for i in stations:
        location = stations[i]
        distance = haversine(p, location[1])
        stations_distances.append(distance,location[0])
    sorted_stations = utils.sort_by_key(stations_distances)

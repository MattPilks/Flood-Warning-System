#Matt Pilkington, 01/03/2022

from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """Requirements for Task 1F"""
    print("Task1F")
    full_station_list = build_station_list()
    if DEBUG: print("full_station_list, length: ", len(full_station_list))
    station_list = inconsistent_typical_range_stations(full_station_list)
    if DEBUG: print("station_list, length: ", len(station_list))
    station_name_list = []
    for station in station_list:
        station_name_list.append(station.name)
        if DEBUG: print("station.name:", station.name)
    if DEBUG: print("Station_name_list:", station_name_list)
    station_name_list.sort()
    print("Sorted Inconsistent stations:", station_name_list)


if __name__ == "__main__":
    DEBUG = False
    run()
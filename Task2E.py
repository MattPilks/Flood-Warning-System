from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from datetime import datetime, timedelta
from floodsystem.plot import plot_water_levels
"""Requirements for Task2E"""




def run():
    stations = build_station_list()
    if DEBUG: print("Build_station_list len:", len(stations))
    if not FULL_LIST: stations = stations[0:10]
    station_dict = {}
    highest_level_stations = []
    for station in stations:
        if DEBUG: print("fetching measure level for current station:", station.name, station.measure_id)
        date_list , level_list = fetch_measure_levels(station.measure_id, timedelta(hours=24))
        station_dict[station.name] = level_list[0] if len(level_list) > 0 else 0
        if DEBUG: print("measure level for current station:", station_dict[station.name])
    sorted_list = sorted(station_dict.items(), key = lambda x: x[1], reverse=True)
    if DEBUG: print("sorted_list: ", sorted_list)
    for item in sorted_list:
        highest_level_stations.append(item[0])
    highest_five_stations = highest_level_stations[0:5]
    print("highest_five_stations: ", highest_five_stations)

    for station in stations:
        for topstation in highest_five_stations:
            if station.name == topstation:
                if DEBUG: print("fetching measure level for current station:", station.name, station.measure_id)
                date_list , level_list = fetch_measure_levels(station.measure_id, timedelta(days=10))
                plot_water_levels(station,date_list,level_list)

if __name__ == "__main__":
    DEBUG = False
    FULL_LIST = False
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
    



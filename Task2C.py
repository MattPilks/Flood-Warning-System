from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

def run():
    station_list = build_station_list()

    # Update latest level data for all stations
    update_water_levels(station_list)
    sorted_list = stations_highest_rel_level(station_list,10)
    processed_list = []
    for tpl in sorted_list:
        processed_list.append((tpl[0].name, tpl[1]))
    print(processed_list)


if __name__ == "__main__":
    
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
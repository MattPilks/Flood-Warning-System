from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    station_list = build_station_list()

    # Update latest level data for all stations
    update_water_levels(station_list)



    sorted_list = stations_level_over_threshold(station_list,0.8)
    processed_list = []
    for tpl in sorted_list:
        processed_list.append((tpl[0].name, tpl[1]))
    print(processed_list)


if __name__ == "__main__":
    
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
    
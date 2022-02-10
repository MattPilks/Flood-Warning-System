from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1F"""
    station_list = build_station_list()
    i = 0
    for station in station_list:
        i +=1
        print(station)
        cons = station.typical_range_consistent()
        print("   consistent:   " , cons, "               <----------------------------------------------------------------------------------------- INCONSISTENCY" if not cons else "")
        print("   index:        ",i)    

if __name__ == "__main__":
    run()
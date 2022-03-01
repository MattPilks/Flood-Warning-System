from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """Requirements for Task 1F"""
    station_list = build_station_list()
    inco_station_list = inconsistent_typical_range_stations(station_list)
    print(inco_station_list)
    inco_names=[]
    for station in inco_station_list:
        inco_names.append(station.name)
    inco_names = sorted(inco_names)
    print(inco_names)


if __name__ == "__main__":
    run()
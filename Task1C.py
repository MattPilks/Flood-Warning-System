#Matt Pilkington, 01/03/2022

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """Requirements for Task 1C"""
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 10
    print(stations_within_radius(stations,centre,r))

if __name__ == "__main__":
    print("List of stations within the radius of acceptance: ")
    run()

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
"""Requirements for Task2E"""





def run():
    stations = build_station_list()
    water_levels_list = []
    highest_station_list = []
    for station in stations:
        water_levels_list.append(fetch_measure_levels(station.measure_id, 0))
        highest_station_list.append(station.name)
        



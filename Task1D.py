from floodsystem.stationdata import build_station_list
from floodsystem.geo import *
def run():
  """Requirement for task D"""
  stations = build_station_list()
  rivers = rivers_with_station(stations)
  rivers = sorted(rivers)
  print(rivers[:10])
  stations_river = stations_by_river(stations)
  Aire = stations_river["Aire"]
  print(Aire)
  Cam = stations_river["Cam"]
  print(Cam)
  Thames = stations_river["Thames"]
  print(Thames)
  
  
if __name__ == "__main__":
    run()

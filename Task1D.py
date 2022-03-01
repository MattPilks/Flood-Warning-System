from floodsystem.stationdata import build_station_list
from floodsystem.geo import *
def run():
  """Requirement for task D, gives stations on a given river"""
  stations = build_station_list()
  rivers = rivers_with_station(stations)
  rivers = sorted(rivers)
  print(rivers[:10])
  stations_river = stations_by_river(stations)
  Aire = stations_river["River Aire"]
  print(Aire)
  Cam = stations_river["River Cam"]
  print(Cam)
  Thames = stations_river["River Thames"]
  print(Thames)
  
  
if __name__ == "__main__":
  run()

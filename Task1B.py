
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
def run():
  """Requirement for task B"""
  stations = build_station_list()
  sorted = stations_by_distance(stations,(52.2053, 0.1218))
  close_ten = sorted[:10]
  farth_ten = sorted[-10:]
  print(close_ten)
  print(farth_ten)
  
if __name__ == "__main__":
  print("Ten closest and ten furthest stations from cambridge city centre are:")
  run()

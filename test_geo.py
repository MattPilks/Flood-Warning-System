from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
from floodsystem.station import MonitoringStation 


"""Making Imaginary Stations"""
def make_stations():
    s1 = MonitoringStation(
        station_id=
        measure_id=
        label=
        coord=
        typical_range=
        river=
        town=
    )

    s2 = MonitoringStation(
        station_id=
        measure_id=
        label=
        coord=
        typical_range=
        river=
        town=
    )

    s3 = MonitoringStation(
        station_id=
        measure_id=
        label=
        coord=
        typical_range=
        river=
        town=
    )






def test_river_by_station_number():
    """Testing function that asserts known return values for given N input"""
    print("Testing river_by_station_number Method:")
    stations = build_station_list()
    river_count_list = rivers_by_station_number(stations,8)
    assert len(river_count_list) == 8 #Correct value = 8
    river_count_list = rivers_by_station_number(stations,9)
    assert len(river_count_list) == 10 #Correct value = 10
    river_count_list = rivers_by_station_number(stations,24)
    assert len(river_count_list) == 29 #Correct value = 29
    print(" Test Passed")


def test_stations_within_radius():
    """Testing Function that asserts known stations within a given radius"""
    print("Testing stations_within_radius Method:")
    stations = build_station_list()
    stations_allowed = stations_within_radius(stations,(52.2053, 0.1218),10)
    assert len(stations_allowed) == 11 #Correct value = 11 for Cambridge city centre and r = 10 for feburary 2022
    print(" Test Passed")

def test_typical_range_consistent():
    """Testing Function that asserts a known inconsistent and consistent station."""
    print("Testing typical_range_consistent Method")
    stations = build_station_list()
    assert stations[0].typical_range_consistent() #Correct value = True for index 0
    assert not stations[1653].typical_range_consistent() #Correct value = False for index 1653
    print(" Test Passed")



def run():
    test_river_by_station_number()
    test_stations_within_radius()
    test_typical_range_consistent()

if __name__ == "__main__":

    print("Testing :")

    run()
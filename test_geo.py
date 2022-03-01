from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list
from floodsystem.geo import *
from floodsystem.station import MonitoringStation 


"""Making Imaginary Stations"""
def make_stations():
    s1 = MonitoringStation(
        station_id=1,
        measure_id=1,
        label="nene station",
        coord=(52.512825, -0.456695),
        typical_range=(2,50),
        river="Nene",
        town="Northampton"
    )

    s2 = MonitoringStation(
        station_id=2,
        measure_id=2,
        label= "ouse station",
        coord=(53.833697, -1.093396),
        typical_range=(25,2),
        river="Ouse",
        town="York"
    
    )

    s3 = MonitoringStation(
        station_id=3,
        measure_id=3,
        label="avon station",
        coord=(52.191044, -1.701045),
        typical_range= None,
        river="Avon",
        town="Stratford"
    )
    return(s1, s2, s3)






def test_river_by_station_number():
    """Testing function that asserts known return values for given N input"""
    print("Testing river_by_station_number Method:")
    stations = make_stations()
    river_count_list = rivers_by_station_number(stations,3)
    assert len(river_count_list) == 3 #Correct value = 3
    print(" Test Passed")


def test_stations_within_radius():
    """Testing Function that asserts known stations within a given radius"""
    print("Testing stations_within_radius Method:")
    stations = make_stations()
    stations_allowed = stations_within_radius(stations,(52.212064, -1.671348),10)
    assert len(stations_allowed) == 1 #Correct value = 1 for station in stratford upon avon
    print(" Test Passed")

def test_typical_range_consistent():
    """Testing Function that asserts a known inconsistent and consistent station."""
    print("Testing typical_range_consistent Method")
    stations = make_stations()
    assert stations[0].typical_range_consistent() #Correct value = True for index 0
    assert not stations[1].typical_range_consistent() #Correct value = False for index 1653
    print(" Test Passed")


def test_stations_by_distance():
    """Testing Function that asserts a known closest station"""
    print("Tesiting test_stations_by_distance Method")
    stations = make_stations()
    stations_distances = stations_by_distance(stations, (52.475844,-1.889093))
    assert(stations_distances[0][1].name) == "avon station"
    print(" Test Passed")



def run():
    
    test_river_by_station_number()
    test_stations_within_radius()
    test_typical_range_consistent()
    test_stations_by_distance()
if __name__ == "__main__":

    print("Testing :")

    run()
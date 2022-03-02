"""Unit test for the utils module"""
from floodsystem.flood import *
from floodsystem.station import MonitoringStation 

def make_flood_test_stations():
    s1 = MonitoringStation(
        station_id=1,
        measure_id=1,
        label="nene station",
        coord=(52.512825, -0.456695),
        typical_range=(2,50),
        river="Nene",
        town="Northampton",
        
    )

    s2 = MonitoringStation(
        station_id=2,
        measure_id=2,
        label= "ouse station",
        coord=(53.833697, -1.093396),
        typical_range=(2,25),
        river="Ouse",
        town="York",
        
    
    )

    s3 = MonitoringStation(
        station_id=3,
        measure_id=3,
        label="avon station",
        coord=(52.191044, -1.701045),
        typical_range= (1,3),
        river="Avon",
        town="Stratford",
        

    )
    s1.latest_level = 26
    s2.latest_level = 2
    s3.latest_level = 3
    return(s1, s2, s3)

def test_stations_level_over_threshold():
    station_list  = make_flood_test_stations()
    processed_list = stations_level_over_threshold(station_list,0.4)
    assert processed_list[0][1] == 1
    assert processed_list[1][1] == 0.5


def test_stations_highest_rel_level():
    station_list = make_flood_test_stations()
    processed_list = stations_highest_rel_level(station_list,2)
    assert processed_list[0][1] == 1
    assert processed_list[1][1] == 0.5
    assert len(processed_list) ==2




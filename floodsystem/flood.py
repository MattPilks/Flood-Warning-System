from operator import itemgetter

def stations_level_over_threshold(stations,tol):
    stations_over = []
    for station in stations:
        if (waterLevel := station.relative_water_level()) != None:
            if waterLevel > tol:
                stations_over.append((station, station.relative_water_level()))
    
    stations_over = sorted(stations_over, key=itemgetter(1))
    stations_over.reverse()
    return stations_over


def stations_highest_rel_level(stations, N):
    danger_sorted_list = stations_level_over_threshold(stations,-0.5)
    i = 0
    most_at_risk = []
    while i < N:
        most_at_risk.append((danger_sorted_list[i][0], danger_sorted_list[i][1]))
        i = i +1
    return most_at_risk
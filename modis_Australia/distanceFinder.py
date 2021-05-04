import pandas as pd
import math
import time
"""
    this scrip calculates the distance between each fire and all the cities
    and indexes the fire to the closest city

    to get the distance between city and fire its used haversine formula
    witch looks like this:
    formula: a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
             c = 2 ⋅ atan2( √a, √(1−a) )
             d = R ⋅ c

    where: Δλ -> diference between longitudes
           Δφ -> diference between latitudes
           R  -> earth’s radius
"""
starTime = time.time()

print('reading cities...')
cities = pd.read_csv('cities\citiesF.csv')

print('reading fires...')
fires = pd.read_csv('modis_Australia\modis_2008-2017F.csv')

fireCity = []

print('calculating distance between fire and nearest city...')
R = 6371e3
for fire in fires.values:
    lat1 = fire[0] * math.pi
    lng1 = fire[1] * math.pi
    distances = []
    for city in cities.values:
        lat2 = city[1] * math.pi
        lng2 = city[2] * math.pi
        Dlat = (lat1 - lat2) * math.pi / 180
        Dlng = (lng1 - lng2) * math.pi / 180

        a = abs(pow((math.sin(Dlat / 2)), 2) + math.cos(lat1) *
                math.cos(lat2) * pow((math.sin(Dlng / 2)), 2))
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = R * c
        distances.append([city[0], d])
    lDistance = distances[0]
    for distance in distances:
        if distance[1] < lDistance[1]:
            lDistance = distance
    fireCity.append(lDistance[0])

fires.insert(2, 'city', fireCity, False)

fires.to_csv(
    'modis_Australia\modis_2008-2017Cities.csv',
    header=['latitude', 'longitude', 'city', 'brightness',
            'acq_date', 'confidence', 'daynight'], index=None)

endTime = time.time()

print(endTime - starTime)

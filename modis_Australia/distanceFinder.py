import pandas as pd
import math
"""
    this scrip calculates the distance between each fire and all the cities 
    and indexes the fire to the closest city

    to get the distance between city and fire its used Equirectangular approximation 
    witch looks like this:
    Formula: x = Δλ ⋅ cos φm
             y = Δφ
             d = R ⋅ √(x² + y²)
    
    where: Δλ -> diference between longitudes
           Δφ -> diference between latitudes
           R  -> earth’s radius
"""

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

        x = (lng2 - lng1) * math.cos((lat1 - lat2)/2)
        y = (lat2 - lat1)
        d = math.sqrt(x**2 + y**2) * R
        distances.append([city[0], d])
    lDistance = distances[0]
    for distance in distances:
        if distance[1] < lDistance[1]:
            lDistance = distance
    fireCity.append(lDistance[0])

fires.insert(2, 'city', fireCity, False)

fires.to_csv(
    'modis_Australia/modis_2008-2017FC.csv',
    header=['latitude', 'longitude', 'city', 'brightness',
            'acq_date', 'confidence', 'daynight'], index=None)

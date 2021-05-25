import pandas as pd

dates = pd.read_csv('Data Warehouse\Date\daysI.csv')
cities = pd.read_csv('Data Warehouse\Location\citiesI.csv')

rFires = pd.read_csv('Datasets\modis_Australia\modis_2008-2017Cities.csv')

f = []

for fire in rFires.values:
    cityId = cities.query('location == @fire[2]').values[0][0]
    dateF = [int(data) for data in fire[4].split('-')]
    dateId = dates.query(
        'year == @dateF[0] & month == @dateF[1] & day == @dateF[2]').values[0][0]
    f.append({'dateId': dateId, 'locationId': cityId, 'brightness': fire[3],
              'confidence': fire[5], 'dayNight': fire[6], 'longitude': fire[0], 'latitude': fire[1]})

fires = pd.DataFrame(f)
print(fires)

fires.to_csv('Data Warehouse/Fires/fires.csv', header=['dateId', 'locationId', 'brightness',
                                                       'confidence', 'dayNight', 'longitude', 'latitude'], index=False)

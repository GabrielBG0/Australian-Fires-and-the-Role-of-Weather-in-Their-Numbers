import pandas as pd

dates = pd.read_csv('Data Warehouse\Date\daysI.csv')
cities = pd.read_csv('Data Warehouse\Location\citiesI.csv')

rWeath = pd.read_csv('Datasets\weatherAUS\weatherAUSF.csv')

w = []

for day in rWeath.values:
    cityId = cities.query('location == @day[1]').values
    if cityId.size == 0:
        print(day[1])
    cityId = cityId[0][0]
    dateF = [int(data) for data in day[0].split('-')]
    dateId = dates.query(
        'year == @dateF[0] & month == @dateF[1] & day == @dateF[2]').values[0][0]
    w.append({'dateId': dateId, 'locationId': cityId,
             'mimTemp': day[2], 'maxTemp': day[3], 'rainfall': day[4], 'windGustDir': day[5], 'windGustSpeed': day[6]})


weather = pd.DataFrame(w)
print(weather)

weather.to_csv('Data Warehouse\Weather\weather.csv', header=[
               'dateId', 'locationId', 'mimTemp', 'maxTemp', 'rainfall', 'windGustDir', 'windGustSpeed'], index=False)

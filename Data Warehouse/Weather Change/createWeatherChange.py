import pandas as pd

dates = pd.read_csv('Data Warehouse\Date\daysI.csv')

rWeath = pd.read_csv('Datasets\Temperature change\DateTempChanges.csv')

w = []

for day in rWeath.values:
    dateF = [int(data) for data in day[0].split('-')]
    dateId = dates.query(
        'year == @dateF[0] & month == @dateF[1] & day == @dateF[2]').values[0][0]
    w.append({'dateid': dateId,
             'temperaturechange': day[1], 'standarddeviation': day[2], 'period': day[3]})


weather = pd.DataFrame(w)
print(weather)

weather.to_csv('Data Warehouse\Weather Change\weatherChange.csv', header=[
               'dateid', 'temperaturechange', 'standarddeviation', 'period'], index=False)

import pandas as pd

db = pd.read_csv('Data Warehouse\Date\days.csv')

for i in range(len(db)):
    if db['month'][i] == 9:
        db['season'][i] = 4
    if db['month'][i] == 10:
        db['season'][i] = 4
    if db['month'][i] == 11:
        db['season'][i] = 4
    if db['month'][i] == 1:
        db['season'][i] = 1

db.to_csv('Data Warehouse\Date\days1.csv', header=[
          'year', 'month', 'day', 'season'], index=False)


db.index += 1


db.to_csv('Data Warehouse\Date\daysI.csv',
          header=['year', 'month', 'day', 'season'])

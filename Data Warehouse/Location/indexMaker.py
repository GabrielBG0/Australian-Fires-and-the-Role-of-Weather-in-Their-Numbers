import pandas as pd

db = pd.read_csv('Data Warehouse\Location\cities.csv')

db.index += 1

db.to_csv('Data Warehouse\Location\citiesI.csv',
          header=['location', 'latitude', 'longitude'])

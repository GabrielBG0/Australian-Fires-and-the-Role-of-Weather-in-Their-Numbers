import pandas as pd

fires = pd.read_csv('modis_Australia\modis_2008-2017F.csv')

for index, fire in fires.iterrows():
    print([index, fire['latitude']])
    break

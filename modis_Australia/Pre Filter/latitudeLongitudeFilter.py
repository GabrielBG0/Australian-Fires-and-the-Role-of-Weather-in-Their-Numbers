import pandas as pd
import numpy as np

print('lendo dados...')
data = pd.read_csv('modis_Australia\modis_2008-2017.csv')
print('leitura completa')

print('filtrando dados por Geo Localisação')
filteredData = []
for pair in data.values:
    if (pair[0] <= np.float64(-27.38646) and pair[0] >= np.float64(-43.67288)) and (pair[1] <= np.float64(153.48215) and pair[1] >= np.float64(140.48572)):
        filteredData.append(pair)

print('a quntidade de dados foi filtrada de ' +
      str(len(data)) + ' para ' + str(len(filteredData)))

pd.DataFrame(filteredData).to_csv('modis_Australia\modis_2008-2017F.csv', header=[
    'latitude', 'longitude', 'brightness', 'acq_date', 'confidence', 'daynight'], index=None)

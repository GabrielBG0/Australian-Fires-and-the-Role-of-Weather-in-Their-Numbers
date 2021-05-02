import numpy as np
import pandas as pd
import random

print('lendo dados...')
data = np.genfromtxt('Map visualisation\MapDataU.csv', delimiter=',')
print('leitura completa')

print('filtrando dados por Geo Localisação')
filteredData = []
for pair in data:
    if (pair[0] <= np.float64(-27.38646) and pair[0] >= np.float64(-43.67288)) and (pair[1] <= np.float64(153.48215) and pair[1] >= np.float64(140.48572)):
        filteredData.append(pair)

print('a quntidade de dados foi filtrada de ' +
      str(len(data)) + ' para ' + str(len(filteredData)))

print('selecionando 2000 randons')
newData = []
for _ in range(1999):
    newData.append(filteredData[random.randint(0, len(filteredData))])
print('salvando...')
pd.DataFrame(newData).to_csv('Map visualisation\MapData.csv', header=[
    'latitude', 'longitude'], index=None)

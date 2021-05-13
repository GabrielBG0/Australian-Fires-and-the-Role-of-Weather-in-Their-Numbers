# Australia-weather-and-fire-analysis

## 1. Motivação

Este trabalho tem como objetivo investigar o impacto das mudanças climáticas nos incêndios florestais na Austrália. Após a análise dos dados é esperado que três principais perguntas sejam respondidas, sendo elas: 1. Existe correlação entre o aumento da temperatura e a quantidade de focos de incêndio? 2. É possível prever a quantidade de focos de incêndio em um dado mês/ano baseando-se em sua variação de temperatura? 3. Como as condições climáticas locais podem afetar um foco de incêndio?
Com as respostas para essas perguntas é possível não só tomar decisões melhor fundamentadas para a criação de políticas climáticas, mas também organizar respostas mais rápidas aos focos de incêndio e criar planos de prevenção para áreas consideradas de risco.

## 2. Dados

Nesta seção será abordado quais dados serão utilizados para a análise, bem como suas origens e estruturas.

### 2.1. Datasets

Os dados utilizados neste trabalho são originários de quatro diferentes fontes, quais sejam: MODIS da NASA, Australian Bureau of Meteorology, FAO e Simple Maps.
</br>
Os dados referentes a focos de incêndio e anomalias térmicas são gerados pelo satélite [MODIS](https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms) da NASA e o dataset completo está disponível através deste [link](https://www.kaggle.com/gabrielbgutierrez/satellite-data-on-australia-fires).
</br>
Os dados referentes a condições climáticas por cidade foram gerados pelo Escritório de Meteorologia da Austrália ([Australian Bureau of Meteorology](http://www.bom.gov.au/climate/data/)) e podem ser acessados [aqui](https://www.kaggle.com/jsphyg/weather-dataset-rattle-package).
</br>
Dados referentes a variações climáticas por ano são dados distribuídos pela [FAO](http://www.fao.org/home/en) e coletados pela [NASA-GISS](https://data.giss.nasa.gov/gistemp/) e podem ser acessados [aqui](https://www.kaggle.com/sevgisarac/temperature-change).
</br>
Por fim, os dados referentes a coordenadas geográficas de cada cidade são originados do dataset [Simple Maps](https://simplemaps.com/data/au-cities) Austrália.
Além dos links contidos acima é possível acessar todos os datasets utilizados na íntegra através do [repositório](https://github.com/GabrielBG0/Australia-weather-and-fire-analysis) do trabalho.
</br>
Ao final do documento estará presente uma relação de todos os atributos dos datasets utilizados, seus significados e quais deles foram escolhidos para serem utilizados.

#### 2.1.1. Anomalias Térmicas

O dataset de anomalias térmicas é composto de leituras do satélite modis de 2000 até 2019, com os campos latitude, longitude, brightness, scan, track, acq_date, acq_time, satellite, instrument, confidence, version, bright_t31, frp, day/night e type. Ao todo, o dataset tem 5.081.221 de medições ao longo de 20 anos.
Para este trabalho, contudo, serão usados apenas dados de 2008 até 2017, uma vez que esse é o período de tempo de intercessão entre todos os dados utilizados. Também não serão utilizados todos os campos presentes no dataset, mas se considerará a latitude, longitude, brightness, acq_date, confidence e day/night, campos que foram julgados mais importantes por conterem informações únicas e úteis aos propósitos deste estudo.
Foi criada uma geofence para delimitar uma área de estudo. Para o trabalho apenas a área entre as latitudes -27.38646 e -43.67288 e as longitudes 153.48215 e 140.48572 foi considerada, uma vez que é nessa área que se concentra a maioria das cidades presentes do dataset de dados meteorológicos. Após a delimitação da área, aproximadamente dois milhões de leituras serão consideradas para o trabalho.

#### 2.1.2. Dados Meteorológicos

O dataset, contendo os dados meteorológicos, tem informações de 2008 até a metade de 2017, com os campos Date, Location, Min Temp, Max Temp, Rainfall, Evaporation, Sunshine, Wind Gust Dir, Wind Gust Speed, WindSor 9am, Wind Dir 3pm, Wind Speed 9am, Wind Speed 3pm, Humidity 9am, Humidity 3pm, Pressure 9am, Pressure 3pm, Cloud 9am, Cloud 3pm, Temp 9am, Temp 3pm, Rain Today, Rain Tomorrow e um total de 145.461 medições de 49 locais diferentes. Para este trabalho serão usados campos date, location, min Temp, max Temp, rainfall, wind Gust Dir, wind Gust Speed e as leituras de 31 cidades.
Os cortes nos campos foram realizados em função da redundância de dados e inconsistência na medição de alguns campos, como evaporation e sunshine. Além disso, Rain Today e Rain Tomorrow foram retirados, uma vez que fogem ao escopo do trabalho.
Também, 18 cidades foram cortadas para o trabalho, uma vez que se encontravam muito distantes das outras cidades. Após os cortes, serão utilizadas aproximadamente 85 mil medições.

#### 2.1.3. Variação de Temperatura

O dataset contendo a variação de temperatura contém dados sobre mudança de temperatura e desvio padrão mensal, sazonal e anual de 1961 até 2019, para a Austrália como um todo. Como falado anteriormente, apenas dados de 2008 até 2017 serão utilizados no trabalho. Os campos Area Code, Months Code, Element Code e Unit foram cortados pela sua insignificância para o projeto. Após as delimitações, obtém-se 350 medições a serem consideradas.

#### 2.1.4. Cidades

Como as medições de satélite têm sua localização marcada como coordenadas geográficas, e as medições meteorológicas usam o nome da cidade para ser identificadas é necessário estabelecer um elo entre os dois dataset. O dataset de cidades faz exatamente isso, ele contém o nome da cidade e as coordenadas geográficas referentes a ela. As cidades utilizadas estão distribuídas da seguinte maneira:

![photo1](https://github.com/GabrielBG0/Australia-Weather-and-Fire-Analysis/blob/main/visual%20resourses/cities%20map.jpeg?raw=true)
![photo2](https://github.com/GabrielBG0/Australia-Weather-and-Fire-Analysis/blob/main/visual%20resourses/cities%20map%202.jpeg?raw=true)

Nas fotos, as cidades representadas por roxo estão localizadas na região de Austrália meridional. As cidades representadas em vermelho estão localizadas na região de Vitória.
As cidades representadas por laranja escuro são da região de Nova Gales do Sul. As cidades em laranja claro pertencem à região de Queensland e por fim, as cidades em amarelo se encontram na Tasmânia.

### 2.2 Data Warehouse

Para apresentar o Data Warehouse vamos, primeiramente, trazer a modelagem do mesmo.

#### 2.2.1 Modelagem

![modelagem](https://github.com/GabrielBG0/Australia-Weather-and-Fire-Analysis/blob/main/visual%20resourses/DW%20Model.png?raw=true)

#### 2.2.2 Tabelas Fato

A modelagem inclui as seguintes tabelas fato:

- Weather, com as informações de temperatura mínima, temperatura máxima, precipitação, direção do vento e velocidade do vento como fatos.
- Fires, com as informações de brilho, confiança, dia/noite, latitude exata, longitude exata como fatos.
- Weather Variation, com as informações de mudança de temperatura e desvio padrão como fatos.

#### 2.2.3 Dimensões

O data warehouse conta comasdimensõesdo _tempo_ , representado por Data, e ado
_espaço_ , representado por Localização.

A dimensão Data tem como atributos dia, mês, ano e estação, que é representada por um
inteiro seguindo a ordem das estações no hemisfério sul, sendo elas: 1-Verão, 2-Outono,
3-Inverno e 4-Primavera. É importante ressaltar que o verão de um ano começa sempre no
mês de dezembro do ano anterior, por isso janeiro de 2017 e dezembro de 2016 são parte
do mesmo verão.

A dimensão Localização é representada por cidade eas suas coordenadas geográficas.
Natabela fato Fires tambémestãopresentes coordenadas geográficas, masessassão
referentes ao foco em si, e não à cidade a qual o foco pertence.

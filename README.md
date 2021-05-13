# Australia-weather-and-fire-analysis

```
Gabriel Borges Gutierrez
```
## 1. Motivação

Este trabalho tem como objetivo investigar o impacto das mudanças climáticas nos
incêndiosflorestaisnaAustrália.Apósaanálisedosdadoséesperadoquetrêsprincipais
perguntas sejam respondidas, sendo elas: 1. Existe correlação entre o aumento da
temperatura eaquantidade defocosdeincêndio?2.Épossívelpreveraquantidadede
focosdeincêndioemumdadomês/anobaseando-seemsuavariaçãodetemperatura?3.
Como as condições climáticas locais podem afetar umfoco de incêndio?
Com as respostas para essas perguntas é possível não só tomar decisões melhor
fundamentadas paraa criaçãode políticasclimáticas, mastambémorganizarrespostas
maisrápidasaosfocosdeincêndioecriarplanosdeprevençãoparaáreasconsideradasde
risco.

## 2. Dados

Nesta seção será abordado quais dados serão utilizadospara a análise, bem como suas
origens e estruturas.

### 2.1. Datasets

Osdadosutilizadosnestetrabalhosãoorigináriosdequatrodiferentesfontes,quaissejam:
MODIS da NASA,Australian Bureau of Meteorology, FAOeSimple Maps.


Osdados referentesafocosdeincêndioeanomaliastérmicassãogeradospelosatélite
MODISda NASA e o dataset completo está disponívelatravés destelink.
Osdados referentesa condiçõesclimáticasporcidadeforamgeradospeloEscritóriode
Meteorologia da Austrália (Australian Bureau of Meteorology)e podem ser acessadosaqui.
Dados referentes a variações climáticas por ano são dados distribuídos pela FAO e
coletados pelaNASA-GISSe podem ser acessadosaqui.
Porfim,osdadosreferentesacoordenadasgeográficasdecadacidadesãooriginadosdo
datasetSimple MapsAustrália.
Alémdoslinkscontidosacimaépossívelacessartodososdatasetsutilizadosnaíntegra
através dorepositóriodo trabalho.
Ao finaldo documentoestarápresenteuma relaçãode todososatributosdosdatasets
utilizados, seus significados e quais deles foramescolhidos para serem utilizados.

#### 2.1.1. Anomalias Térmicas

Odatasetde anomaliastérmicasécompostode leituras dosatélitemodis de 2000 até
2019, com os campos latitude,longitude, brightness, scan, track, acq_date, acq_time,
satellite,instrument,confidence,version,bright_t31,frp,day/nightetype.Aotodo,odataset
tem 5.081.221 de medições ao longo de 20 anos.
Paraestetrabalho,contudo,serãousadosapenasdadosde 2008 até2017,umavezque
esseéoperíododetempodeintercessãoentretodososdadosutilizados.Tambémnão
serão utilizadostodos os campos presentesno dataset,masseconsiderará alatitude,
longitude,brightness,acq_date,confidenceeday/night,camposqueforamjulgadosmais
importantes por conterem informações únicas e úteisaos propósitos deste estudo.
Foicriadaumageofenceparadelimitarumaáreadeestudo.Paraotrabalhoapenasaárea
entre as latitudes -27.38646 e -43.67288 e as longitudes 153.48215 e 140.48572 foi
considerada,umavezqueénessaáreaqueseconcentraamaioriadascidadespresentes
do datasetdedadosmeteorológicos.Apósadelimitaçãodaárea,aproximadamentedois
milhões de leituras serão consideradas para o trabalho.

#### 2.1.2. Dados Meteorológicos

Odataset,contendoosdadosmeteorológicos,teminformaçõesde 2008 atéametadede
2017, com os campos Date, Location, Min Temp, Max Temp, Rainfall, Evaporation,
Sunshine,WindGustDir,WindGustSpeed,WindSor9am,WindDir3pm,WindSpeed9am,
WindSpeed3pm,Humidity9am,Humidity3pm,Pressure9am,Pressure3pm,Cloud9am,
Cloud 3pm, Temp9am, Temp3pm, RainToday,RainTomorrowe umtotalde 145.
mediçõesde 49 locaisdiferentes.Paraestetrabalhoserãousadoscamposdate,location,
min Temp, max Temp, rainfall, wind Gust Dir, windGust Speed e as leituras de 31 cidades.
Os cortes nos campos foram realizados em função da redundância de dados e
inconsistêncianamediçãodealgunscampos,comoevaporationesunshine.Alémdisso,
Rain Today e Rain Tomorrow foram retirados, uma vezque fogem ao escopo do trabalho.
Também, 18 cidadesforamcortadasparaotrabalho,umavezqueseencontravammuito
distantes das outrascidades. Apósoscortes,serãoutilizadasaproximadamente 85 mil
medições.

#### 2.1.3. Variação de Temperatura

O dataset contendo a variação de temperatura contém dados sobre mudança de
temperaturaedesviopadrãomensal,sazonaleanualde 1961 até2019,paraaAustrália
como um todo. Como falado anteriormente, apenas dados de 2008 até 2017 serão
utilizadosnotrabalho.OscamposAreaCode,MonthsCode,ElementCodeeUnitforam
cortados pela sua insignificância para o projeto. Após asdelimitações, obtém-se 350
medições a serem consideradas.


#### 2.1.4. Cidades

Como as medições de satélite têm sua localização marcada como coordenadas
geográficas,easmediçõesmeteorológicasusamonomedacidadeparaseridentificadasé
necessárioestabelecerumeloentreosdoisdataset.Odatasetdecidadesfazexatamente
isso, elecontémonomeda cidadee ascoordenadasgeográficasreferentes aela.As
cidades utilizadas estão distribuídas da seguintemaneira:

Nas fotos, ascidades representadas por roxo estãolocalizadas na regiãode Austrália
meridional. As cidades representadas emvermelhoestãolocalizadas na região de Vitória.
As cidades representadas por laranjaescuro sãodaregiãode NovaGalesdoSul.As
cidades em laranja claropertencem àregiãodeQueensland epor fim,ascidadesem
amarelose encontram na Tasmânia.

### 2.2 Data Warehouse

Para apresentar o Data Warehouse vamos, primeiramente,trazer a modelagem do mesmo

#### 2.2.1 Modelagem

#### 2.2.2 Tabelas Fato

A modelagem inclui as seguintes tabelas fato:
● Weather, com as informações de temperatura mínima, temperatura máxima,
precipitação, direção do vento e velocidade do ventocomo fatos.
● Fires, comasinformaçõesdebrilho,confiança,dia/noite,latitudeexata,longitude
exata como fatos.
● WeatherVariation,comasinformaçõesdemudançadetemperaturaedesviopadrão
como fatos.


#### 2.2.3 Dimensões

O data warehouse conta comasdimensõesdo _tempo_ , representadoporData, eado
_espaço_ , representado por Localização.

AdimensãoDatatemcomoatributosdia,mês,anoeestação,queérepresentadaporum
inteiroseguindoaordemdasestaçõesnohemisfériosul,sendoelas:1-Verão,2-Outono,
3-Invernoe4-Primavera.Éimportanteressaltarqueoverãodeumanocomeçasempreno
mêsdedezembrodoanoanterior,porissojaneirode 2017 edezembrode 2016 sãoparte
do mesmo verão.

A dimensão Localização é representada por cidade eas suas coordenadas geográficas.
Natabela fatoFires tambémestãopresentes coordenadasgeográficas,masessassão
referentes ao foco em si, e não à cidade a qual ofoco pertence.

## 3. Cronograma

Cronograma de entregas parciais.

```
Data Atividades
21/05 Implementação do DWInício do processo de extração de padrões
28/05 Resultados parciais do processo de extração de padrões
04/06 Resultados parciais do processo de extração de padrões
11/
Resultados finais do processo de extração de padrões
Início do Pós-Processamento
18/06 Resultados parciais do pós-processamento
25/06 Resultados finais do pós-processamento
28/
Conclusão do estudo
Entrega do relatório final
```
## 4. Informações Adicionais

Essa seção contém informações adicionais sobre o trabalho.

### 4.1 Descrição dos campos dos datasets utilizados

Aseguirserãodetalhadostodososcamposdosdatasetsutilizadoscomseusrespectivos
significados.

#### 4.1.1 Anomalias Térmicas

```
● latitude:Centerof1kmfirepixelbut
notnecessarilytheactuallocationof
thefireasoneormorefirescanbe
detected within the 1km pixel.
● longitude: Centerof1kmfirepixel
but not necessarily the actual
locationofthefireasoneormore
firescanbedetectedwithinthe1km
pixel.
● brightness: Brightnesstemperature
21 (Kelvin): Channel 21/
```
```
brightness temperature of the fire
pixel measured in Kelvin.
● scan: Along Scan pixel size: The
algorithm produces 1km firepixels
butMODISpixelsgetbiggertoward
theedge ofscan. Scan and track
reflect actual pixel size.
● track: Along Track pixelsize: The
algorithm produces 1km firepixels
butMODISpixelsgetbiggertoward
```

```
the edge ofscan. Scan and track
reflect actual pixel size.
● acq_date: Date of MODIS
acquisition.
● acq_time: Time of
acquisition/overpass of thesatellite
(in UTC).
```
#### ● satellite:A = Aqua and T = Terra.

#### ● instrument: Constant value for

##### MODIS.

#### ● confidence:Thisvalueisbasedon

```
acollectionofintermediatealgorithm
quantities used in the detection
process.Itisintendedtohelpusers
gauge the quality of individual
hotspot/fire pixels. Confidence
estimates range between 0 and
100%andareassignedoneofthe
three fire classes (low-confidence
fire, nominal-confidence fire, or
high-confidence fire).
```
#### ● version:Version identifies the

```
collection(e.g.MODISCollection6)
andsourceofdataprocessing:Near
Real-Time (NRT suffix added to
collection) or Standard Processing
(collection only). "6.0NRT" -
Collection 6 NRTprocessing."6.0"-
Collection 6 Standard processing.
Findoutmoreoncollectionsandon
thedifferencesbetweenFIRMSdata
sourced from LANCE FIRMS and
University of Maryland.
```
#### ● bright_t31:Channel 31 brightness

```
temperature of the fire pixel
measured in Kelvin.
```
#### ● frp:Depictsthepixel-integratedfire

```
radiative power in MW (megawatts).
```
#### ● daynight:Day/Night:D=Daytime,

```
N = Nighttime.
```
#### ● type: No info

#### 4.1.2 Dados Meteorológicos

```
● Date: The date of observation.
● Location: The common name of
the location of the weather station.
● MinTemp: The minimum
temperature in degrees celsius.
● MaxTemp: The maximum
temperature in degrees celsius.
● Rainfall: The amount of rainfall
recorded for the day in mm.
● Evaporation:Theso-calledClassA
pan evaporation (mm) in the 24
hours to 9am.
● Sunshine:Thenumberofhoursof
bright sunshine in the day.
● WindGustDir: The direction of the
strongestwindgustinthe 24 hours
to midnight.
● WindGustSpeed: Thespeed(km/h)
ofthestrongestwindgustinthe 24
hours to midnight.
● WindDir9am:Directionofthewindat
9am.
● WindDir3pm:Directionofthewindat
3pm.
```
```
● WindSpeed9am: Wind speed
(km/hr) averaged over 10 minutes
prior to 9am.
● WindSpeed3pm: Wind speed
(km/hr) averaged over 10 minutes
prior to 3pm.
● Humidity9am:Humidity(percent)at
9am.
● Humidity3pm:Humidity(percent)at
3pm.
● Pressure9am:Atmosphericpressure
(hpa)reducedtomeansealevelat
9am.
● Pressure3pm:Atmosphericpressure
(hpa)reducedtomeansealevelat
3pm.
● Cloud9am:Fractionofskyobscured
bycloudat9am.Thisismeasuredin
"oktas'',whichareaunitofeighths.
Itrecordshowmanyeighthsofthe
sky are obscured by clouds. A 0
measure indicates a completely
clearskywhilstan 8 indicatesthatit
is completely overcast.
● Cloud3pm:Fractionofskyobscured
bycloud(in“oktas”:eighths)at3pm.
```

```
See Cload9amfor adescriptionof
the values.
● Temp9am:Temperature(degreesC)
at 9am.
● Temp3pm:Temperature(degreesC)
at 3pm.
```
```
● RainToday: Boolean: 1 if
precipitation(mm)inthe 24 hoursto
9am exceeds 1mm, otherwise 0.
● RainTomorrow:Theamountofnext
day rainin mm. Used tocreatea
responsevariableRainTomorrow.A
kind of measure of the "risk".
```
#### 3.2.3 Variação de Temperatura

```
● AreaCode:Thenumericalcodeof
areacolumn,typeofareacodeis
an integer.
● Area: CountriesandTerritories(In
2019: 190 countriesand 37 other
territorialentities.),typeofareais
an object.
● MonthsCode:Thenumericalcode
ofmonthscolumn,typeofmonths
code is an integer.
● Months: Months, Seasons,
Meteorological year, type of
months is an object.
```
```
● Element Code: The numerical
code of element column, type of
element code is an integer.
● Element: 'Temperature change',
'Standard Deviation', type of
element is an object.
● Unit:Celsius degrees°C,typeof
unit is an object.
● Y1961-2019: Year
```
#### 3.2.4 Cidades

```
● cit: City name.
● lat: Latitude.
● lng: Longitude.
● country: City’s country.
● iso2: Country’s name abbreviation.
● admin_name:City’sadministrative
name.
```
```
● capital: Boolean: Admin or not.
● population: Population number.
● population_proper: Population
number.
```


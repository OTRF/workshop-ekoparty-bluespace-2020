# Análisis de Datos con Pandas - Transformando Datos

* **Autor**: Jose Rodriguez (@Cyb3rPandah)
* **Proyecto**: Infosec Jupyter Book
* **Organización Pública**: [Open Threat Research](https://github.com/OTRF)
* **Licencia**: [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/)
* **Referencia**: https://github.com/OTRF/mordor/tree/master/datasets/large/apt29/day1

## Representando el Archivo JSON como Dataframe usando Pandas

La representación del archivo JSON como un Dataframe de Pandas puede involucrar el uso de comandos como **wget**, **unzip**. Esto fue explicado con más detalle en el notebook que lleva por título **Representando el Archivo JSON como Dataframe usando Pandas**, y además se encuentra en la misma carpeta del presente notebook. Para mantener la estructura del presente notebok en un formato simple, los JSON files requeridos para este workshop ya han sido desargados y descomprimidos. Estos archivos se encuentran en la carpeta **sets_datos**.

! wget https://github.com/OTRF/mordor/raw/master/datasets/large/apt29/day1/apt29_evals_day1_manual.zip  -O sets_datos/apt29_evals_day1_manual.zip

! unzip -o sets_datos/apt29_evals_day1_manual.zip -d sets_datos/

apt29_json = 'sets_datos/apt29_evals_day1_manual_2020-05-01225525.json'

### a) Importando la librería Pandas

import pandas as pd

### b) Leyendo Archivo JSON

Usaremos el método **pandas.read_json**.

Referencia: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html

# reading the json file using read_json method and considering the parameter lines = True
# setting the chunksize parameter = 1000
df = pd.read_json(apt29_json, lines = True, chunksize = 1000)
# creating an empty list to store data for every chunk
apt29_chunks = []
# adding data of every chunk to an empty list using a for loop and the append method
for chunk in df:
    apt29_chunks.append(chunk)
# putting everything together into a Pandas dataframe using the concat method
# considering the parameter sort = False
df = pd.concat(apt29_chunks, sort = False)
# visualizing the first five records of the Pandas dataframe using the head method
df.head()

### c) Conociendo las columnas o atributos del Dataframe

Usaremos el método **pandas.DataFrame.info**.

Referencia: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.info.html

df.info(verbose = True)

## Filtrando Eventos de Seguridad: Sysmon 1 (Creacion de Processo)

Vamos a usar el mismo codigo del notebok anterior, pero con una pequeña modificación. En vez de buscar el nombre del channel completo, buscaremos la palabra **sysmon**.

Referencias:
* https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.contains.html
* https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.startswith.html
* https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.endswith.html

(
df[['@timestamp','Image','CommandLine']]
    
[(df['EventID'] == 1) & (df['Channel'].str.contains('sysmon',case = False, na = False, regex = False)) ]
    
.head(5)
)

## Calculando la Longitud del CommandLine

Usaremos el método **assign** para agregar una columna nueva a nuestro dataframe. Esta nueva columna mostrará el calculo de la longitud del command line que el processo utilizó.

Referencia: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.assign.html

(
df[['@timestamp','Image','CommandLine']]
    
[(df['EventID'] == 1) & (df['Channel'].str.contains('sysmon',case = False, na = False, regex = False))]
    
.assign(Command_Length = df['CommandLine'].str.len())
)

## Muchas gracias!! Espero que este notebooks haya sido útil para empezar a revisar algunas técnicas para transformar datos :D

## Aún hay más por aprender :D
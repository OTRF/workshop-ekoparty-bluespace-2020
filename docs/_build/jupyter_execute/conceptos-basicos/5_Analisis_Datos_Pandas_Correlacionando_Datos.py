# Análisis de Datos con Pandas - Correlacionando Datos

* **Autor**: Jose Rodriguez (@Cyb3rPandah)
* **Proyecto**: Infosec Jupyter Book
* **Organización Pública**: [Open Threat Research](https://github.com/OTRF)
* **Licencia**: [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/)
* **Referencia**: https://mordordatasets.com/notebooks/small/windows/08_lateral_movement/SDWIN-190518210652.html

## Representando el Archivo JSON como Dataframe usando Pandas

La representación del archivo JSON como un Dataframe de Pandas puede involucrar el uso de comandos como **wget**, **unzip**. Esto fue explicado con más detalle en el notebook que lleva por título **Representando el Archivo JSON como Dataframe usando Pandas**, y además se encuentra en la misma carpeta del presente notebook. Para mantener la estructura del presente notebok en un formato simple, los JSON files requeridos para este workshop ya han sido desargados y descomprimidos. Estos archivos se encuentran en la carpeta **sets_datos**.

psexec_json = 'sets_datos/empire_psexec_dcerpc_tcp_svcctl_2020-09-20121608.json'

### a) Importando la librería Pandas

import pandas as pd

### b) Leyendo Archivo JSON

Usaremos el método **pandas.read_json**.

Referencia: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html

df = pd.read_json(path_or_buf = psexec_json, lines = True)
df.head(5)

### c) Conociendo las columnas o atributos del Dataframe

Usaremos el método **pandas.DataFrame.info**.

Referencia: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.info.html

df.info(verbose = True)

## Filtrando Columnas o Atributos de nuestro Dataframe

Seleccionando las columnas **'@timestamp','Hostname','Channel','EventID'** usando una **lista** con los nombres de las columnas.

df[['@timestamp','Hostname','Channel','ParentImage','Image','EventID']].head()

## Preparando Dataframes para un JOIN

### a)  QUE EVENTO NOS PODRIA AYUDAR A VER NUEVOS SERVICIOS INSTALLADOS EN UN SISTEMA? 





### b) QUE EVENTO NOS PODRIA AYUDA A IDENTIFICAR USUARIOS AUTHENTICATING REMOTAMENTE? HINT: LOGON TYPE 3 ;)



## JOINing Nuevos Servicios Installados con usuarios authenticating remotemente

### COMO PODEMOS UNIR ESTOS DOS EVENTOS?

(
pd.merge(Security4697, Security4624[Security4624['LogonType'] == 3],
         left_on = 'SubjectLogonId', right_on = 'TargetLogonId', how = 'inner')
[['ServiceName', 'ServiceFileName','IpAddress']]
)

## Muchas gracias!! Espero que este notebooks haya sido útil para empezar a revisar algunas técnicas para correlationar datos :D

## Aún hay más por aprender :D
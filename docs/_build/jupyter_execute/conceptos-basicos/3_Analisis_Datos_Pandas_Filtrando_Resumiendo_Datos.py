# Análisis de Datos con Pandas - Filtrando y Resumiendo Datos

* **Autor**: Jose Rodriguez (@Cyb3rPandah)
* **Proyecto**: Infosec Jupyter Book
* **Organización Pública**: [Open Threat Research](https://github.com/OTRF)
* **Licencia**: [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/)
* **Referencia**: https://mordordatasets.com/notebooks/small/windows/02_execution/SDWIN-200806115603.html

## Representando el Archivo JSON como Dataframe usando Pandas

La representación del archivo JSON como un Dataframe de Pandas puede involucrar el uso de comandos como **wget**, **unzip**. Esto fue explicado con más detalle en el notebook que lleva por título **Representando el Archivo JSON como Dataframe usando Pandas**, y además se encuentra en la misma carpeta del presente notebook. Para mantener la estructura del presente notebok en un formato simple, los JSON files requeridos para este workshop ya han sido desargados y descomprimidos. Estos archivos se encuentran en la carpeta **sets_datos**.

psremoting_json = 'sets_datos/covenant_psremoting_command_2020-08-06115603.json'

### a) Importando la librería Pandas

import pandas as pd

### b) Leyendo Archivo JSON

Usaremos el método **pandas.read_json**.

Referencia: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html

df = pd.read_json(path_or_buf = psremoting_json, lines = True)
df.head(5)

### c) Conociendo las columnas o atributos del Dataframe

Usaremos el método **pandas.DataFrame.info**.

Referencia: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.info.html

df.info(verbose = True)

## Filtrando Columnas o Atributos de nuestro Dataframe

Seleccionando las columnas **'@timestamp','Hostname','Channel','EventID'** usando una **lista** con los nombres de las columnas.

df[['@timestamp','Hostname','Channel','ParentImage','Image','EventID']].head()

## Filtrando Filas o Registros de nuestro Dataframe

### a) Una condición

Filtrando nombres de procesos que incluyan el string **wsmprovhost.exe**.

(
df[['@timestamp','Hostname','Channel','ParentImage','Image','EventID']]
    
[df['Image'].str.contains('wsmprovhost.exe',case = False, na = False, regex = False)]
    
.head(5)
)

### b) Más de una condición: Operadores AND y OR

Podemos usar múltiples condiciones usando los operadores **&** (AND) y **|** (OR). El uso de parentesis es importante cuando trabajamos con múltiples condiciones.

(
df[['@timestamp','Hostname','Channel','ParentImage','Image','EventID']]
    
[(df['Image'].str.contains('wsmprovhost.exe',case = False, na = False, regex = False)) |
  (df['ParentImage'].str.contains('wsmprovhost.exe',case = False, na = False, regex = False))]    

.head(5)
)

## Resumiendo Filas o Registros de nuestro Dataframe

### a) Resumiendo los eventos de seguridad para el proveedor Sysmon

Ahora podemos realizar la agrupación del dataframe anterior usando el método **groupby** y la columna que representa el número de identificaión del evento de seguridad.

Referencia: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html

(
df[['@timestamp','Hostname','Channel','ParentImage','Image','EventID']]
    
[(df['Image'].str.contains('wsmprovhost.exe',case = False, na = False, regex = False)) |
  (df['ParentImage'].str.contains('wsmprovhost.exe',case = False, na = False, regex = False))]    

.groupby(['EventID']).size()
)

El código ejecutado previamente nos devuelve una **Serie**. En caso quisieramos convertir este objeto a un **dataframe**, podemos usar el método **to_frame**.

Referencia: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.to_frame.html

(
df[['@timestamp','Hostname','Channel','ParentImage','Image','EventID']]
    
[(df['Image'].str.contains('wsmprovhost.exe',case = False, na = False, regex = False)) |
  (df['ParentImage'].str.contains('wsmprovhost.exe',case = False, na = False, regex = False))]    

.groupby(['EventID']).size().to_frame(name = 'Frequencia')
)

### b)  Resumiendo y Ordenando los eventos de seguridad para el proveedor Sysmon

Similar al codigo anterior, pero ahora vamos a agregar la operacion de ordenamiento usando el método **sort_values**.

Referencia: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html

(
df[['@timestamp','Hostname','Channel','ParentImage','Image','EventID']]
    
[(df['Image'].str.contains('wsmprovhost.exe',case = False, na = False, regex = False)) |
  (df['ParentImage'].str.contains('wsmprovhost.exe',case = False, na = False, regex = False))]    

.groupby(['EventID']).size().to_frame(name = 'Frequencia').sort_values(by = 'Frequencia', ascending = False)
)

## Muchas gracias!! Espero que este notebooks haya sido útil para empezar a revisar algunas técnicas para filtrar y resumir datos :D

## Aún hay más por aprender :D


# Creando un Dataframe desde un Set de Datos de Mordor

* **Autor**: Jose Rodriguez (@Cyb3rPandah)
* **Proyecto**: Infosec Jupyter Book
* **Organización Pública**: [Open Threat Research](https://github.com/OTRF)
* **Licencia**: [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/)
* **Referencia**: https://mordordatasets.com/notebooks/small/windows/02_execution/SDWIN-200806115603.html

## Obteniendo el archivo JSON

### a) Descargando el archivo Zip

Usaremos el comando **wget** y la opción **-O** (output document file) para guardar el archivo Zip en la carpeta **sets_datos**.

! wget https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/host/covenant_psremoting_command.zip -O sets_datos/covenant_psremoting_command.zip

### b) Extrayendo el archivo JSON

Usaremos el comando **unzip** y las opciones **-o** (Overwrite) y **-d** (different directory) para guardar el archivo JSON en la carpeta **sets_datos**.

! unzip -o sets_datos/covenant_psremoting_command.zip -d sets_datos/

Para facilitar nuestro código, almacenaremos el **directorio** del archivo JSON en una variable.

psremoting_json = 'sets_datos/covenant_psremoting_command_2020-08-06115603.json'

## Representando el Archivo JSON como Dataframe usando Pandas

### a) Importando la librería Pandas

import pandas as pd

### b) Leyendo el archivo JSON

Usaremos el método **pandas.read_json**.

Referencia: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html

df = pd.read_json(path_or_buf = psremoting_json, lines = True)

Validaremos el tipo de objecto creado usando la funcion **type**, la cual es proveida por Python (Built-In).

Referencia: https://docs.python.org/3/library/functions.html

type(df)

Finalmente, podemos visualizar el **dataframe** generado:

df

### c) Conociendo las columnas o atributos del Dataframe

Usaremos el método **pandas.DataFrame.info**.

Referencia: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.info.html

df.info(verbose = True)

## Muchas gracias!! Espero que este notebooks haya sido útil para empezar a importar sets de datos de mordor

## Aún hay más por aprender :D


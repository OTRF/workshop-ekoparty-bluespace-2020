# Introducción a NumPy Arrays
* **Autor:** Jose Rodriguez (@Cyb3rPandah)
* **Proyecto:** Infosec Jupyter Book
* **Organización Pública:** Open Threat Research
* **Licencia:** Creative Commons Attribution-ShareAlike 4.0 International

**Referencias:**
* http://www.numpy.org/
* https://docs.scipy.org/doc/numpy/user/quickstart.html
* https://www.datacamp.com/community/tutorials/python-numpy-tutorial
* https://blog.thedataincubator.com/2018/02/numpy-and-pandas/
* https://medium.com/@ericvanrees/pandas-series-objects-and-numpy-arrays-15dfe05919d7
* https://www.machinelearningplus.com/python/numpy-tutorial-part1-array-python-examples/
* https://towardsdatascience.com/a-hitchhiker-guide-to-python-numpy-arrays-9358de570121
* McKinney, Wes. Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython. O'Reilly Media. Kindle Edition

## Arrays

import array

array_one = array.array('i',[1,2,3,4])
type(array_one)

type(array_one[0])

## NumPy N-Dimensional Array (ndarray)

import numpy as np
np.__version__

list_one = [1,2,3,4,5]

numpy_array = np.array(list_one)
type(numpy_array)

numpy_array

## Ventajas de los NumPy Arrays

### Operaciones Vectoriales

list_two = [1,2,3,4,5]
# The following will throw an error:
list_two + 2

* Ejecutando un Python FOR loop para agregar **2** a cada numero entero en la lista

for index, item in enumerate(list_two):
    list_two[index] = item + 2
list_two

* Con NumPy array, es tan simple como:

numpy_array

numpy_array + 2

* Cualquier operación aritmetica entre dos arrays de el mismo tamaño, es aplicada a todos los elementos de los arrays:

numpy_array_one = np.array([1,2])
numpy_array_two = np.array([4,6])

numpy_array_one + numpy_array_two

numpy_array_one > numpy_array_two


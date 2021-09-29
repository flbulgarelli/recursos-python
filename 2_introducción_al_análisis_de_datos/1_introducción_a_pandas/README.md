# Introducción a los Datasets con Pandas

A continuación, vamos a aprender sobre qué es un dataset (es decir, un conjunto o lote de datos), cómo se estructura y cómo se puede procesar utilizando algunas herramientas y tecnologías de ciencia de datos


https://colab.research.google.com/drive/1DXhu0bNiy7U5qayoC4icGPNd3rST49OH#scrollTo=kDEWWrePOMiX
https://colab.research.google.com/drive/1q1qvfikU1QPARm_fSdJrSQ9qHCVFDBRD#scrollTo=HYwrSLUnqf65

# La biblioteca de Babel

conjunto de funciones, procedimientos
# tipos de datos y otras yerbas)

# Comerciando código

# sentencia import
# se lee como "andá a buscar la biblioteca pandas y nombrala como pd"
import pandas as pd

# ¿Cesequé?

Vamos a trabajar con archivos CSV, que es un acrónimo de Comma Separated Value, es decir, un archivo con valores separados por comas.

Por ejemplo:

```
nombre,apellido,edad
Feli,Perez,24
Dani,Lopez,32
Juani,Vazquez,13
```

## A cargar, a cargar, cada tabla en su lugar

El primer paso es **cargar** la _biblioteca_ `pandas`, una herramienta poderosa para el lenguaje Python, que posibilita manipular datos de un lote de forma programática. En otras palabaras, va a permitirnos hacer las mismas operaciones que haríamos en una hoja de cálculos, pero utilizando código.

## Quien busca, encuentra

El siguiente paso es conseguir un lote y cargarlo dentro de Jupyter (es decir, esta aplicación) en la forma de un `DataFrame` llamado `bibliotecas`

# Tablas y columnas


Momento... ¿lo qué? ¿Un `DataFrame`?  ¿Qué es eso?

Hasta ahora veníamos trabajando con cosas como números (por ejemplo, el `1`, el `42` y el `30410`) y booleanos (`True` o `False`); pero eso es muy limitado. Por eso vamos a usar ahora un nuevo tipo de dato llamado `DataFrame`, que es el tipo de la variable `bibliotecas`:

# a lo que llamos tabla, pandas lo llama DataFrame
# a lo que llamamos columna, pandas lo llama Series


# Series vs DataFrames

Hay funciones y procedimientos que funcionan tanto con los DataFrames como con los Series.

Pero, al ser distintas sus estructuras, ya que el primero es una tabla con muchas columnas, mientras que el Series es básicamente una única columna, los parámetros variarán.


# El DataFrame también lo puedo ordenar, pero al tener muchas columnas, tengo que indicar por cuál/es criterios hacerlo.
# No puede ordenar por TODAS las columnas a la vez.

bibliotecas.sort_values("calle", ascending = False)

# sort_values es casi igual que antes, pero con un argumento indicando la columna a utilizar para ordenar.


# Lo mismo ocurre con los gráficos, donde tengo múltiples variables para elegir y graficar.
# Agregamos entonces las columnas deseadas, indicando en qué eje estarán:

bibliotecas.plot.bar(x = "comuna", y = "codigo_postal")



Para una rápida visualización de los datos, tenemos algunas herramientas como:
* `columns`, que nos permite ver rápidamente los nombres de las columnas y darnos una idea de la información que contienen
* `head` y `tail` para tomar las primeras o las últimas n-filas, y chusmear la info en sí
* `sample` que también toma n-filas, pero de manera aleatoria. Conviene usarlo para no sesgarnos con la información, ya que las primeras n filas podrían compartir ciertas características que no contengan las siguientes o las últimas.


# Si bien vimos que value_counts era mucho más simple de usar que groupby, este último nos da más libertad para hacer otro tipo de operaciones.
# Por ejemplo, si luego de agrupar por cierto criterio quiero sumar los valores de una columna en vez de contarlos, aplicaré un sum()

codigos_postales_sumados = bibliotecas.groupby("comuna").sum().codigo_postal

# Ojo, porque count() no suele tener problemas; en definitiva, siempre podemos contar elementos sin importar qué contengan.
# No pasa lo mismo que sum(), que funcionará únicamente con cosas que se puedan sumar entre sí.


Por otra parte, es un poco tedioso agregar `sort_values(ascending = False)` cada vez que quiera ordenarlo de manera descendente. Así que podemos definir una función que, al invocarla, resuelva esta parte.

Lo importante es:
* no repetir código innecesariamente (nos daremos cuenta tras copiar y pegar lo mismo 2 ó 3 veces)
* reutilizar para simplificarnos la vida (nos ahorramos el problema de buscar el código que resuelva exactamente eso, y lo abstraemos en una función cuyo nombre será más fácil de recordar).


def ordenar_descendente(series_a_ordenar):
  return series_a_ordenar.sort_values(ascending = False)

# Ojo, como ya vimos, sort_values no es igual en DataFrames que en Series. Así como está definido acá, funciona con Series.

### Otra forma de responderlo: gráfica

Podemos hacer un gráfico de barras con el resultado de un `value_counts` usando `plot.bar` de la siguiente manera:

```python
dataframe.plot.bar(figsize=(tamanio_x_en_pulgadas, tamanio_y_en_pulgadas))
```
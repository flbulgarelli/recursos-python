Guía Rápida Pandas
==================

# Lectura

## `read_csv`

Nos permite leer un archivo [CSV](https://es.wikipedia.org/wiki/Valores_separados_por_comas) a partir de una URL (es decir, de la dirección donde se encuentra el archivo). Ejemplo:

```python
>>> pd.read_csv("http://cdn.buenosaires.gob.ar/datosabiertos/datasets/arbolado-publico-lineal/arbolado-publico-lineal.csv")
          long       |	lat        |	id_arbol  |	altura_tot |	diametro |	inclinacio | nombre_com
0      |	-58.389059 |	-34.620026 |	2430      |	7  |	20 |	17  |	Fresno americano
1      |	-58.389211 |	-34.620034 |	2431      |	8  |	33 |	16  |	Fresno americano
2      |	-58.389269 |	-34.620037 |	2432      |	2  |	3  |	0   |	Ligustro
3      |	-58.389525 |	-34.620052 |	2433      |	9  |	17 |	0   |	Arce negundo
4      |	-58.389608 |	-34.620057 |	2434      |	6  |	13 |	14  |	Fresno americano
...    |	...        |	...        |	...       |	.. |	.. |	... |	...
372694 |	-58.493294 |	-34.623746 |	938000239 |	10 |	52 |	5   |	Paraíso
372695 |	-58.493241 |	-34.623788 |	938000240 |	11 |	60 |	10  |	Paraíso
372696 |	-58.493176 |	-34.623840 |	938000241 |	10 |	56 |	20  |	Paraíso
372697 |	-58.493116 |	-34.623887 |	938000242 |	10 |	58 |	0   |	Paraíso
372698 |	-58.493086 |	-34.624042 |	938000243 |	3  |	5  |	0   |	Crespón (Àrbol de Júpiter)
```

Típicamente nos convendrá guardar este resultado en una variable para usarlo más tarde:

```python
>>> arbolado = pd.read_csv("http://cdn.buenosaires.gob.ar/datosabiertos/datasets/arbolado-publico-lineal/arbolado-publico-lineal.csv")
```

# Consulta

## `iloc`

Nos permite obtener una fila segun el índice. Ejemplo:

```python
# nos devuelve la fila cuyo índice es 15
arbolado.iloc[15]
```
:warning: obtener una fila por índice `n` no es necesariamente lo mismo que obtener la fila en la `n`-ésima posición. Ver manejo de índices.

## `head`

Nos permite obtener un nuevo `DataFrame` con únicamente las primeras `n` filas. Por ejmplo:

```python
# nos da los primeros 10 elementos
arbolado_valido.head(10)
```

:warning: Head no ordena al `DataFrame`, solo nos dan los primeros o últimos
en el orden en que estén, por tanto nos será útil ordenar previamente según algún criterio. Por ejemplo:

```python
arbolado.sort_values('diametro').tail(2)
```

## `tail`

Nos permite obtener un nuevo `DataFrame` con únicamente las últimas `n` filas. Por ejmplo:

```python
# nos da los últimos 10 elementos
arbolado.tail(10)
```

:warning: Tal como sucede con `head`, `tail` no ordena de ninguna forma al `DataFrame`.

# Acceso por columna

## `.`
## `[]`

# Recuento

## `len`

La función estándar `len`, de la misma forma que nos sirve para contar los elementos de una lista o los caracteres de una palabra, nos permite contar la cantidad de filas de un DataFrame. Ejemplo:

```python
>>> len(arbolado)
372699 # arbolado tiene 372699 filas
```

## `nunique`

Retorna la cantidad de valores únicos, excluyendo a los valores `NaN`:

```python
>>> arbolado.nombre_com.nunique()
305
```

Si la columna no contiene valores nulos, es lo mismo que hacer:

```python
>>> len(pd.unique(arbolado.nombre_com))
306
```

# Valores únicos

## `unique`

Nos permite obtener todos los valores de una columna, sin repetidos. Ejemplo:

```python
# retorna los nombres comunes únicos de los árboles
>>> pd.unique(arbolado.nombre_com)
[
  'Fresno americano', 'Ligustro', 'Arce negundo',
  'Ciruelo de jardín', 'Ficus', 'Tilo', 'Acacia blanca',
  'Pata de vaca  (Pezuña de vaca)', 'Mandarino',
  'Crespón (Àrbol de Júpiter)', 'Ceibo', 'No Determinable',
  'Liquidambar', 'Jacarandá', ... etc ...
]
```


# Caracterización

## `describe`

# Agregaciones

## `mean`
## `median`
## `quantile`
## `max` y `min`

Nos devuelven, respectivamente el valor más grande y más pequeño de la columna. Ejemplo:

```python
# altura máxima
arbolado.altura_tot.max()

# diametro mínimo
arbolado.diametro.min
```

## `idxmax` y `idxmin`

Nos permiten obtener el índice de la primera fila que hace máxima o mínima a la columna dada, respectivamente. Ejemplo:

```python
# el valor del índice de la fila con el máximo diámetro
arbolado.diametro.idxmax()
```

Como consecuencia de su definición, si obtenemos el valor de la columna para el índice obtenido, éste va a ser el máximo:

```python
# la siguiente expresión siempre va a ser verdadera:
arbolado.diametro.max() == arbolado.diametro.iloc[arbolado.diametro.idxmax()]
```

# Ordenamiento

## `sort_values`

# Transformaciones sobre strings

## `+`, `-`
## `str`
## `dt`

# Creación y actualización de columnas

# Filtrado

## `&`, `|` y `~`
## `isin`
## `isna`, `notna`


# Agrupamiento

## `groupby`

```
bibliotecas.groupby("barrio").count()
bibliotecas.groupby("barrio").biblioteca.count()
bibliotecas.groupby(bibliotecas.barrio).biblioteca.count()
bibliotecas.groupby(bibliotecas.barrio, as_index = False).biblioteca.count()
bibliotecas.groupby(bibliotecas.barrio, as_index = False).biblioteca.filter()
bibliotecas.groupby(bibliotecas.barrio, as_index = False).biblioteca.agg()
```

## `value_counts`

# Combinación

## `merge`
## `concat`

# Gráficos

## `plot.bar`

```
cantidad_de_bibliotecas_por_barrio.plot.bar(figsize=(20, 10))
```

## `plot.hist`
## `plot.line`
## `plot.scatter`
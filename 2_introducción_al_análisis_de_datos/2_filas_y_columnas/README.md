# Operaciones básicas

Ya sabemos qué es un lote de datos, un `DataFrame` y cómo podemos usar `pandas` para cargarlo con datos. ¡Descubramos entonces qué podemos hacer con los datos a partir de ahora!

¡Seguínos!

## 1. De flor en flor

Carguemos un luego lote de datos

## 2. Accediendo a las columnas

```python
# para obtener los valores de una columna,
# la sintaxis es tabla[nombre_de_columna]
florerias["TITULAR"]
```

## 3. La revancha de los últimos

de igual forma tenemos la función tail

columna.head()
florerias["TITULAR"].head(5)


ojo con esta función, que se escribe como
florerias["TITULAR"].tail(5)

## 4. Series vs DataFrames

```python
# a lo que llamos tabla, pandas lo llama DataFrame
# a lo que llamamos columna, pandas lo llama Series
```
Hay funciones y procedimientos que funcionan tanto con los DataFrames como con los Series.

Pero, al ser distintas sus estructuras, ya que el primero es una tabla con muchas columnas, mientras que el Series es básicamente una única columna, los parámetros variarán.


## 5. No tan único

```python
florerias["Calle"].unique()
```

## 6. Cuántos cuentan

```python
florerias["Calle"].value_counts()
```

## 7. También vale ordenar

Vuelta sobre el `sort_values`

## 8. Índices

No, ¡no es el índice de la lección!

```
# otro uso de corchetes:
# la función iloc se usa de la siguiente forma:
# tabla.iloc[indice]
# con iloc podemos obtener una fila en base a su número (índice) de fila
# OJO: el número o indice de fila no necesariamente coincide con la posición de la fila en la tabla
florerias.iloc[4]
```

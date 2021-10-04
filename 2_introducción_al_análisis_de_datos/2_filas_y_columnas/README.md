# Operaciones básicas

Ya sabemos qué es un lote de datos, un `DataFrame` y cómo podemos usar `pandas` para cargarlo con datos. ¡Descubramos entonces qué podemos hacer con los datos a partir de ahora!

¡Seguínos!

## 1. De flor en flor

Carguemos un luego lote de datos

```python
>>> florerias = pd.read_csv("https://cdn.buenosaires.gob.ar/datosabiertos/datasets/ministerio-de-espacio-publico-e-higiene-urbana/puestos-de-flores/puestos-flores.csv")
>>> florerias
```

## 2. Accediendo a las columnas

```python
# para obtener los valores de una columna,
# la sintaxis es tabla[nombre_de_columna]
>>> florerias["TITULAR"]
0             PEVES SALLY STEPHANIE
1               HEREDIA LUIS HECTOR
2               AYBAR MARIA SOLEDAD
3      REBASA OTINIANO SANTOS CLARA
4           SALAZAR ESCOBAR ROSENDA
                  ...
95      DE NICOLO CONO WALTER DARIO
96               SAGARDIA DESIDERIO
97           CONDOLUCI MARIA TERESA
98      MC INTYRE YOLANDA ELIZABETH
99    CORDERO EZEQUIEL MAXIMILIANO
Name: TITULAR, Length: 100, dtype: object
```

> ¡Ahora te toca a vos! Obtené las calles de las florerías

### Solución posible

<details>
<summary>👀 Ver</summary>

```python
>>> florerias["Calle"]
0                   FLORIDA
1     LACROZE, FEDERICO AV.
2               CABILDO AV.
3                   FLORIDA
4         MARTIN GARCIA AV.
              ...
95             EMILIO MITRE
96           AV. CORRIENTES
97      AV. GUZMAN PUESTO 7
98                JURAMENTO
99           C. PELLEGRINI
Name: Calle, Length: 100, dtype: object
```

</details>

## 3. La revancha de los últimos

ojo con esta función, que se escribe como
de igual forma tenemos la función tail

```python
>>> florerias["TITULAR"].head(5)
0           PEVES SALLY STEPHANIE
1             HEREDIA LUIS HECTOR
2             AYBAR MARIA SOLEDAD
3    REBASA OTINIANO SANTOS CLARA
4         SALAZAR ESCOBAR ROSENDA
Name: TITULAR, dtype: object
```

```python
>>> florerias["TITULAR"].tail(5)
95      DE NICOLO CONO WALTER DARIO
96               SAGARDIA DESIDERIO
97           CONDOLUCI MARIA TERESA
98      MC INTYRE YOLANDA ELIZABETH
99    CORDERO EZEQUIEL MAXIMILIANO
Name: TITULAR, dtype: object
```

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

```python
>>> len(florerias["Calle"].unique())
67
```

Como esta operación es tan común, contamos con un atajo: la función infija `nunique`:

```python
>>> florerias["Calle"].nunique()
67
```

## 6. Cuántos cuentan

```python
florerias["Calle"].value_counts()
```

## 7. También vale ordenar

Vuelta sobre el `sort_values`

## 8. Índices

No, ¡no es el índice de la lección!

```python
# otro uso de corchetes:
# la función iloc se usa de la siguiente forma:
# tabla.iloc[indice]
# con iloc podemos obtener una fila en base a su número (índice) de fila
# OJO: el número o indice de fila no necesariamente coincide con la posición de la fila en la tabla
florerias.iloc[4]
```

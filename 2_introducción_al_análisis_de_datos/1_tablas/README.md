# Introducción a pandas

_¡Qué queremos? ¡Trabajar con datos! ¿Y dónde los vamos a buscar? Eh... en un... ¿conjunto de datos?🤔_

Cuando queramos analizar datos, con mucha frecuencia los encontraremos en archivos llamados (no muy originalmente 😛) _lotes de datos_ (_datasets_, en inglés). ¿Pero cómo se ven estos lotes? ¿Dónde los podemos encontrar publicados? ¿Cómo los podemos procesar?

¡Muchas preguntas! En esta lección responderemos alguans de ellas. Y en el camino, conoceremos a `pandas` 🐼, una biblioteca que poco tiene con los simpáticos osos oriundos de las regiones montañosas de China 🇨🇳, pero que nos ayudará enormemente a trabajar con estos lotes de datos.

¡Empecemos!

## 1. Abierto al público

Primero lo primero: entendamos dónde encontrar nuestros tan deseados lotes de datos. O mejor dicho, entendamos que _no siempre_ podremos encontrarlos 😓. Esto se debe a las organizaciones que los recopilan (estados, empresas, ONGs, etc) a veces los _publican_ y otras veces, no.

Por eso es que tenemos dos grandes familias de lotes de datos:

 * 🔓 Los datos abiertos: pueden ser consultados por cualquier persona y usados para casi cualquier fin.
 * 🔒 Los datos cerrados: sólo los pueden consultar personas que pertenezcan a las organizaciones que los producen, o personas externas pero con fuertes limitaciones en su acceso y uso (por ejemplo, a través de un pago)

> 🏅 Desafío: las siguientes son páginas de estados que ofrecen datos abiertos. Exploralas e identificá qué tipo de información publican y **en qué formatos**.
>
> * 🇦🇷 https://www.datos.gob.ar/
> * 🇺🇾 https://www.gub.uy/datos-abiertos
> * 🇲🇽 https://datos.gob.mx/
> * 🇨🇱 https://datos.gob.cl/

## 2. Manteniendo las formas

Si exploraste las páginas anteriores, quizás hayas notado que casi todos los lotes de datos están publicados en forma de tablas. Y dentro de tooodos los formatos que existen, uno de los más frecuentes (y fáciles de usuar) se llama CSV.

Momento, ¿cesequé? ¡Ce-ese-vé! Se trata de un acrónimo en inglés de _Comma Separated Value_, es decir, un archivo de texto con valores separados por comas. Por ejemplo así se ve un archivo `datos_ejemplo.csv`:

```csv
Feli,Perez,24
Dani,Lopez,32
Juani,Vazquez,19
```

> Para pensar 🤔: ¿qué está intentando representar este CSV de ejemplo? ¿Qué información contiene cada renglón?

## 3. Sin título

El archivo CSV que vimos antes contenía información de personas, o al menos eso parece. Quizás se traten de sus nombres, apellidos y sus edades, o quizás sean estudiantes de una carrera y nos esté informando la cantidad de materias aprobadas.

Para evitar este tipo de ambigüedad, normalmente los archivos CSV contendrán en su primer renglón los títulos de cada columna. Por ejemplo así podría verse ahora nuestro `datos_ejemplo.csv`:

```csv
nombre,apellido,edad
Feli,Perez,24
Dani,Lopez,32
Juani,Vazquez,19
```


> Para pensar 🤔: Y si ahora quisieras agregar la información de cuál es su gusto de helado favorito, ¿cómo harías?

## 4. Comerciando código


conjunto de funciones, procedimientos tipos de datos y otras yerbas)

```python
# sentencia import
# se lee como "andá a buscar la biblioteca pandas y nombrala como pd"
import pandas as pd
```

## 5. A cargar, a cargar, cada tabla en su lugar

El primer paso es **cargar** la _biblioteca_ `pandas`, una herramienta poderosa para el lenguaje Python, que posibilita manipular datos de un lote de forma programática. En otras palabaras, va a permitirnos hacer las mismas operaciones que haríamos en una hoja de cálculos, pero utilizando código.

El siguiente paso es conseguir un lote y cargarlo dentro de Jupyter (es decir, esta aplicación) en la forma de un `DataFrame` llamado `bibliotecas`

## 6. Tablas y columnas

Momento... ¿lo qué? ¿Un `DataFrame`?  ¿Qué es eso?

Hasta ahora veníamos trabajando con cosas como números (por ejemplo, el `1`, el `42` y el `30410`) y booleanos (`True` o `False`); pero eso es muy limitado. Por eso vamos a usar ahora un nuevo tipo de dato llamado `DataFrame`, que es el tipo de la variable `bibliotecas`:

## 7. Poniéndonos cuantitativos

len y len de columns

## 8. La cabeza...

head y tail

## 9. ...y la cola


## 10. Ordená, ¡es una orden!

```python
# sort_values también es una función infija
# tabla.sort_values(nombre_columna)
florerias.sort_values("COMUNA")
```

## 11. Del derecho y del revés

```python
florerias.sort_values("COMUNA", ascending=False)
```

## 12. Haciendo valer el orden

... combinar head + sort ...


## Una imágen vale más que mil palabras

Podemos hacer un gráfico de barras con el resultado de un `value_counts` usando `plot.bar` de la siguiente manera:

```python
dataframe.plot.bar(figsize=(tamanio_x_en_pulgadas, tamanio_y_en_pulgadas))
```


## 14. Combinando todo


### Solución posible

<details>
<summary>👀 Ver</summary>

```python
bicicleterias.head(20).tail(10)
```

</details>

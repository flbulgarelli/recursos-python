> Este material retoma material de [Bioinfo UNQ](https://github.com/AJVelezRueda/Bioinfo_UNQ/tree/master/Trabajos_Practicos/Estadistica_con_pandas)

### Introducción a la Ciencia de Datos con Python

Para este recorrido necesitarás las librerías [Pandas](https://pandas.pydata.org/), [Seaborn](https://seaborn.pydata.org/) y [Scipy](https://www.scipy.org/)


Podes corroborar si las tienes instaladas corriendo las siguientes líneas en tu intérprete de Python:

```python
import pandas as pd
import seaborn as sns
import scipy.stats as ss
```

Si correr estas lineas no tira ningún error, etonces están felizmente instaladas las bibliotecas enc uestión. De lo contrario, obtendremos un mensaje de error `ModuleNotFoundError: No module named` al correr las lineas anteriores. En tal caso, podés instalar las bibliotecas desde la consola, con el comando:

```bash
        pip install pandas
        pip install seaborn
        pip install scipy
```

En este recorrido trabajaremos sobre los datos abiertos del sobre el personal del [Ministerio de Ciencia y Tecnología](https://datasets.datos.mincyt.gob.ar/dataset/personal-de-ciencia-y-tecnologia/archivo/11dca5bb-9a5f-4da5-b040-28957126be18) del Gobierno Argentino. 

Si bien no es estrictamente necesario saber a fondo la sintaxis de Python para comenzar a utilizar Pandas, te recomendamos fuertemente realizar el [recorrido introductorio de Python](https://github.com/AJVelezRueda/UCEMA_Fundamentos_de_informatica/blob/master/Python_intro/intro_python_tutorial.md), que te brindará los conocimientos básicos de programación en general y de Python particular que te permitiran abordar este contenido sin problemas.

# Guias de Trabajo
  * [1. Un osito cariñosito](#1-pandas)
  * [2. Trabajando con DataFrames](#2-dfs)
  * [3. Métodos de los DataFrames](#3-metodos)
  * [4. Tratamiento de Datos con Python](#4-datos)

[1. Un osito cariñosito](#1-pandas) 

En este recorrido vamos a adentrarnos en el mundo de los datos, y para ello utilizaremos Pandas, una biblioteca de Python que nos permite trabajar con archivos de formato definido: CSV, un excel, etc. Además, Pandas proporciona estructuras de datos rápidas, flexibles y expresivas diseñadas para que trabajar con datos "relacionales" o "etiquetados" sea fácil e intuitivo. En criollo: Pandas es como en excel, pero super duper!

> Para pensar 🤔: Si hasta aquí no te has preguntado qué es una bliblioteca, ¡es momento de hacerse esa pregunta! ¿Para qué creés que nos puede resultar útil esta biblioteca? ¿Cuál es la ventaja de usar Pandas? ¿Por qué no solo usar Python `"de a pie"`?
>

Pandas soporta múltipes tipos de datos:

- Datos tabulares con columnas de tipo heterogéneo, como en una tabla SQL o en una hoja de cálculo de Excel
- Datos ordenados y desordenados (no necesariamente frecuencia fija).
- Datos matriciales arbitrarios (homogéneamente tipados o heterogéneos) con etiquetas de fila y columna
- Cualquier otra forma de conjuntos de datos observacionales/estadísticos. 

Los datos en realidad no necesitan ser etiquetados para ser colocados en una estructura de datos de pandas. Estas estructuras se construyen a partir de arrays(listas), pero agregando nuevas funcionalidades. Pandas maneja dos estructuras de datos: Series y DataFrames.

**Series (1-dimensional)**
Las series pueden contener cualquier tipo de datos (enteros, cadenas, números de punto flotante, etc.). Y se pueden crear del siguiente modo:

```python
import pandas as pd
una_serie = pd.Series(['Peru', 'Argentina', 'Bolivia', 'Uruguay', 'Brasil', 'Chile'], dtype='string')

print(una_serie)
```

**DataFrames (2-dimensional)**

Un DataFrame es una estructura tabular bidimensional de datos tabulares, potencialmente heterogéneos, con ejes etiquetados (filas y columnas). Las operaciones aritméticas se alinean en las etiquetas de fila y columna. Se puede considerar como un contenedor similar a un dict para objetos Serie. Podemos crear un DataFrame del sigueinte modo:

```python
paises_latam = pd.DataFrame(data ={"Pais": ['Peru', 'Argentina', 'Bolivia', 'Uruguay', 'Brasil', 'Chile'], "Lengua oficial primaria": ['Español', 'Español', 'Español', 'Español', 'Portugues', 'Español']}, index = [1,2,3,4,5,6])

print(paises_latam)
```

Por lo tanto, la serie es la estructura de datos para una sola columna de un DataFrame, no solo conceptualmente, sino literalmente, es decir, los datos en un DataFrame se almacenan realmente en la memoria como una colección de Series.

También, se puede crear un DataFrame a partir de un diccionario, en este caso las claves se corresponderán con los nombres de las columnas y los valores con los datos de las filas para cada columna:

```python
#será DataFrame(data=diccionario, index=filas, columns=columnas, dtype=tipos)
datos = {"Pais": ['Peru', 'Argentina', 'Bolivia', 'Uruguay', 'Brasil', 'Chile'], "Idioma oficial": ['Español', 'Español', 'Español', 'Español', 'Portugues', 'Español']}
paises_latam = pd.DataFrame(datos)

print(paises_latam)
```
🛑 Alerta: los valores asociados a las claves del diccionario deben ser listas del mismo tamaño

`df` es el nombre génerico para designar DataFrame y es el nombre que utilizaremos de ahora en más para mayor simplicidad.


Otra forma muy usual de generar DataFrames es mediante la lectura de **archivos estructurados**. Existen muchas formas de cargar/leer información desde archivos la información desde archivos pero en general la diferencia radica principalmente en los parámetros por defecto que toman para definir las columnas. Por ejemplo: 

- El caracter de separación de columnas por defecto del método `read_cvs` es una coma (',') 
- El caracter de separación de columnas por defecto del método `read_fwf` es una tab ('\t').

```python
import pandas as pd
df = pd.read_csv(path_al_erchivo)
```

>  🧗‍♀️ Desafío I: Estos métodos aceptan otros parámetros que merecen la pena ser explorados. Averiguá para qué sirven los parámetro sep, index_col, nrows y header

>  🧗‍♀️ Desafío II: Descargá a tu computadora la [tabla](https://datasets.datos.mincyt.gob.ar/dataset/personal-de-ciencia-y-tecnologia/archivo/11dca5bb-9a5f-4da5-b040-28957126be18) de personas que conforman el Ministerio de Ciencia y Tecnología de Argentina, en formato csv.
>
> Cargá (lee) la tabla a un DataFrame de Pandas de nombre `personas` ¿Qué forma te lectura de archivos usarías? ¿Qué separación entre columnas posee el archivo? ¿Cómo te diste cuenta? 🤔
>

Ya tenemos nuestra tabla cargada, podeés hacer una previsualización de los datos haciendo:

```python
personas.head()
```
> Para pensar 🤔: ¿Cuántas filas se imprimen al hacer head? ¿Qué sucede si hacemos `personas.head(10)`? ¡Probalo!

[2. Trabajando con DataFrames](#2-dfs)

Ahora que aprendiste a cargar datos en una `"tabla"` de Pandas, podés averiguar la información general de tu tabla haciendo: 

```python
personas.info()
```

Si bien esta información nos ayuda a saber los nombres de las columnas de nuestra tabla, o el tipo de datos que contiene cada una de ellas, quizás una descripción más informativa podría ser:

```python
personas.describe()
```
> Para pensar 🤔: ¿Qué tipo de información nos brinda el método describe? ¿Tienen sentido estos cálculos para todas las columnas?
>

Podemos acceder a los datos de cada columna haciendo df['nombre de la columna'], en nuestro caso por ejemplo:

``` python
personas[' persona_id']
```

> Para pensar 🤔: ¿Podés imprimir la columna de los `max_dedicacion_horaria_docente_id` de nuestra tabla? ¿Cómo calcularías el promedio de esta columna?

Quizás nos resulte útil acceder, no a todos los datos de una columna, sino a un dato de una celda en particular. Para ello podemos utilizar _iloc_:

```python
df.loc[fila, columna] 
```
esto devuelve el elemento que se encuentra en la fila con nombre fila y la columna de con nombre columna del DataFrame df. Probá el siguiente código:

```python
personas.loc[2, 'persona_id']
```

> Para pensar 🤔: ¿Qué resultado obtuviste? ¿Por qué? ¿Cómo obtendrías la edad de esa persona?

Podemos acceder los datos de una columna del DataFrame como una lista mediante el método _tolist()_:

``` python
df['columna'].tolist()
```

>  🧗‍♀️ Desafío IV: Extrae la columna `seniority_level` y contá cuántas personas tenían expertice nivel B, C y D

Seguramente tu resulación del _Desafío IV_ implicó hacer un _bucle for_ y un if, lo cual parece a priori un tanto engorroso. Para evitarnos tantas lineas de código, podemos hacer uso de los métodos _groupby()_ y _count()_, que nos permiten contar sobre una columna la frecuencia de un dato/evento en particular. Ejecutá las siguientes lineas a ver qué pasa:

```python
personas["seniority_level"].count()

personas.groupby("seniority_level").count()

personas.groupby("seniority_level")[["persona_id"]].count()
```

> 🧗‍♀️ Desafío V: ¿Qué resultados obtuviste en cada caso? Explicá qué hace cada linea de código

Podemos operar con las columnas con los mismo operadores relacionales y matemáticos que ya hemos visto:

``` python
personas['edad'] * 2
personas['edad'] + 2
personas['edad'] > 2  
```          
> Para pensar 🤔: ¿Qué resultado nos daría en cada caso? 

Pero los operadores tambien nos sirven también para filtrar nuestro DataFrame:

``` python
personas[personas['edad'] < 35 ]
```         

> 🧗‍♀️ Desafío V: Contá cuántas personas de 30 años ingresaron al ministerio en 2011 ¿Cuántas formas de hacer este cálculo se te ocurren?

Ahora vamos a ver cómo podemos incorporar más información a nuestro DataFrame. En la página del ministerio podés encontrar las tablas que pueblas la tabla general...veamos por ejemplo la tabla de [categoría de conicet](https://datasets.datos.mincyt.gob.ar/dataset/personal-de-ciencia-y-tecnologia/archivo/c72c9f88-d9ef-4349-bb20-5c9a1aca5d67)

> 🧗‍♀️ Desafío VI: Descargala en formato csv y cargala en un nuevo DataFrame de nombre `categorias`
> 🧗‍♀️ Desafío VII: Identificá si existen columnas en común con el DataFrame grande

Supongamos que ahora queremos poder realizar análisis de nuestros datos filtrando por categoria de conicet, en este caso podemos combinar las dos tablas, de modo de saber qué valos de `categoria_conicet_id` se corresponde con cada categoria de conicet. Probemos haciendo:

``` python
personas_cat = pd.merge(personas, categorias, on='categoria_conicet_id')
```

> Para pensar 🤔: ¿Qué datos tiene df3? ¿Qué hace el método merge? 

Probemos ahora el método _concat()_:
``` python
personas_cat = pd.conact([personas, categorias])
```
> Para pensar 🤔: ¿Qué datos tiene df3? ¿Qué hace el método _concat()_ y qué diferencia tiene con hacer _merge()_? 

[3. Métodos de los DataFrames](#3-metodos)

Veamos un resumen de los métodos que podés encontrar en Pandas para trabajar con DataFrames: 

| Lectura/carga de datos | Limpieza de los datos | Estdistica de los datos |
|-------------	|----------	|---	|
| pd.read_csv() | pd.head() | pd.describe() |
| pd.read_table() | pd.fillna() |df.sample()|
| pd.read_excel() | pd.dropna() | pd.mean() |
| pd.read_sql() | pd.sort_values() | pd.median() |
| pd.read_json() | pd.groupby() | pd.std() |
| pd.to_csv() |pd.apply() | pd.min() |
| pd.DataFrame() | pd.append() | pd.max() |
| pd.concat() | pd.rename()  | pd.count() |
| pd.Series() | pd.set_index() | pd.corr() |
| pd.DataFrame.from_dict() |  pd.tail() | pd.hist() |


>
>  🧗‍♀️ Desafío III: averiguá para qué sirve cada uno de los métodos y qué parámetros podés pasarseles. ¡Esta información nos será útil para más adelante!
>

Ahora que conocemos algunas de los métodos que nos permiten trabajar con DataFrames, veamos como cómo [trabajar los datos](https://github.com/flbulgarelli/recursos-python/blob/master/2_Ciencia_de_datos_pandas/Analisis_de_datos_con_pandas.md) 🤓
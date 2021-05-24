> Basado en [Fundamentos de Informatica](https://github.com/AJVelezRueda/Fundamentos_de_informatica)
### Introducción a la Ciencia de Datos con Python

Para este recorrido necesitarás las librerías [Pandas](), [Seaborn]() y [Scipy]()


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
  * [2. Tratamiento de Datos con Python](#)

[1. Un osito cariñosito](#1-pandas) 
En este recorrido vamos a adentrarnos en el mundo de los datos, y para ello utilizaremos Pandas, una biblioteca de Python que nos permite trabajar con archivos de formato definido: CSV, un excel, etc. Además, Pandas proporciona estructuras de datos rápidas, flexibles y expresivas diseñadas para que trabajar con datos "relacionales" o "etiquetados" sea fácil e intuitivo. En criollo: Pandas es como en excel, pero super duper!


Pandas soporta múltipes tipos de datos:

- Datos tabulares con columnas de tipo heterogéneo, como en una tabla SQL o en una hoja de cálculo de Excel
- Datos ordenados y desordenados (no necesariamente frecuencia fija).
- Datos matriciales arbitrarios (homogéneamente tipados o heterogéneos) con etiquetas de fila y columna
- Cualquier otra forma de conjuntos de datos observacionales/estadísticos. 

Los datos en realidad no necesitan ser etiquetados para ser colocados en una estructura de datos de pandas. Pandas maneja dos estructuras de datos:

- Series (1-dimensional)
- DataFrames (2-dimensional)

Un DataFrame es una estructura tabular bidimensional de datos tabulares, potencialmente heterogéneos, con ejes etiquetados (filas y columnas). Las operaciones aritméticas se alinean en las etiquetas de fila y columna. Se puede considerar como un contenedor similar a un dict para objetos Serie. La estructura de datos de los pandas primarios. Los DataFrames de pandas proporcionan las mismos tipos de usos y utilidades que los data.frame de R.

Por lo tanto, la serie es la estructura de datos para una sola columna de un DataFrame, no solo conceptualmente, sino literalmente, es decir, los datos en un DataFrame se almacenan realmente en la memoria como una colección de Series.

> Para pensar 🤔:¿?
>
> 🧗‍♀️ Desafío I:   
>
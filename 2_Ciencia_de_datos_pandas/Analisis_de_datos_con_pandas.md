> Este material retoma material de [Bioinfo UNQ](https://github.com/AJVelezRueda/Bioinfo_UNQ/tree/master/Trabajos_Practicos/Estadistica_con_pandas) y [Python_for_friends](https://github.com/jennifergc/Python_for_friends/tree/Angie)


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
 * [1. Tratamiento de Datos con Python](#1-datos)


[1. Tratamiento de Datos con Python](#1-datos)

El primer paso para poder analizar los datos y sacar conclusiones de ese análisis es realizar una
limpieza de los mismos... ¡claro que no vamos a pasarle el plumero para sacarle el polvo! Limpieza de datos se refiere por ejemplo a verificar si faltan datos o si a alguna de las columnas debe hacerseles una corrección de notación o de tipo de dato, etc.

Para ello vamos a recurrir a alguno de los métodos que vimos en la [guía introductoria](https://github.com/flbulgarelli/recursos-python/blob/master/2_Ciencia_de_datos_pandas/Introducci%C3%B3n_pandas.md). Para comenzar descargaremos localmente la [tabla](https://datasets.datos.mincyt.gob.ar/dataset/personal-de-ciencia-y-tecnologia/archivo/11dca5bb-9a5f-4da5-b040-28957126be18) de personas que conforman el Ministerio de Ciencia y Tecnología de Argentina, en formato csv. Podemos cargar (leer) la el contenido del archivo en un DataFrame de Pandas de nombre `personas`

```python
import pandas as pd
personas =  pd.read_csv("personas_2011_cyt.csv", sep=";")
personas.head()
```

> Para pensar 🤔: Al imprimir el DataFrame se ven celdas con valores `NaN` ¿Qué son esos valores?¿Qué significa?
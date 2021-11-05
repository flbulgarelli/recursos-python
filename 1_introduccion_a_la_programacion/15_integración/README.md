# Integración

## 1. Repaso

🛑 Hagamos un alto en el camino. ¿Qué vimos hasta acá?

* Herramientas de programación
  * Operadores matemáticos, lógicos y de strings
  * Funciones, parámetros y procedimientos
  * Alternativa condicional (`if`)
  * Variables
  * Repetición indexada (`for ... in`)
* Estructuras de datos
  * Listas: colecciones homogéneas con repetidos que preservan el orden
  * Diccionarios: colecciones heterogéneas de pares clave-valor (llamados entradas) que no tienen un orden particular
  * Tablas (`DataFrame`s): estructuras tabulares con filas y columnas
* Procesamiento de datos
  * Se puede hacer de diferentes formas:
     * con operaciones de alto nivel:
        * `len`, `all`, `any`, `max`, `sum`, `sorted` _listas por comprensión_, etc (listas)
        * `groupby`, `dropna`, `value_counts`, `head`, filtros, etc (tablas)
     * con operaciones de bajo nivel (recorridos), combinando las herramientas antes vistas: `for`, `if`, variables acumuladoras, variables contadoras, segmentos, acceso indexado, operaciones de alto nivel, etc
  * Los distintos procesamientos que vimos caen en general en las siguientes categorías:
    * Agregación:
      * sumatorias (`sum`)
      * promedios (`mean`)
      * medianas (`median`)
      * cuantiles (`quantile`)
      * máximos y mínimos (`max`, `min`, `idxmax`, `idxmin`)
    * Ordenamiento (`sort_values`, `sorted`)
    * Recorte:
      * Primeros N elementos (head: `cabeza`)
      * Últimos N elementos (cola: `tail`)
      * Elementos N al M (secciones: `slices`)
    * Agrupación (`groupby`)
    * Transformación:
      * Renombrado de columnas / entradas (`rename`)
      * Creación de columnas / entradas
      * Eliminación de columnas / entradas (`del`, `drop`)
    * Filtrado
    * Acceso indexado (`iloc`, `una_lista[índice]`)

¡Fueron un montón de cosas!

> Como material de referencia, te dejamos algunos links para que leas y tengas a mano a partir de ahora:
>
> * [guía rápida de python](https://flbulgarelli.github.io/recursos-python/1_introduccion_a_la_programacion/15_integraci%C3%B3n/referencia_r%C3%A1pida_python/)
> * [otra de pandas](https://flbulgarelli.github.io/recursos-python/1_introduccion_a_la_programacion/15_integraci%C3%B3n/referencia_r%C3%A1pida_pandas/)
>

## 2. `anio`

Definí la función `anio` que dado un string con una fecha (como por ejemplo `"30/11/2014"`) devuelva el año, como **un número**. La función tiene que andar tanto con si el string original completa los dígitos con cero como si no lo hace.

Por ejemplo:

```python
>>> anio("30/11/2014")
2014
>>> anio("05/01/0152")
152
>>> anio("5/1/152")
152
```

## 3. Estadísticas del curso

Tenemos datos de un curso como el siguiente:

```python
curso_ejemplo = [
  {
    'legajo': '123446',
    'nombre': 'María',
    'apellido': '(...)',
    'notas' : [10, 2, 3],
    'zona': 'Quilmes'
  },
  {
    'legajo': '123450',
    'nombre': 'Carlos',
    'apellido': '(...)',
    'notas' : [5, 8, 8],
    'zona': 'CABA'
  },
  {
    'legajo': '123430',
    'nombre': 'Liz',
    'apellido': '(...)',
    'notas' : [4, 8, 2],
    'zona': 'CABA'
  },
  {
    'legajo': '123453',
    'nombre': 'Hector',
    'apellido': '(...)',
    'notas' : [9, 9, 1],
    'zona': 'Temperley'
  },
  {
    'legajo': '123110',
    'nombre': 'Ana',
    'apellido': '(...)',
    'notas' : [6, 7, 8],
    'zona': 'Quilmes'
  },
  {
    'legajo': '123371',
    'nombre': 'Ivana',
    'apellido': '(...)',
    'notas' : [7, 7, 9],
    'zona': 'Avellaneda'
  }
]
```

> Con esta información, definí las siguientes tres funciones:
>
>   1. `nota_final(un_estudiante)`: devuelve la nota final de un estudiante, que se calcula como el promedio de sus notas
>   1. `promedio_de_notas_del_curso(un_curso)`: devuelve el promedio general de las notas finales del curso
>   1. `estudiantes_aprobados(un_curso)`: devuelve aquellos estudiantes cuyas notas individuales (sin importar la nota final) son todas mayores o iguales a 4.
>
> Ejemplo:
> ```python
> >>> estudiantes_aprobados(curso_ejemplo)
> [
>  {
>     'legajo': '123450',
>     'nombre': 'Carlos',
>     'apellido': '(...)',
>     'notas' : [5, 8, 8],
>     'zona': 'CABA'
>   },
>   {
>     'legajo': '123110',
>     'nombre': 'Ana',
>     'apellido': '(...)',
>     'notas' : [6, 7, 8],
>     'zona': 'Quilmes'
>   },
>   {
>     'legajo': '123371',
>     'nombre': 'Ivana',
>     'apellido': '(...)',
>     'notas' : [7, 7, 9],
>     'zona': 'Avellaneda'
>   }
> ]
> ```

### 4. Zonas y legajos

Ahora vamos a querer más estadísticas:

  1. `cantidad_de_estudiantes_por_zona(un_curso)`: devuelve un diccionario con la cantidad de estudiante que hay en cada zona
  1. `legajos_de_estudiantes(un_curso)`: devuelve una lista con sólo los legajos
  1. `nombre_completo_de(legajo, un_curso)`: busca un estudiante por legajo y devuelve su nombre completo, asumiendo que el legajo existe.
  1. `legajo_registrado(legajo, un_curso)`: dice si existe un estudiante con el legajo dado

Ejemplos:

```python
>>>> cantidad_de_estudiantes_por_zona(curso_ejemplo)
 {
  "Quilmes": 2,
  "CABA": 2,
  "Temperley": 1,
  "Avellaneda": 1
}
>>> legajos_de_estudiantes(curso_ejemplo)
['123446', '123450', '123430', '123453', '123110', '123371']
>>> nombre_completo_de('123446', curso_ejemplo)
"María (...)"
>>> legajo_registrado('89612', curso_ejemplo)
False # nadie tiene ese legajo
```

> Definí las nuevas funciones.

## 5. Estadísticas de estudiantes, recargada

Usando `pandas`, Creá un `DataFrame` en pandas con los datos de ejercicio anterior ....

```python
import pandas as pd

estudiantes = pd.DataFrame(curso_ejemplo)
```

...y realizá los siguientes análisis:

1. Realizá un gráfico de barras donde se ve la cantidad de estudiantes por zona.
1. Generá una tabla con cada zona del curso y su cantidad de estudiantes
1. Generá una tabla con dos columnas: una con el legajo y otra con el nombre completo de cada estudiante
1. Bonus: generá una tabla igual a la original pero que reemplace la columna de notas individuales de cada estudiante por otra con su nota promedio

## 6. Tabla de emojis 😜

Cargá [este](https://raw.githubusercontent.com/github/gemoji/ce6c4ab12ae229be2b1089cbf7e85702fdc5552f/db/emoji.json) archivo en una tabla de `pandas`...

```python
import pandas as pd

# notá que este archivo no es un CSV, sino un JSON, un formato
# muy diferente pero que podemos cargar de forma muy similar
emojis = pd.read_json("https://raw.githubusercontent.com/github/gemoji/ce6c4ab12ae229be2b1089cbf7e85702fdc5552f/db/emoji.json")
emojis
```

... y respondé lo siguiente:

1. ¿Cuántas categorías de emojis hay?
1. ¿Cuántas banderas hay?
1. ¿Cuáles son todos los emojis que estén diferenciados por tono de piel?
   * Bonus: Imprimí cada uno usando `print`
1. ¿Cuántos y cuáles emojis se incorporaron entre la versión 13 y 14 de IOS?

## 7. Banderas

Usando la tabla `emojis` del ejercicio anterior, definí una función `bandera_de` que tome el nombre de un país (en inglés) y te de su bandera.

Por ejemplo:

```python
>>> bandera_de("Argentina")
'🇦🇷'
>>> bandera_de("Brazil")
'🇧🇷'
>>> emojificar("Mexico")
'🇲🇽'
```

## 7. Emojificar

Definí la función `emojificar`, que tome un texto y reemplace todas las palabras que se correspondan con el alias de un emoji por el emoji correspondiente.

Por ejemplo:

```python
>>> emojificar("Emojificando smile")
'Emojificando 😄'
>>> emojificar("hola argentina")
'hola 🇦🇷'
>>> print(emojificar("pizza y mate"))
# el print puede ser
# necesario si el emoji no se ve bien
🍕 y 🧉
```

### Ayuda

Hay varias formas de encarar este ejercicio. Una de ellas es recorrer la tabla de `emojis` iterando los índices, y luego accediendo cada fila con `iloc`:

```python
for index in emojis.index:
  emoji = emojis.iloc[index]
  # y ahora emoji es una fila que podés
  # usar como emoji.skin_tones, por ejemplo
```

Otra más sencilla es usar `itertuples()` que nos permite recorrer directamente cada fila:

```python
for emoji in emojis.itertuples():
  # y ahora emoji es una fila que podés
  # usar igual que el ejemplo anterior
```

Por último, también podés convertir el dataframe `emojis` en una lista de diccionarios usando ...

```python
# esto devuelve una lista de diccionarios
emojis.to_dict("records")
```

... y luego recorrerla normalmente.

Por último, ojo porque hay muchos emojis que tienen alias muy cortos y si no tenés cuidado te puede pasar ésto:

```python
>>> emojificar("hola argentina")
'h⭕l🅰️ 🅰️rgentin🅰️'
```

## 8. Partidos de fútbol

En una aplicación tenemos estadísticas de partidos de fútbol ⚽ como las siguientes:

```python
partidos_de_ejemplo = [
 {'anio': 2015,
  'dia': 17,
  'equipo_local': 'Belgrano',
  'equipo_visitante': 'Nueva Chicago',
  'goles_locales': 3,
  'goles_visitantes': 1,
  'mes': 2,
  'resultado': 'local'},
 {'anio': 2017,
  'dia': 22,
  'equipo_local': 'Olimpo Bahia Blanca',
  'equipo_visitante': 'Estudiantes L.P.',
  'goles_locales': 3,
  'goles_visitantes': 1,
  'mes': 5,
  'resultado': 'local'},
 {'anio': 2015,
  'dia': 31,
  'equipo_local': 'Tigre',
  'equipo_visitante': 'Defensa y Justicia',
  'goles_locales': 0,
  'goles_visitantes': 0,
  'mes': 3,
  'resultado': 'empate'},
 {'anio': 2020,
  'dia': 8,
  'equipo_local': 'Banfield',
  'equipo_visitante': 'Rosario Central',
  'goles_locales': 1,
  'goles_visitantes': 1,
  'mes': 2,
  'resultado': 'empate'},
 {'anio': 2017,
  'dia': 25,
  'equipo_local': 'Tigre',
  'equipo_visitante': 'Velez Sarsfield',
  'goles_locales': 0,
  'goles_visitantes': 3,
  'mes': 8,
  'resultado': 'visitante'}]
```

Como vemos, estas estadísticas tienen información de la fecha, equipos que se enfrentaron, y quien ganó (`resultado`) y qué goles hizo cada equipo.

> Sabiendo ésto, definí una función `goles_hechos_a`, que reciba un equipo y un diccionario con las estadísticas de un partido, y devuelva la cantidad de goles que le hicieron al equipo dado, sin importante si fueron de visitante o local.
>
> Por ejemplo:
>
> ```python
> >>> goles_hechos_a("Tigre", {
>  'equipo_local': 'Rosario Central',
>  'equipo_visitante': 'Tigre',
>  'goles_locales': 2,
>  'goles_visitantes': 1,
>  ...
> })
> 2 # porque Tigre era visitante y hubo un sólo gol local
> >>> goles_hechos_a("River Plate", {
>   'equipo_local': 'River Plate',
>   'equipo_visitante': 'Quilmes',
>   'goles_locales': 2,
>   'goles_visitantes': 3,
>   ...
> })
> 3 # porque River era local y hubo dos goles visitantes
> ```
>
> **Nota**: asumí que la función será siempre invocada con uno de los dos equipos participantes.

## 9. Tajaí

Definí una función `participo` que diga si un equipo partició en un partido.

```python
>>> participo("Nueva Chicago", partidos_de_ejemplo[0])
True # Porque fue un partido Belgrano vs Nueva Chicago
>>> participo("Olimpo Bahia Blanca", partidos_de_ejemplo[1])
True # Porque fue vs Olimpo Bahia Blanca vs Estudiantes L.P.
>>> participo("River Plate", partidos_de_ejemplo[1])
False
```

## 10. El clásico del domingo

Los domingos necesitamos armar los titulares que se ven durante el partido y al finalizar. Por ejemplo:

```python
>>> titular_durante(partidos_de_ejemplo[3])
"El minuto a minuto del Banfield - Rosario Central"
>>> titular_final(partidos_de_ejemplo[4])
"Tigre 0 - 0 Defensa y Justicia: toda la información"
```

> Definí las funciones `titular_durante` y `titular_final`

## 11. ¡6 a 1!

Definí una función `mayor_goleada_recibida` que responda cuál fue la mayor goleada recibida, independientemente de si fue recibida de local o visitante. Probablemente te convenga reutilizar algunas de las funciones anteriores

## 12. Siamo Fuori

Definí una función `perdio`, que diga si un equipo perdió en un partido. **Nota**: si el equipo empató o no partició, diremos que _no perdió_.

## 13. Saliendo a la cancha

¡Llegó la hora de usar datos reales!

> Cargá desde https://www.football-data.co.uk/new/ARG.csv una tabla de pandas y mirá qué contiene.

## 13. No todo es información

Dado que no vamos a usar todas las columnas, vamos a quedarnos sólamente con las siquientes:

* League = `League Division` (división)
* Date = `Match Date` (fecha del partido dd/mm/yy)
* Time = `Time of match kick off` (horario de inicio)
* Home = `Home Team` (equipo local)
* Away = `Away Team` (equipo visitante)
* HG = `Home Team Goals` (goles locales)
* AG = `Away Team Goals` (goles visitantes)
* Res = `Full Time Result` (H=Home Win, D=Draw, A=Away Win) (resultado)

> Recortá el dataframe para que contenga sólo las columnas mencionadas

## 14. Es la misma columna, pero el nombre es nuevo

El problema es que las columnas tienen nombres difíciles de recordar, y no se parece mucho a lo que veníamos trabajando.

> Renombrar las columnas para que sus nombres coincidan con lo que representan, en español. Inspirate en las estadísticas de ejemplo que usamos en los ejercicios anteriores.

## 15. Cambiando el resultado

Ah, pero los valores de la columna `resultado` tampoco coinciden con los que veníamos trabajando.

> Convertí los códigos de la columna resultado de la siguiente forma:
>
>  * `H` ➡️ `local`
>  * `A` ➡️ `visitante`
>  * `D` ➡️ `empate`
>

### Ayuda

Podés transformar los valores de una columna usando `un_datagrame.una_columna.map(diccionario)`, donde las claves del diccionario son los valores originales, y los valores, los valores nuevos.

## 16. Todo a su tiempo

Momento, ¿y de cuándo son estos datos? ¿Desde qué año hay registros?

> Transformá la columna de fecha en `datetime` para que podamos maniuplarla adecuadamente, agregá una columna `anio` y finalmente respondé la pregunta.

### Ayuda

Te va a convenir usar la función `pd.to_datetime`.

## 17. De visitante

¿Cuál es el promedio de goles visitante y local de cada año?

> Hacé una tabla que contenga una fila por cada liga con sus resultados y un gráfico de barras donde se presente esta información

## 18. Tantas estadísticas me dieron hambre

¿Cuál es la proporción de victorias de local, visitante y empates?

> Calculá estas estadísticamente numéricamente y con ellas hacé un gráfico de torta 🥧.

## 19. ¡Hay equipo(s)!

1. ¿Qué cantidad de equipos participaron?
2. ¿Cuál es el promedio de goles que le hicieron a cada equipo siendo local? Hacé una tabla con una fila por cada partido que responda esta pregunta
3. ¿Y cuál es la mayor cantidad de goles que le hicieron a un equipo siendo visitante? Hacé una tabla que responda ésto por cada equipo.
4. Bonus: representalo también como un gráfico de barras horizontal, ordenado de mayor a menor

## 20. Para cerrar

Ahora que tenemos los datos reales, ¿podríamos usar nuestras primeras funciones con ellos?

> Actualizá la variable `partidos_de_ejemplo` para que tenga una lista de diccionarios iguales a los originales, pero esta vez generados tomando 20 partidos al azar de la tabla.
>

### Ayuda

Recordá que contás con `un_dataframe.sample` y que podés transformar una tabla en una lista de registros usando `to_dict("records")`

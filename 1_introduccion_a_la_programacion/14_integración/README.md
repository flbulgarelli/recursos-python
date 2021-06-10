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

Para más información, te dejamos de referencia una [guía rápida de python](https://github.com/flbulgarelli/recursos-python/tree/master/1_introduccion_a_la_programacion/14_integraci%C3%B3n/referencia_r%C3%A1pida_python#readme) y [otra de pandas](https://github.com/flbulgarelli/recursos-python/tree/master/1_introduccion_a_la_programacion/14_integraci%C3%B3n/referencia_r%C3%A1pida_pandas#readme)

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

Con esta información, definí funciones que calculen las siguientes estadísticas:

  1. `nota_final(un_estudiante)`: devuelve la nota final de un estudiante, que se calcula como el promedio de sus notas
  1. `promedio_de_notas_del_curso(un_curso)`: devuelve el promedio general de las notas finales del curso
  1. `estudiantes_aprobados(un_curso)`: devuelve aquellos estudiantes cuyas notas individuales (sin importar la nota final) son todas mayores o iguales a 4.
  1. `cantidad_de_estudiantes_por_zona(un_curso)`: devuelve un diccionario con la cantidad de estudiante que hay en cada zona
  1. `legajos_de_estudiantes(un_curso)`: devuelve una lista con sólo los legajos
  1. `nombre_completo_de(legajo, un_curso)`: busca un estudiante por legajo y devuelve su nombre completo, asumiendo que el legajo existe.
  1. `legajo_registrado(legajo, un_curso)`: dice si existe un estudiante con el legajo dado
Ejemplos:

```python
>>> estudiantes_aprobados(curso_ejemplo)
[
  {
    'legajo': '123450',
    'nombre': 'Carlos',
    'apellido': '(...)',
    'notas' : [5, 8, 8],
    'zona': 'CABA'
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
>>> cantidad_de_estudiantes_por_zona(curso_ejemplo)
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

## 4. Estadísticas de estudiantes, recargada

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

## 5. Tabla de emojis 😜

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

## 6. Banderas

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

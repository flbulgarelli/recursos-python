> Basado en https://github.com/mumukiproject/mumuki-guia-python3-repeticion-condicional-e-indexada-2021


# Secuencias y Repetición

Como te contábamos cuando empezaste, programar nos da un gran poder: **nos permite automatizar tareas repetitivas y tediosas**.

¿Y qué quiere decir eso de "repetitivas"? Pensemos, por ejemplo, ¿cómo haríamos una función que sume los primeros 5 elementos de una lista?

```python
def sumar_los_primeros_5(una_lista):
  return una_lista[0] + una_lista[1] + una_lista[2] + una_lista[3] + una_lista[4]
```

¿Notás qué es lo que se repite? Sí, estamos haciendo 4 veces lo mismo: _acceder a un elemento por índice y luego sumarlo_. Sin dudas, sería mucho más interesante que la computadora hiciera eso por nosotros... ¡o si no te estaríamos mintiendo con lo de automatizar! 😑

En esta guía vamos a aprender cómo decirle a la computadora que repita varias veces lo mismo, y también algunos trucos más.

## 1. No tan distintos

En las lecciones anteriores vimos varias funciones (¡y algunos operadores!) que operan con números, otras con booleanos, y así.

Pero quizás ya hayas notado que hay dos operaciones en particular que son bastante _peculiares_: `len` e `in`. ¿Por qué? Observemos los siguientes ejemplos:

```python
>>> len("no tenemos pertenencias sino equipaje")
37
>>> "en" in len("un alma sola dividida en dos")
True
>>> len([4, 8, 15, 16, 23, 42])
6
>>> 34 in [1, 1, 2, 3, 5, 8, 13, 21, 34]
True
```

¡`len` e `in` funcionan tanto con listas como con strings!

> ¿Será casualidad? ¿Habrá más operaciones en común entre estos dos tipos de datos? Averigüemoslo probando lo siguiente:
>
> ```python
> >>> "Del árbol" + " una hoja se cayó"
> >>> "Sin brújula y sin radio"[4]
> >>> [1, 4] + [4, 5]
> >>> ["el", "carozo", "cantó"][2]
> ```


### Para pensar

Como vemos, las listas y los strings, si bien _no son lo mismo_, son más parecidos de lo que pensábamos: ambos tipos de datos representan _secuencias_.

* los strings son secuencias de caracteres, como `'a'`, `'b'`, `'#'`, etc;
* las listas son secuencias de cualquier tipo de dato: números, booleanos, strings, o incluso otras listas.



## 2. Una rebanada, por favor

Otras operaciones que listas y strings tienen en común son los _slices_, que podemos traducir como segmentos, secciones, o (de forma más literal y graciosa) rebanadas  🍞, que nos permite obtener los elementos entre dos límites:

```python
>>> numeros = [10, 20, 30, 40, 50]
>>> numeros[0:2]
[10, 20]         # es la lista conformada por el 1er y 2do elemento;
                 # ⚠️ recordemos que los índices en Python cuentan desde 0
>>> numeros[2:4]
[30, 40]         # es la lista conformada por el 3er y 4to elemento
>>> numeros[0:4]
[10, 20, 30, 40] # es la lista conformada
                 # por los elementos 1 al 4
>>> numeros[:4]
[10, 20, 30, 40] # equivalente al ejemplo anterior;
                 # si no ponemos el límite inferior,
                 # trae todos los elementos desde el principio
>>> numeros[3:]
[40, 50]         # es la lista conformada
                 # por todos los elementos partir del 4to
                 # si no ponemos el límite superior,
                 # trae todos los elementos hasta el final
```


> ¡Usemos lo aprendido para extraer segmentos de los strings! Ya cargamos en la consola una variable de tipo string  llamada `primera_estrofa`; aplicando lo visto te toca:
>
>  1. Averiguar cuantos caracteres tiene `primera_estrofa`
>  2. Obtener un string con los primeros 22 caracteres de `primera_estrofa`
>  3. Obtener un string con los últimos 25 caracteres de `primera_estrofa`
>

### Pistas

💡 Algunas sugerencias:

* Tanto los primeros 22 caracteres como los útimos 25 tienen palabras completas. Si ves alguna palabra cortada, es porque no estás usando los límites correctos. 🙅
* Para resolver la última tarea te puede ser útil escribir algo del estilo `primera_estrofa[aca_va_el_punto_de_partida:]` ¿Y cómo hacer para saber cuáles cuál es el primero de los últimos 25 caracteres? Probá restar 25 al largo de la lista 😉
* Si te pica la  curiosidad 🐝, podés ver qué contiene `primera_estrofa`, escribiendo, simplemente, `primera_estrofa`. El problema es que se verá mezclado con varios caracteres _extraños_. Probá usar entonces `print(primera_estrofa)`. No te preocupes: ya hablaremos de esto de breve.


### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
def listo():
  pass


primera_estrofa = """
Aquí me pongo a cantar
al compás de la vigüela,
que el hombre que lo desvela
una pena estraordinaria,
como la ave solitaria
con el cantar se consuela
""".strip()

>>> True
True
```



### Para pensar

¡Bien! Probablemente te haya resultado bastante tedioso resolver la tercera tarea:

```python
primera_estrofa[len(primera_estrofa) - 25:]
```

al fin y al cabo, no teníamos ninguna forma para indicar de forma más sencilla que queríamos los últimos 25 elementos.... ¿o sí? ¡Averguémoslo!

## 3. Al derecho y al revés

¡Los segmentos `[:]` y el operador de indexación `[]` no serían tan útiles si no pudieramos contar también de atrás para adelante! ⬅️ Por eso es que Python nos permite utilizar:

 * índices positivos: empiezan en `0` y cuentan los elementos desde la primera posición hasta la última;
 * índices negativos: empiezan en `-1` y cuentan los elementos desde la última posición hasta la primera.

Por ejemplo, esto nos permitirá entender al string `"hola mundo"` de dos formas diferentes...

<table class="table table-bordered">
<thead>
  <tr>
    <th></th>
    <th>h</th>
    <th>o</th>
    <th>l</th>
    <th>a</th>
    <th></th>
    <th>m</th>
    <th>u</th>
    <th>n</th>
    <th>d</th>
    <th>o</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>➡️</td>
    <td>0</td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>4</td>
    <td>5</td>
    <td>6</td>
    <td>7</td>
    <td>8</td>
    <td>9</td>
  </tr>
  <tr>
    <td>⬅️</td>
    <td>-10</td>
    <td>-9</td>
    <td>-8</td>
    <td>-7</td>
    <td>-6</td>
    <td>-5</td>
    <td>-4</td>
    <td>-3</td>
    <td>-2</td>
    <td>-1</td>
  </tr>
</tbody>
</table>


... y hacer operaciones como las siguientes:

```python
>>> "hola mundo"[:4] # los primeros 4 caracteres, como ya conocemos
"hola"
>>> "hola mundo"[:-1] # todos los caracteres salvo el último
"hola mund"
>>> "hola mundo"[-5:] # los último 5 caracteres
"mundo"
>>> "hola mundo"[0] # primer carácter, como ya conocemos
"h"
>>> "hola mundo"[-1] # último carácter
"o"
>>> "hola mundo"[-2] # anteúltimo carácter
"d"
```

> ¡Pongamos todo lo visto en práctica! Definí:
>
>  * una función `sin_extremos` que tome una lista y devuelva otra igual pero sin su primer y último elemento;
>  * una función `extremos` que haga exactamente lo contrario, es decir, tome una lista y devuelva otra con solamente el primer y último elemento.
>
> ```python
> >>> sin_extremos([4, 5, 10, 2, 3])
> [5, 10, 2]
> >>> extremos([4, 5, 10, 2, 3])
> [4, 3]
> ```



### Pistas

En `extremos` no va a alcanzar con sólo extraer segmentos o acceder por indices: vas a tener que de alguna forma crear una nueva lista especificando sus elementos. 🤔



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
>>> sin_extremos([4, 5, 10, 2, 3])
[5, 10, 2]
>>> sin_extremos([4, 5, 10, 2, 3, 9])
[5, 10, 2, 3]
>>> sin_extremos([4, 5, 10])
[5]
>>> sin_extremos([40, 20])
[]
>>> extremos([4, 5, 10, 2, 3])
[4, 3]
>>> extremos([4, 3])
[4, 3]
>>> extremos([1, 2, 5])
[1, 5]
```

## 4. Textos impresos

🛑 Antes de continuar vamos a hacer un alto en el camino para ver <del>una vaca 🐄</del> otra payada:

```python
payada_de_la_vaca = """
Dígame usted compañero
y conteste con prudencia
Cual es la mansa paciencia
que puebla nuestras praderas
Y en melancólica espera
con abnegada paciencia
Nos da alimento y abrigo
Fingiendo indiferencia
"""
```

¿Tres comillas? ¿Es un error de tipeo? ¡No! En Python podemos escribir textos de _varias líneas_ si los colocamos entre triples comillas dobles 🕶️. Si bien esto funciona muy bien, tiene un pequeño problema: cuando queramos verlo en la consola, aparecerán unos muy peculiares `\n`:

```python
>>> payada_de_la_vaca
'\nDígame usted compañero\ny conteste con prudencia\nCual es la mansa paciencia\nque puebla nuestras praderas\nY en melancólica espera \ncon abnegada paciencia\nNos da alimento y abrigo\nFingiendo indiferencia\n'
```

Este `\n`, llamado _salto de línea_, **representa**  que allí, antes del siguiente carácter, debe haber un enter `↵`. Perfecto, pero ¿y si queremos "escribir" el texto en la pantalla, con verdaderos enters en lugar de estos `\n`? Démosle la bienvenida al procedimiento `print`, que imprime los textos tal como queremos que se vean:

```python
> print(payada_de_la_vaca)

Dígame usted compañero
y conteste con prudencia
Cual es la mansa paciencia
que puebla nuestras praderas
Y en melancólica espera
con abnegada paciencia
Nos da alimento y abrigo
Fingiendo indiferencia
```

> ¿Y qué pasará si usamos print con string que no contienen saltos de lína? ¿Y si imprimimos otros tipos de datos? Averigualo probando lo siguiente y comparando resultados:
>
> ```python
> >>> 5
> >>> print(5)
> >>> [1, 2, 3]
> >>> print([1, 2, 3])
> >>> "a la voz de aura"
> >>> print("a la voz de aura")
> ```


### Para pensar

Como vemos, `print` imprime el pantalla el valor recibido y funciona con listas, strings, y... casi cualquier tipo de dato. Y como todo buen procedimiento, ¡no devuelve nada!

Por otro lado, cuando estamos en la consola los resultados son apenas diferentes cuando usamos strings. Por eso es que no fue necesario... hasta ahora.  😛

## 5. De visita

_¡Y llegamos al plato fuerte de la lección 🍝!_

De todas las cosas interesantes que podemos hacer con las secuencias de cosas, probablemente la más poderosa sea la de _recorrer_ **cada uno** de sus elementos 🚶, utilizando la estructura de control `for`:

```python
def imprimir_cada_elemento(elementos):
  for elemento in elementos:
    print(elemento)
```

Esta estructura de control nos permitirá...

> ...no, mejor no te contamos qué hace exactamente `for` 😈. Descubrilo probando el **procedimiento** `imprimir_cada_elemento` en la consola:
>
> ```python
> >>> imprimir_cada_elemento(["Violeta", "Mercedes", "Natalia", "Charo", "María Elena"])
> >>> imprimir_cada_elemento([True, False, False, True])
> >>> imprimir_cada_elemento("adivinador")
> >>> imprimir_cada_elemento(range(1, 10))    # range en inglés significa rango
> >>> imprimir_cada_elemento(range(5, 30, 2)) # prestá atención al tercer argumento de range
> ```
>
> Cuando termines, escribí `listo()`



### Pistas

No olvides que los procedimientos no devuelven nada. Esto significa que ni `print` ni `imprimir_cada_elemento` están retornando valores, sino que sólo los están imprimiendo.


Ah, ¿y qué hace `range`? También te lo dejamos a vos para que lo descubras 😇



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
def imprimir_cada_elemento(elementos):
  for elemento in elementos:
    print(elemento)


def listo():
  pass

>>> True
True
```



### Para pensar

¡Acaban de pasar varias cosas! Primero, han entrado en escena los _rangos_, que son otro tipo de dato de Python que representa una secuencia de números, que puede ser:

* continua, como en `range(1, 10)`, que no es nada más y nada menos que la secuencia de los números del `1` al `9` (sí, el último no entra ❗)
* con saltos, como en `range(0, 10, 3)`, que son los números del `0` al `9` dando saltos de a 3: `0`, `3`, `6`, `9`

Por otro lado, acabamos de ver también que el `for ... in` nos permite "visitar" a cada elemento de una lista, string o rango de números, y hacer algo con éste. Para ello, esta estructura tiene tres partes:

 1. `in` nos permite especificar qué secuencia de elementos vamos a recorrer;
 2. `for` nos permite elegir un nombre con el que nos referiremos a cada elemento de la secuencia;
 3. y después del `:` tendremos una o más acciones que ejecutaremos al visitar cada elemento. ⚠️ ¡Cuidado! Tienen que estar tabuladas respecto de la línea del `for`


En este caso, en `imprimir_cada_elemento` elegimos:

 1. recorrer cada elemento del parámetro `elementos`:
 2. llamar a cada uno de esos elementos `elemento`;
 3. imprimir cada uno de esos elementos usando `print`.


Muy interesante, pero no parece que hayamos hecho nada muy útil 😕. ¿Podremos hacer cosas más que sólo mostrar elementos?



## 6. Contalo vos

Veamos ahora una nueva `operacion_misteriosa`:

```python
def operacion_misteriosa(elementos):
  cantidad = 0

  for elemento in elementos:
    cantidad += 1

  return cantidad
```

¿Qué hace? ¿Qué devuelve? ¿Te recuerda a algo conocido? ¿Tiene algo que llama la atención?

> 😵 ¡Muchas preguntas! ¡Marcá todas las opciones que creas correctas!





### Pistas

💡 Recordá que `cantidad += 1` es lo mismo que escribir `cantidad = cantidad + 1`. En otras palabras, estamos _actualizando_ la variable local `cantidad`, incrementádola de a uno en uno.



1. 🔲 `operacion_misteriosa` es una función, porque devuelve algo
1. 🔲 `operacion_misteriosa` es un procedimiento, porque no devuelve nada
1. 🔲 `operacion_misteriosa` visita cada elemento de `elementos`, e incrementa `cantidad` en `1` por cada uno
1. 🔲 `operacion_misteriosa` inicializa una variable local `cantidad` en `0`
1. 🔲 `operacion_misteriosa` inicializa una variable global `cantidad` en `0`
1. 🔲 `operacion_misteriosa` hace lo mismo que la función `len`
1. 🔲 `operacion_misteriosa` no usa la variable `elemento`

### Respuesta

<details>
<summary>👀 Ver</summary>

1. ☑️ `operacion_misteriosa` es una función, porque devuelve algo
1. ❎ `operacion_misteriosa` es un procedimiento, porque no devuelve nada
1. ☑️ `operacion_misteriosa` visita cada elemento de `elementos`, e incrementa `cantidad` en `1` por cada uno
1. ☑️ `operacion_misteriosa` inicializa una variable local `cantidad` en `0`
1. ❎ `operacion_misteriosa` inicializa una variable global `cantidad` en `0`
1. ☑️ `operacion_misteriosa` hace lo mismo que la función `len`
1. ☑️ `operacion_misteriosa` no usa la variable `elemento`

</details>

### Para pensar

`operacion_misteriosa` hace exactamente lo mismo que la función `len`: cuenta la cantidad de elementos en una secuencia 😄. Además empieza a darnos una idea de lo poderoso que es combinar _variables locales_ con la estructura `for`.

Y eso que aún no usamos realmente a cada `elemento`. 🤭


## 7. Todo suma

Las cosas se ponen aún más interesantes cuando combinamos todo lo anterior. Por ejemplo, esta función `sumatoria`...

```python
def sumatoria(numeros):
  suma = 0

  for numero in numeros:
    suma += numero

  return suma
```

... calcula la suma de todos los elementos de una lista de números...

```python
>>> sumatoria([10, 5, 20])
35 # porque es 10 + 5 + 20
>>> sumatoria([])
0 # porque la sumatoria de una lista vacía es 0

```

...o incluso de un rango:

```python
>>> sumatoria(range(1, 6))
15 # porque es 1 + 2 + 3 + 4 + 5
```

> Veamos si va entendiendo: completá la definición de la función `productoria` que, al igual que `sumatoria`, toma una secuencia de números, pero en lugar de sumarlos a todos, los multiplica:
>
> ```python
> productoria([10, 2, 3])
> 60 # porque es 10 * 2 * 3
> productoria([3, 3, 2, 4])
> 72 # porque es 3 * 3 * 2 * 4
> productoria([8])
> 8 # porque la productoria de un número es ese mismo número
> productoria([])
> 1 # porque la productoria de un una lista vacía es 1
> ```
>








### Pistas

¿Con cuanto deberás inicializar la variable local en la que acumularás los resultados? ¿También con `0` o te convendrá otro valor?



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
>>> productoria([10, 2, 3])
60
>>> productoria([3, 3, 2, 4])
72
>>> productoria([8])
8
>>> productoria(range(1, 10))
362880
>>> productoria([6])
6
>>> productoria([])
1
```



### Para pensar

¡Bien! 👏 Si bien la función `productoria` no existe en Python, sí existe la función `sum` que calcula una sumatoria tal como vimos acá.

Lo que tienen estas dos funciones en común (y casi todas las que veremos a continuación) es que se basan en la estructura de un _acumulador_: una variable local que **inicializamos con un valor de base**, y cada vez que visitemos un elemento, **la actualizaremos**. Y al final, **retornaremos ese resultado acumulado**.

## 8. Todos los días un poco

_¡Pero el `for` no se trata sólo de números! Por ejemplo también podríamos utilizarlo para acumular un resultado booleano._ 😮

Agus quiere saber si en alguna de sus últimas marcas de natacion 🏊 superó su objetivo personal de 3 minutos:

```python
>>> alguna_vez_supero_objetivo([3.2, 3.4, 3.01, 3.08])
False # todas sus marcas fueron de más de 3 minutos
>>> alguna_vez_supero_objetivo([3.1, 3.2, 2.9, 3.1])
True  # una de sus marcas (2.9) fue menor a 3 minutos
```

Y para eso definió la siguiente función:

```python
def alguna_vez_supero_objetivo(duraciones):
  supero = False # en principio, no se superó la marca de 3 minutos

  for duracion in duraciones:
    supero = supero or duracion < 3 # pero si alguna de ellas es menor a 3 minutos,
                                    # entonces sí la habrá superado

  return supero
```

Como vemos, acá la variable local que estamos usando de _acumulador_ es booleana, y en cada _iteración_ (es decir, cada vez que visitamos una `duracion`) actualizaremos su valor, para saber si esta `duracion` o alguna de las anteriores fue menor a 3.


> ¡Ahora te toca a vos! Dani tampoco quiere perder la práctica diaria de fútbol ⚽ y necesita una función `todos_los_dias_un_poco` que reciba una lista con cuántos minutos practicó cada cada día, y retorne si su práctica diaria fue siempre mayor a 30 minutos:
>
>
> ```python
> >>> todos_los_dias_un_poco([35, 40, 32, 60])
> True  # todos los días practicó más de 30 minutos
> >>> todos_los_dias_un_poco([15, 45, 90, 0])
> False # un día practicó solo 15 minutos, y otro no practicó nada
>```
>
> Nuevamente, te dejamos el molde de la función para que te sirva como punto de partida.







### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
>>> todos_los_dias_un_poco([35, 40, 32, 60])
True
>>> todos_los_dias_un_poco([15, 45, 90, 0])
False
```

## 9. Juntando todo

_Y por supuesto, también podemos usar el `for` con listas de strings_

> Definí la función `juntar` que tome por parámetro una lista de strings y los una de la siguiente forma:
>
> ```python
> >>> juntar(["super", "califragilistico", "espialidoso"])
> "supercalifragilisticoespialidoso"
> >>> juntar(["cuatri", "motor"])
> "cuatrimotor"
> >>> juntar([])
> ""
> ```



### Pistas

Te dejamos como inspiración la definición de `sumatoria` del ejercicio anterior:

```python
def sumatoria(numeros):
  suma = 0

  for numero in numeros:
    suma += numero

  return suma
```



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
>>> juntar(["super", "califragilistico", "espialidoso"])
"supercalifragilisticoespialidoso"
>>> juntar([])
""
>>> juntar(["cuatri", "motor"])
"cuatrimotor"
```

## 10. Juntos pero no tanto

¿Y si ahora quisieramos juntar listas de strings, pero indicando además un _separador_? Por ejemplo:

```python
>>> juntar(" ", ["Nicki", "Nicole"])
"Nicki Nicole"
>>> juntar(",", ["Londra", "Paulo"])
"Londra,Paulo"
>>> juntar("", ["W", "O", "S"])
"WOS" # podemos seguir uniendo sin separadores si pasamos
      # la lista vacía como argumento
```

> ¡Mejoremos nuestra funcion anterior! Modificá `juntar` para que podamos recibir también un separador. El separador es lo que va a ir entre cada string.




### Pistas

💡 Quizás, para evitar que te sobren separadores al principio o al final, te convenga extaer segmentos como vimos al inicio de la lección.

Por otro lado, para hacer las cosas un poco más fáciles, no es necesario que la nueva versión de `juntar` funcione para la lista vacía 😌. Pero si lo hace, ¡mucho mejor 🕶️!



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
>>> juntar("", ["super", "califragilistico", "espialidoso"])
"supercalifragilisticoespialidoso"
>>> juntar("", ["cuatri", "motor"])
"cuatrimotor"
>>> juntar(" ", ["hola", "mundo"])
"hola mundo"
>>> juntar(",", ["hola", "mundo"])
"hola,mundo"
```



### Para pensar

¡Bien! Esta versión final de nuestra función `juntar` también existe en Python, y se llama `str.join` 🤓

## 11. La fama es puro cuento

¡Que suerte que te encontramos, pensábamos que ya te ibas! ¿Podrías quedarte un poco más en esta lección? Es que Agus y Dani nos pidieron les demos una mano para llevar cuenta de sus estadísticas.

Por ahora, para Agus ya definimos esta función...

```python
def cuantas_veces_supero_objetivo(duraciones):
  veces = 0

  for duracion in duraciones:
    if duracion < 3:
      veces += 1

  return veces
```

...que es muy parecida a la que ya habíamos definido, pero tiene una novedad: ahora estamos contando **cuantas veces** se superó el objetivo. Y para eso necesitamos un `if`, con algunas novedades:

  * Por un lado, está dentro del `for`, tabulado, y no retorna nada;
  * por el otro, no tiene `else`: si la condición no se cumple, no hace _nada_.

En otras palabras: en cada iteración, si la condición `duracion < 3` se cumple, el acumulador `veces` se incrementará, y en caso contrario, permanecerá igual.

> Sabiendo esto, ahora ayudemos a Dani a definir `cuantas_veces_entreno_lo_suficiente`, que retorna la cantidad de veces que entrenó más de 30 minutos.
>
> ```python
> >>> cuantas_veces_entreno_lo_suficiente([35, 40, 32, 60])
> 4  # todos los días practicó más de 30 minutos
> >>> cuantas_veces_entreno_lo_suficiente([15, 45, 90, 0])
> 2 # sólo dos días entrenó más de 30 minutos
> ```



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
>>> cuantas_veces_entreno_lo_suficiente([35, 40, 32, 60])
4
>>> cuantas_veces_entreno_lo_suficiente([15, 45, 90, 0])
2
```

## 12. ¿Dónde están las llaves?

Estabamos por proponerte jugar a un conocido juego que consiste en encontrar a un personaje de pulóver blanco y rojo, pero por problemas de copyright vamos a hacer una versión de bajo presupuesto ©️: _¿Dónde están las llaves?_

> Usando lo visto en esta lección, definí la función `donde_estan_las_llaves` que tome un string con emojis y nos diga en qué posición están las llaves, contando desde `1`:
>
> ```python
> >>> donde_estan_las_llaves("🌂🐍🔑👛")
> 3
> >>> donde_estan_las_llaves("🔑🔥👓")
> 1
> >>> donde_estan_las_llaves("🍪🍪🍪🍪🍪🍪🍪🔑🧉")
> 8
> ```
>
> Considerá que las llaves _siempre_ están.






### Pistas

Como podrás ver, los strings pueden tener emojis. Así que los emojis son caracteres, por lo que podemos hacer cosas de este estilo:

``` python
>>> "🍪" == "👓"
False
```




### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
>>> donde_estan_las_llaves("🔑🔥👓")
1
>>> donde_estan_las_llaves("👓🔑🔥")
2
```



### Para pensar

En esta guía aprendiste algo muy importante: cómo hacer que la computadora repita tareas, usando la estructura de control `for`. Además, conociste los segmentos (_slices_), que nos permiten extrar rebanadas de listas y strings, los y rangos, que nos permiten generar números enteros entre otros dos. Y todo esto lo combinamos con el poder de las listas, para agrupar elementos y hacer tareas repetitivas con todos ellos.

Este caldero de conocimientos ya tiene todos los ingredientes de la pócima de la programación... 🧙‍♀️🧙‍♂️

...pero no tan rápido, ¡aún falta uno! 🔮 Acompañanos a la siguiente lección para revelar el misterio de _los diccionarios_.

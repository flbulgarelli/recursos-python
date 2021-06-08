> Basado en https://github.com/mumukiproject/mumuki-guia-python3-hola-python

# ¡Hola Python!

En esta lección conoceremos algunos de los tipos de datos más comunes de Python 🐍 , un lenguaje multipróposito muy usado en la actualidad. También conoceremos a la consola 🖥️ , la herramienta que nos permitirá probar las operaciones que más utilizaremos a lo largo de todo el recorrido.

¡Comencemos! 🤩

## 1. El sentido de Python

Python es un lenguaje creado a fines de los 80 y publicado por primera vez en 1991. Lo desarrolló Guido van Rosum y, si bien tuvo sus momentos de auge y declinación, resurgió gracias a su uso extendido en el ámbito de ciencia de datos. 🔍

> ¿En qué crees que está inspirado su nombre? 🤔

1. 🔲 En el lenguaje de programación _Cobra_.
1. 🔲 En los humoristas británicos _Monty Python_.
1. 🔲 En la picadura de serpiente que sufrió el creador.

### Respuesta

<details>
<summary>👀 Ver</summary>

1. ❎ En el lenguaje de programación _Cobra_.
1. ☑️ En los humoristas británicos _Monty Python_.
1. ❎ En la picadura de serpiente que sufrió el creador.

</details>

### Para pensar

El lenguaje de programación Cobra existe, pero es muy posterior a Python. Por otro lado, no sabemos si hubo una picadura de serpiente 😛, pero el motivo oficialmente reconocido es el show de Monty Python. 😂


## 2. Calculo que sí

Una de las tantas cosas que podemos hacer con Python es cálculos matemáticos. Aunque suene medio aburrido,  😴 aprender a hacer estos cálculos nos va a ayudar después a trabajar sobre otros tipos de datos. 🤩

Para estos cálculos usaremos la *consola*, una herramienta muy útil para hacer pruebas rápidas sobre lo que estás haciendo. La podés reconocer fácilmente porque arranca con el chirimbolito `>>>`, que se llama _[prompt](https://es.wikipedia.org/wiki/Prompt)_.

> ¡Empecemos a probar! Escribí al lado del >>> lo siguiente:
>
> ```python
> >> 2 * 3
> >> 8 + 7
> >> 21 / 7
> >> 11 - 2
> ```
>
> Luego de cada cálculo presioná enter y observá que muestra en la pantalla.


## 3. #Comentario

Si bien ahora nos acostumbramos a ver el `#` en redes sociales 👥, también es lo que vamos a utilizar para hacer comentarios en nuestro código. Es que cuando programamos, a veces queremos hacer aclaraciones. 😅

> Probá esto en la consola...
>
> ```python
> >>> 2 * 3 #¿Esto será 6 o llueve?`
> ```
>
> ... y pensá: ¿cambió en algo el resultado?


### Para pensar

¡Lo ignoró! 😖

Eso está bien, los comentarios son para quienes programan, sirven para comunicarnos o para recordarnos cosas a futuro. 🧠


## 4. ¡Cuántos chirimbolos!

Como acabamos de ver en Python podemos multiplicar ✖️ y dividir ➗, y como te imaginarás, también sumar   ➕  y restar , ➖. En programación a estos chirimbolos se los llaman _operadores_ y se escriben ligeramente diferentes:

|Operación	     | Operador  | Ejemplo  |
|-------------	 |----------	|-------  |
|  Suma           | `+`       | `4 + 9`  |
|  Resta          | `-`       | `12 - 2` |
|  Multiplicación | `*`       | `2 * 3`  |
|  División       | `/`       | `16 / 2` |

Genial 🎉 , entonces ¿la consola nos permite hacer cualquier cálculo? 🤔

> Probá en la consola:
>
> `>>> 8 / 0`
>
> y fijate que pasa. 😬



### Para pensar

_¿Qué pasó?_ 😱

¡Nada grave! Esa es la manera en que veremos los errores en la consola. En este caso fue porque no podemos dividir por 0. 😅

## 5. No todo es un chirimbolo

 Por suerte no todas las operaciones que podemos hacer son con chirimbolos. Además de los operadores matemáticos `+`, `-`, `/` y `*`, existen otras operaciones matemáticas comunes, algunas de las cuales ya vienen con Python y están listas para ser usadas. 🙌

A diferencia de los operadores que vimos hasta acá, estos funcionan un poco distinto. Les específicamos los valores de entrada, llamados *argumentos*, entre paréntesis y a partir de ellos nos da un valor de salida, conocido como *retorno*.

> Probá en la consola las siguientes operaciones y fijate qué devuelve, o retorna, cada una:
>
``` python
>>> abs(-123)
>>> round(4.3)
>>> max(8, 7)
>>> min(8, 7)
```
> ¿Qué pasará si hacemos `abs` con un número positivo?¿ `round(4.6)`  dará lo mismo?
>
> Si no descubrís qué hace cada una, podés probar con otros valores.



### Para pensar

Formalicemos qué hacen estas operaciones antes de continuar 😉 :

* `abs`: nos dice el [valor absoluto](https://es.wikipedia.org/wiki/Valor_absoluto) de un número;
* `round`: nos devuelve el redondeo de un número;
* `max`: a partir de dos números nos dice cuál es el mayor;
* `min`: parecido a `max` pero nos retorna el menor.

## 6. No todo es un número

Pero los operadores no solo nos sirven para obtener números a partir de otros, ¡también podemos compararlos! 💪

> Probá lo siguiente en la consola:
>
``` python
>>> 10 > 9
>>> 11 >= 11
>>> 87 < 87
>>> 87 <= 100
>>> 9 == 9
>>> 8 != 8
```
> ¿Qué crees que devolverán? ¿Será un número? 🤔




### Para pensar

Como podés ver, estos operadores no devuelven números sino `True` o `False`, (verdadero y falso en inglés respectivamente). Ete nuevo tipo de dato se llama *booleano*. Vamos al siguiente ejercicio a conocer otro tipo más. 🕶️

## 7. Palabras, solo palabras

Ya conocimos a los números y a los booleanos de Python, ¡pero eso no es todo!

Muchas veces queremos escribir programas que trabajen con texto 📄: queremos saber cuántas palabras hay en un libro, o convertir minúsculas a mayúsculas, o saber en qué parte de un texto está otro.

Para este tipo de problemas tenemos los _strings_, también llamados _cadenas de caracteres_:

* `"En 15 minutos estoy"`
* `'El hierro nos ayuda a jugar'`
* `"¡Hola Miguel!"`

Como se observa, todos los strings están encerrados entre comillas simples o dobles. ¡Da igual usar unas u otras! Pero sé consistente: por ejemplo, si abriste comilla doble, tenés que cerrar comilla doble. Además, un string puede estar formado por (casi) cualquier carácter: letras, números, símbolos, espacios, etc.

¿Y qué podemos hacer con los strings? Por ejemplo, compararlos, como a cualquier otro valor:

```python
>>> "hola" == "Hola"
False

>>> "todo el mundo" == "todo el mundo"
True
```

y también concatenarlos, es decir, obtener un string a partir de la unión de otros. ⛓️

> Probá en la consola lo siguiente:
>
> ``` python
> >>> "guarda" + "polvos"
> >>> "Hola, " + "¿cómo estás?"
> >>> "Dame " + str(5)
> >>> 'Mari' + 'posa'
> ```



### Para pensar

¡Genial! 😁

Si te estás preguntando qué es ese `str`, es la manera que tenemos de convertir números a strings. Si no lo hacemos y escribimos...

``` python
>>> "Dame " + 5
```

... nos daría un error que diría `can only concatenate str (not "int") to str`. En otras palabras, que los strings solo se pueden concatenar con otros strings. 🤷

## 8. Yo soy parte

Cuando trabajamos con _strings_ también podemos saber si uno contiene a otro utilizando el operador `in`. 👇

> Para verlo en práctica, escribí lo siguiente en la consola:
>
> ``` python
> >>> "amor" in "celos"
> >>> "placer" in "dolor"
> >>> "historia" in "prehistoria"
> ```



### Para pensar

Resumiendo, no hay amor en los celos ni placer en el dolor ¡pero si historia en la prehistoria! 🦖 🦕

Fuera del juego de palabras, `in` se puede utilizar con textos más largos. Por ejemplo:

```python
>>> "protección de las leyes" in "El trabajo en sus diversas formas gozará de la protección de las leyes, las que asegurarán..."
True
```


## 9. De principio a fin

Como vimos, `in` nos puede decir si un string está incluído en otro. Hay dos casos particulares de esta operación: cuando un string comienza, o termina, con otro.

La sintaxis de estas operaciones es _apenitas_ 👌 diferente de lo que venimos haciendo: hay que prefijarlas con `str.`. Por ejemplo, la operación que devuelve si un `string` comienza con otro es `str.startswith`, mientras que la que nos dice si termina con otro es `str.endswith`. 👀

> Probalas en la consola escribiendo:
>
> ``` python
> >>> str.startswith("Fundación e imperio", "Fundación")
> >>> str.endswith("Bueno, y sí", "y sí")
> >>> str.endswith("Hola, ¿qué tal?", "Hola")
> ```

## 10. ¿Cuánto mide?

Muchas veces nos va a interesar saber el largo de un string, o en otras palabras, cuántos caracteres tiene 📏 . Para esto nos va a ayudar `len`. 🤩

> Veámoslo funcionando en la consola probando:
>
> ``` python
> >>> len('prosopopeya')
> >>> len("Buenos días a todo el mundo")
> >>> len('¿No tenés 5 minutos?')
> ```
> ¿Te animás a pensar qué va a devolver cada caso antes de probarlo?



### Para pensar

¡Un momento! 🤨

¿Por qué la última consulta retorno `20` si solo tiene 14 letras? 🧐

Es que como te contamos, `len` nos dice la cantidad de caracteres. Los caracteres son tanto las letras como los espacios, números y carácteres especiales (`.`, `?`, `&`, `/`, etc.)

## 11. ¡A mí no me grités!

🗣️ QUE AGRESIVAS LAS MAYÚSCULAS, ¿NO? ¡NI HABLAR SI LES AGREGAMOS SIGNOS DE EXCLAMACIÓN!

Por suerte en la contracara tenemos a las calmas minúsculas. En Python podemos pasar un texto en mayúsculas a minúsculas y viceversa. También podemos sacar los espacios que tenga un string al principio o al final, dado que hay veces que no nos interesan. 🤷

> Probemos `str.strip`, `str.upper` y `str.lower` en la consola:
>
> ```python
> >>> str.strip("    ¿Por qué tantos espacios?       ")
> >>> str.lower('BAJÁ EL VOLUMEN')
> >>> str.lower('ya bajamos el volumen')
> >>> str.upper('¡Ahora sí!')
> >>> str.upper('NECESITO MAYÚSCULAS MÁS GRANDES')
> ```
> ¿Te imaginás qué va a pasar en cada caso?



### Para pensar

¡Cuántas cosas podemos hacer con los strings! Y eso no es todo, pero con estas operaciones estamos por ahora. 😅

## 12. No olvidemos los booleanos

Ya estuvimos probando operaciones de números y de strings, ¿los booleanos se podrán operar? 💭

¡Sí! Una de las operaciones más comunes es la conjunción lógica, "Y lógico" o simplemente `and`. 😌

> Probá lo siguiente en la consola:
>
> ``` python
> >>> len("hola") == len("chau") and len("blanco") == len("negro")
> >>> 8 < 10 and 8 > 9
> >>> str.startswith("caracol", "cara") and str.endswith("caracol", "col")
> ```
> Fijate si detectas algún patrón.



### Para pensar

¿Descubriste el patrón? 😬

Para que `and` retorne `True` es necesario que ambas condiciones sean verdaderas. Por eso...

``` python
>>> 8 < 10 and 8 > 9
```

... retorna `False`, porque 8 es menor a 10 pero no es mayor a 9. Dicho de otra forma, `8 < 10` es `True` pero `8 > 9` es `False`. En cambio al probar...

``` python
>>> str.startswith("caracol", "cara") and str.endswith("caracol", "col")
```

... obtenemos `True`, dado que ambas condiciones son verdaderas. En resumen:

```python
>>> False and False
False
>>> True and False
False
>>> False and True
False
>>> True and True
True
```




## 13. Verdadero o falso

Otro famoso operador lógico es el `or` que sirve para realizar disyunciones lógicas. El "O lógico" tiene sus diferencias con el `and`, ¿te animás a descubrirlas? 🤗

> Hacé las siguientes pruebas en la consola:
>
> ``` python
> >>> str.lower("HOLA") == "hola" or str.lower("adiós") == "adiós"
> >>> len("hola") > 5 or abs(-5) == 5
> >>> str.upper("python") == "Python" or "amor" in "romance"
> ```



### Para pensar

 ¿Descubriste las diferencias? 🤓

Dijimos que `and` solo retorna `True` cuando ambos booleanos son `True`. Por el otro lado, para que `or` sea verdadero alcanza con que al menos uno de los booleanos lo sea. Dicho de otra manera, ambas condiciones deben ser falsas para que retorne `False`. Por ejemplo en...

``` python
>>> str.upper("python") == "Python" or "amor" in "romance"
```

... tanto `str.upper("python") == "Python"` como `"amor" in "romance"` devuelven `False`. Si probamos con los booleanos directamente veremos que:

```python
>>> False or False
False
>>> True or False
True
>>> False or True
True
>>> True or True
True
```




## 14. Operando con sentido

 Como acabamos de ver, en Python existen números, booleanos y strings:

|  Tipo de dato |  Representa             |  Ejemplo |  Operaciones                   |
|---------------|-------------------------|----------|--------------------------------|
|Números        |cantidades               | `4947`   | `+`, `-`, `*`, `/`, `<`, etc .  |
|Booleanos      |valores de verdad        | `True`   | `and`, `or`, etc.
|Strings        |texto                    | `"¡hola Python!"` | `str.upper`, `str.startswith`, `len` |


Además, existen operaciones que sirven para todos los _tipos de datos_, por ejemplo:

* `==`: nos dice si dos cosas son iguales;
* `!=`: nos dice si dos cosas son diferentes.

**Es importante usar las operaciones correctas con los tipos de datos correctos**, por ejemplo, no tiene sentido sumar dos booleanos o hacer operaciones booleanas con los números. **Si usas operaciones que no corresponden, cosas muy raras y malas pueden pasar**. 😖

> Probá en la consola lo siguiente:
>
> ``` python
> >>> 5 + 6
> >>> 5 == "5"
> >>> 8 > 6
> >>> False / True
> >>> 'hola' or 'chau'
> ```
> ¿Todas estas operaciones tienen sentido?



### Para pensar

Hablemos de las dos últimas consultas:

* ¿por qué querríamos dividir booleanos?
* ¡`or` no sirve para elegir un string u otro!

Si bien no arrojaron un error no tenían sentido 🤨 . Es por eso que tenemos que tener cuidado con las operaciones que usamos con cada tipo de dato. 🧐

## 15. Un poco de cada tipo

Uff, ¡vimos un montón de cosas! 😅 Aprendimos sobre la sintaxis de las funciones en Python, los _tipos de datos_ y sus operaciones.

¡Pero no tan rápido! 🏃

> Antes de terminar, un último desafío: ¡marcá todas las opciones correctas!


1. 🔲 `4 + 4` vale `8`
1. 🔲 `"4" + "4"` vale `"44"`
1. 🔲 `4 + 4` vale `"44"`
1. 🔲 `"on" + "ce"` vale `"once"`
1. 🔲 `True and False` vale `False`
1. 🔲 `True and False` vale `0`
1. 🔲 `5 >= 6` vale `False`

### Respuesta

<details>
<summary>👀 Ver</summary>

1. ☑️ `4 + 4` vale `8`
1. ☑️ `"4" + "4"` vale `"44"`
1. ❎ `4 + 4` vale `"44"`
1. ☑️ `"on" + "ce"` vale `"once"`
1. ☑️ `True and False` vale `False`
1. ❎ `True and False` vale `0`
1. ☑️ `5 >= 6` vale `False`

</details>

### Para pensar

¡Excelente! 🙌

Ya vimos cómo son los números, los booleanos y los strings de Python. También conocimos a la consola, una poderosa aliada que nos acompañará a lo largo de todo este recorrido. 🤝

Ahora que sabemos algunas operaciones básicas de Python ¡vamos a crear nuestros primeros programas! 💪

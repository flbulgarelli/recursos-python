> Basado en https://github.com/mumukiproject/mumuki-guia-python3-funciones-2021

# Funciones y Parámetros

Si bien ya sabemos usar la consola de Python, con la que podemos dar algunas órdenes sencillas a una computadora, tenemos un pequeño problema con el que quizás ya te topaste: ¿qué pasa cuando queremos dar la misma secuencia de órdenes, una y otra vez? ¿No se vuelve un poco tedioso escribir las mismas instrucciones? ¡Aprendamos a reutilizar de la mano de las funciones y los parámetros!

## 1. La unión hace la fuerza

Cuando programamos es común que las órdenes que vimos anteriormente no sean suficientes por sí solas para resolver un problema. Pero, ¿hay algo que nos impida _combinarlas_? :thinking: ¡Por supuesto que no! :handshake:

Por ejemplo, en Python no hay nada que nos diga si dos textos tienen la misma longitud. Pero podemos averiguarlo combinando `len` con `==`:

```python
>>> len("bombo") == len("guitarra")
False
>>> len("timbal") == len("flauta")
True
```

> ¡Ahora te toca a vos! Averiguá usando la consola si:
>
> * `"Bahía de Samborombón"` es mas largo que `"Sierra Grande"`
> * `"Patagonia"` es más largo que `"Cuyo"`
> * `"Tierra del Fuego"` es más largo que `"Santiago del Estero"`


### Para pensar

¡Lo lograste! Pero, ¿no fue un poco tedioso y repetitivo? :sleeping: Una vez que ya nos dimos cuenta cómo resolver el problema de saber si un string es más largo que otro...

```python
>>> len(un_string) > len(otro_string)
```

...¿no sería genial si pudiéramos _reutilizar_ esta idea? :recycle:


## 2. ¡No te repitas!

Combinar operaciones es muy útil, pero tiene el problema de que ahora tenemos que recordar (o pensar :thought_balloon:) como hacerlo cada vez que lo necesitemos. Esto nos puede llevar a equivocarnos...

```python
# queremos saber si el primero es mas largo que el segundo
>>> len("Santiago del Estero") < len("Misiones")
False # Ups ¡era para el otro lado!
```
...o simplemente a aburrirnos por hacer una y otra vez lo mismo :rolling_eyes:. ¿No sería mucho mejor si pudieramos escribir directamente así?:

```python
>>> es_mas_largo_que("Santiago del Estero", "Misiones")
```

> :octagonal_sign: ¡Momento! ¿Esta _consulta_ que acabamos de mostrar funcionará?
>
> Para averiguarlo, pegá el siguiente código en la consola...
>
> ```python
> def es_mas_largo_que(un_string, otro_string):
>   return len(un_string) > len(otro_string)
> ```
> ... y luego probá la consulta.
>

### Para pensar

¡Ahora sí! Sin errores y mucho más fácil de entender. ¿Pero no habíamos dicho que en Python nada resolvía el problema de saber si un string es mas largo que otro? ¿Qué pasó entonces? ¿Mentimos? ¿Fue magia?

Develemos el misterio...


## 3. Una definición, inifinitos usos

Sí, Python nos da operaciones que nos permites resolver diferentes tareas y además nos permite combinarlas, pero el verdadero poder de la programación es que también podemos crear nuestras propias operaciones.

Y para hacer esto, ¡démosle entonces la bienvenida a _las funciones_ :confetti_ball:! Nuestras nuevas amigas nos permitirán "enseñarle"  a la computadora a realizar una tarea que originalmente no estaba incluida en el lenguaje mediante. ¿Cómo? _Escribiendo una definición_ como la siguiente **una sola vez** :one:...

```python
def es_mas_largo_que(un_string, otro_string):
  return len(un_string) > len(otro_string)
```

...y luego _invocando_ a esta función **cuantas veces queramos** :1234::

```python
>>> es_mas_largo_que("Valle de Uco", "Cerro de los Siete Colores")
False
>>> es_mas_largo_que("Valle de Uco", "Cerro de los Siete Colores")
False # las dos veces devuelve lo mismo
```

¡Y no sólo eso! Cada vez que la invoquemos podremos hacerlo con _argumentos_ diferentes :open_mouth: :

```python
>>> es_mas_largo_que("Rosario", "Bahía Blanca")
False
>>> es_mas_largo_que("Valle de Uco", "La Punta")
True # si los argumentos cambian, el resultado puede ser diferente también
```

> Veamos si se va entendiendo:
>
>  Copiá la _definición_ de la función `es_mas_largo_que` en la consola y luego invocá la función `es_mas_largo_que` varias veces con argumentos diferentes.
>


### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
>>> es_mas_largo_que("Bahía Blanca", "Rosario")
True
>>> es_mas_largo_que("Temperley", "Lomas del Mirador")
False
>>> es_mas_largo_que("San Fernando", "Tigre")
True
```

### Para pensar

Como vemos las funciones tienen un _nombre_ (en este caso `es_mas_largo_que`) que tendremos que _inventar_ al momento de definir la función, y luego escribirlo exactamente igual cada vez que la usemos.

Es muy importante que este nombre sea _expresivo_, es decir, que sea claro y refleje la intención de esa función. Por ejemplo, si la función nos dice si una palabra está escrita en mayúsculas:

* :heavy_check_mark: `esta_en_mayusculas` podría ser un buen nombre;
* :x: `asdf` o `estenmayus` son malos nombres.

¿Pero qué es `def` y `return`? ¿Y esos dos puntos? ¡Estudiemos la sintaxis!



## 4. El juego de los parecidos

Veamos ahora la definición de otra función...

```python
def es_pregunta(oracion):
  return str.startswith(oracion, "¿") and str.endswith(oracion, "?")
```
...la cual podemos usar así:

```python
>>> es_pregunta("¿Qué hora es?")
True
>>> es_pregunta("¡En esta casa obedecemos las leyes de la termodinámica!")
False
```

¿Se parece la definición de esta función a la anterior? ¿Por qué será?

> :mag: Compará esta nueva definición con la que vimos anteriormente...
>
> ```python
> def es_mas_largo_que(un_string, otro_string):
>   return len(un_string) > len(otro_string)
> ```
>
> ...y respondé qué tienen en común.


1. ☐ Ambas empiezan con `def` seguido del nombre de la función
1. ☐ Ambas empiezan con `def` seguido de dos puntos
1. ☐ Ambas tienen un `return` en la primera línea
1. ☐ Ambas tienen un `return` en la última línea
1. ☐ Ambas terminan la primera línea con dos puntos
1. ☐ Ambas arrancan la segunda línea contra el margen

### Respuesta

<details>
<summary>:eyes: Ver</summary>

1. ☑️ Ambas empiezan con `def` seguido del nombre de la función
1. ☒ Ambas empiezan con `def` seguido de dos puntos
1. ☒ Ambas tienen un `return` en la primera línea
1. ☑️ Ambas tienen un `return` en la última línea
1. ☑️ Ambas terminan la primera línea con dos puntos
1. ☒ Ambas arrancan la segunda línea contra el margen


</details>

### Para pensar

¡Bien! Estas semanejanzas no son casuales: ¡para definir funciones hay que seguir algunas reglas _sintácticas_! :straight_ruler:

1. La primera línea, también llamada cabecera:
  1. debe arrancar con la palabra reservada `def` (abreviatura de _definir_ en inglés);
  2. luego, debe ir el nombre de la función;
  3. luego, entre paréntesis y separados por comas, deben ir los _parámetros_ que la función va a tener y que más tarde le permitirán recibir _argumentos_ al invocarla;
  4. y por último,deben finalizar con dos puntos (`:`)
2. Las siguientes líneas (también llamadas _cuerpo_) deben:
  1. empezar tabuladas, es decir, no directamente contra el margen, sino presionando la tecla `Tab ↹`;
  2. la última línea en particular debe empezar además con  `return`, seguido de lo que queremos que devuelva nuestra función.


Uff, ¡muchas reglas :tired_face:! No te preocupes, de a poco las iremos dominando. :smile:




## 5. Funciones que no funcionan

¿Y qué pasa si al definir una función no cumplimos la reglas que acabamos de ver :speak_no_evil:? ¡La computadora se rehusará a aprender la tarea que acabamos de enseñarle!

Esto es lo que se conoce como un _error de sintaxis_, que representaremos mediante el símbolo <i class="fas fa-minus-circle text-broken"></i>. Mientras aprendemos a programar nos toparemos con esta clase de errores muchas veces, ¡pero a no desesperar! Si leemos con paciencia y atención nuestro código podremos resolverlo.

> ¡Veamos si se entiende! Mirá las dos funciones a continuación...
>
> ```python
> Def mitad(un_numero)
> return un_numero / 2
>
> def suma_longitudes un_string, otro_string):
>   return len(un_string) + len(otro_string)
> ```
>
> ...¿están bien escritas? ¡Averigüémoslo!
>
> 1. :arrow_forward: Pegá el código en la consola, y fijate qué pasa;
> 2. :eyes: lee con atención el mensaje que Python te muestra;
> 3. :tools: corregí los errores de sintaxis y volvé a enviar
>

### Pistas

Repasemos las reglas:

1. La cabecera:
  1. debe arrancar con la palabra reservada `def` (sí, en minúscula);
  2. luego, debe ir el nombre de la función;
  3. luego, entre paréntesis, deben ir los _parámetros_;
  4. y por último, dos puntos (`:`)
2. Las líneas del cuerpo deben:
  1. empezar tabuladas usando la tecla `Tab ↹`;
  2. la última línea en particular debe empezar además con  `return`, seguido de lo que queremos devolver


### Autoevaluación

Una vez corregido el código, probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
>>> mitad(2)
1
>>> mitad(20)
10
>>> mitad(10)
5
>>> suma_longitudes("hola", "mundo")
9
>>> suma_longitudes("llueva", "café")
10
```


### Para pensar

¡Muy bien! Quizás habrás notado que cuando Python no puede entender tu código genera mensajes como éstos:

```
  File "<stdin>", line 1, ...
    Def mitad(un_numero)
                       ^
SyntaxError: invalid syntax
```

Aunque resulten un poco crípticos al principio, ¡en realidad son textos muy útiles! En general el símbolo `^` está precisamente donde falta algo (por ejemplo los dos puntos `:`) o justo después de algo que está mal escrito. Eso sí, no siempre es perfecto, tampoco le podemos pedir tanto. :face_with_hand_over_mouth:

Pero ahora que nuestro código anda, te dejamos algo para pensar: ¿Qué devuelve la función `mitad`? ¿Un booleano u otra cosa? ¿Y `suma_longitudes`? Probalo en la consola para sacarte la duda :wink:

## 6. Funciones con agujeritos

Probablemente habrás notado que las funciones que definimos hasta ahora podían devolver tanto números como booleanos. Es más: **pueden devolver cualquier tipo de dato** :exploding_head:. Pero, ¿qué hay de lo que _entra_ a la función? ¿Cuántos argumentos podemos pasarles? ¿Y qué son exactamente los parámetros?

La respuesta es que los parámetros son _...redoble de tambores :drum:..._  ¡pequeños agujeros! :face_with_raised_eyebrow:

Por ejemplo, en esta definición estamos _declarando_ **un** parámetro llamado `un_numero`...

```python
def mitad(un_numero): # un_numero es un parámetro
  return un_numero / 2
```

...que sirve para que `mitad` pueda recibir exactamente **un** argumento:

```python
>>> mitad(4) # 4 es un argumento
2
```

Por ejemplo, cuando invocamos `mitad` con el argumento `4`, a través de este "agujerito" llamado `un_numero` le llegará el valor `4`, que luego nuestra función podrá dividir por dos y retornar su resultado. En cambio, si la invocamos así...


```python
>>> mitad(10) # 10 es otro argumento
5
```

...a través del parámetro `un_numero` llegará a `mitad` el `10` con el que invocamos la función. Y nuevamente, lo dividirá por dos y retornará el `5`.

> ¡Más despacio! Volvamos a la función del ejercicio anterior...
>
> ```python
> def suma_longitudes(un_string, otro_string):
>   return len(un_string) + len(otro_string)
> ```
>
> ... y marcá las opciones correctas.



1. ☐ `suma_longitudes` es una función
1. ☐ `suma_longitudes` tiene dos parámetros
1. ☐ `suma_longitudes` puede ser invocada con 2 argumentos
1. ☐ si escribimos `suma_longitudes("aprendiendo", "programación")`, `"aprendiendo"` será el primer argumento y `"programación"`, el segundo

### Respuesta

<details>
<summary>:eyes: Ver</summary>

1. ☑️ `suma_longitudes` es una función
1. ☑️ `suma_longitudes` tiene dos parámetros
1. ☑️ `suma_longitudes` puede ser invocada con 2 argumentos
1. ☑️ si escribimos `suma_longitudes("aprendiendo", "programación")`, `"aprendiendo"` será el primer argumento y `"programación"`, el segundo

</details>

### Para pensar

¡Exactamente! Todas las opciones son correctas. :ok_hand:

Una función puede _declarar_ tantos parámetros como necesite en su definición; por cada uno de ellos, deberemos pasar un argumento al invocarla. Lo interesante es que no importa qué argumentos utilicemos, ya que a cada uno lo conoceremos con el nombre de su parámetro. En este ejemplo, si escribimos en la consola...

```python
>>> suma_longitudes("aprendiendo", "programación")
```
...dentro de la función `suma_longitudes` el argumento `"aprendiendo"` será `un_string` y `"programación"` será `otro_string`:

```python
def suma_longitudes(un_string, otro_string):
  #                     ▲           ▲
  #              "aprendiendo"  "programación"
  return len(un_string) + len(otro_string)
  #            ▲                  ▲
  #     len("aprendiendo")  len("programación")
```

Sin embargo, si lo invocamos escribiendo...

```python
>>> suma_longitudes("conociendo", "Python")
```

... ahora el parámetro `un_string` tiene como valor `"conociendo"` y `otro_string` _vale_ `"Python"`.

¡Por eso es tan importante darle un buen nombre!

## 7. La hora de la verdad

¡El momento ha llegado! Ahora escribiremos nuestra primera función desde cero.

Pero a no desesperar :scream:: si algo no sale recordá que podés enviar tantas veces como necesites, siempre podés consultar los ejercicios anteriores. ¡Y la ayuda, claro! :wink:


> Definí la función `es_hora_de_la_verdad`, que tome una hora y nos diga si son las `12` y probala en la consola:
>
> ```python
> >>> es_hora_de_la_verdad(0)
> False
> >>> es_hora_de_la_verdad(11)
> False
> >>> es_hora_de_la_verdad(12)
> True
> >>> es_hora_de_la_verdad(23)
> False
> ```
>
> Al terminar, presioná enviar.
>
> Ah, ¿y por qué _la hora de la verdad son las 12_? La verdad, ahora no hay un por qué :stuck_out_tongue_winking_eye:
>





### Pistas

Estas son las funciones que definimos hasta ahora. Te pueden servir de inspiración :art:.


```python
def mitad(un_numero):
  return un_numero / 2

def suma_longitudes(un_string, otro_string):
  return len(un_string) + len(otro_string)

def es_pregunta(oracion):
  return str.startswith(oracion, "¿") and str.endswith(oracion, "?")

def es_mas_largo_que(un_string, otro_string):
  return len(un_string) > len(otro_string)
```





### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
>>> es_hora_de_la_verdad(11)
False
>>> es_hora_de_la_verdad(14)
False
>>> es_hora_de_la_verdad(12)
True
```



### Para pensar

¡Excelente! :tada:

En esta lección estuvimos hablando de la importancia de la expresividad a la hora de elegir nombres para nuestras funciones ¡Esto también aplica a los parámetros!

Si por ejemplo al parámetro de `hora_de_la_verdad` le pusiste `numero`, está bien. Sin embargo, un mejor nombre sería `hora` o `una_hora`, ya que eso es lo que representa :wink::

```python
def es_hora_de_la_verdad(hora):
  return hora == 12
```

## 8. Plan Combo 2.0

¿Y podremos combinar estas funciones al igual que hacíamos con los operadores y funciones que ya venían con Python? ¡Por supuesto! :heart_eyes: En otras palabras, _podemos invocar funciones dentro de definiciones_. Por ejemplo:

```python
def doble(numero):
  return 2 * numero

def siguiente_del_doble(numero):
  return doble(numero) + 1
```

O incluso mejor:

```python
def doble(numero):
  return 2 * numero

def siguiente(numero):
  return numero + 1

def siguiente_del_doble(numero):
  return siguiente(doble(numero))
```

> Veamos si se entiende; definí las siguientes funciones:
>
> * `anterior`: toma un número y devuelve ese número menos uno.
> * `triple`: devuelve el triple de un número.
> * `anterior_del_triple`, que combina las dos funciones anteriores: multiplica a un número por 3 y le resta 1.
>




### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
>>> anterior(1)
0
>>> anterior(10)
9
>>> triple(1)
3
>>> triple(3)
9
>>> anterior_del_triple(1)
2
>>> anterior_del_triple(3)
8
>>> anterior_del_triple(10)
29
```

## 9. Libros de la buena memoria

¡Definamos más funciones! :writing_hand: Dani ama el primer dia de cada mes :date:, y por eso definió esta función...

```python
def es_dia_favorito(dia_del_mes):
  return dia_del_mes == 1
```

...y la usa así (_y la dejó en la biblioteca para que la pruebes_):

```python
>>> es_dia_favorito(13)
False
>>> es_dia_favorito(1)
True
```

> ¡Ahora te toca a vos! Dani también dice que a alguien `le_gusta_leer`, cuando la cantidad de libros que recuerda haber leído es mayor a 20. Por ejemplo:
>
> ```python
> >>> le_gusta_leer(15)
> False
>
> >>> le_gusta_leer(45)
> True
> ```
>
> Definí y probá en la consola la función `le_gusta_leer`.






### Pistas

Como vimos anteriormente, en Python contamos con operadores como `>=`, `>`, `<`,`<=` que nos dicen si dos valores son  mayores-o-iguales, mayores, menores, etc. Los vamos a usar bastante :grin:.



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
def es_dia_favorito(dia_del_mes):
  return dia_del_mes == 1

>>> le_gusta_leer(25)
True
>>> le_gusta_leer(80)
True
>>> le_gusta_leer(1)
False
>>> le_gusta_leer(15)
False
```



### Para pensar

¡Muy bien! :clap:

Aunque sonemos un poco insistentes :rolling_eyes:, no te olvides de poner buenos nombres a tus parámetros. Por ejemplo, `libros` o `cantidad_de_libros` son mejores que `cantidad` o `numero`:

```python
def le_gusta_leer(cantidad_de_libros):
  return cantidad_de_libros > 20
```

## 10. Entre los números y la pared

¡Hagamos un breve repaso de los booleanos antes de continuar!

* Se puede hacer la conjunción lógica entre dos booleanos (_y lógico_), mediante el operador `and`. Por ejemplo: `esta_lloviendo and hace_calor`
* Se puede hacer la disyunción lógica entre dos booleanos (_o lógico_), mediante el operador `or` haciendo `es_verano or es_primavera`

Y además de estos dos operadores, contamos con un tercero: el operador de negación `not`, que convierte al `True` en `False` y viceversa:

```python
>>> not True
False
>>> not False
True
```

> ¡A practicar! :muscle: Definí las siguientes funciones:
>
> * `esta_entre`, que tome tres números y diga si el primero es mayor al segundo y menor al tercero.
> * `esta_fuera_de_rango`: que tome tres números y diga si el primero es menor al segundo o mayor al tercero
>
> ```python
> >>> esta_entre(3, 1, 10)
> True
> >>> esta_entre(90, 1, 10)
> False
> >>> esta_entre(10, 1, 10)
> False
> >>> esta_fuera_de_rango(17, 1, 10)
> True
> ```
>




### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
>>> esta_entre(10, 1, 10)
False
>>> esta_entre(4, 4, 9)
False
>>> esta_entre(12, 1, 10)
False
>>> esta_entre(200, 54, 112)
False
>>> esta_entre(67, 0, 100)
True
>>> esta_entre(2, 0, 100)
True
>>> esta_fuera_de_rango(0, 1, 10)
True
>>> esta_fuera_de_rango(12, 1, 10)
True
>>> esta_fuera_de_rango(200, 54, 112)
True
>>> esta_fuera_de_rango(67, 0, 100)
False
>>> esta_fuera_de_rango(2, 0, 100)
False
```



### Para pensar

¡Bien hecho!

Ya fueron suficientes números y booleanos por ahora, ¿no? Exploremos algo más interesante: los `string`s.

## 11. Un string no es parámetro

Como vimos, un string puede ser pasado como argumento a una función...

```python
>>> es_biblioteca("Biblioteca De Babel")
True
>>> es_biblioteca("Biblioteca Del Congreso")
True
>>> es_biblioteca("Teatro Colón")
False
```

...y además, las funciones pueden tener parámetros, uno por cada argumento que necesite recibir.

> ¡Momento! ¿Tendremos que escribir de forma diferente nuestros parámetros cuando _son de tipo_ string? :thinking:
>
> Por ejemplo, observá la siguiente definición de `es_biblioteca`...
>
> ```python
> def es_biblioteca("lugar"):
>  return "biblioteca" in "lugar"
> ```
> ...¿está bien escrita? :eyes:



1. ☐ Si, porque en la función `es_biblioteca`, `lugar` es un parámetro de tipo string y debemos indicarlo colocándolo entre comillas
1. ☐ No, porque en la función `es_biblioteca`, `lugar` es un parámetro de tipo string, pero los parámetros son nombres que no van entre comillas

### Respuesta

<details>
<summary>:eyes: Ver</summary>

1. ☒ Si, porque en la función `es_biblioteca`, `lugar` es un parámetro de tipo string y debemos indicarlo colocándolo entre comillas
1. ☑️ No, porque en la función `es_biblioteca`, `lugar` es un parámetro de tipo string, pero los parámetros son nombres que no van entre comillas

</details>

### Para pensar

¡Bien! Los parámetros son simplemente identificadores, que se escriben sin comillas y pueden servirnos para recibir argumentos de cualquier tipo. Por lo tanto, la forma de escribir esta función es la siguiente:

```python
def es_biblioteca(lugar):
  return "biblioteca" in lugar
```


## 12. Nombres completos

¡Practiquemos lo visto!

> Definí una función `longitud_nombre_completo`, que tome un nombre y un apellido, y devuelva su longitud total, **contando un espacio extra** para separar a ambos:
>
>```python
> >>> longitud_nombre_completo("Cosme", "Fulanito")
>14
>```




### Pistas

Recordá que podemos averiguar el largo de los strings mediante `len`...

```python
>>> len("biblioteca")
10
>>> len("babel")
5
```

...y también podemos _concatenarlos_, es decir, obtener **uno nuevo** que junta dos strings:

```python
>>> "aa" + "bb"
"aabb"
>>> "sus anaqueles " + "registran todas las combinaciones"
"sus anaqueles registran todas las combinaciones"
```




### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
>>> longitud_nombre_completo("Cosme", "Fulanito")
14
>>> longitud_nombre_completo("John", "Snow")
9
>>> longitud_nombre_completo("Juana", "Azurduy")
13
```

## 13. ¡GRITAR!

Una conocida banda, para agregar gritos varios a su canción, nos pidió que desarrollemos una función `gritar`, que tome un string y lo devuelva en mayúsculas y entre signos de exclamación.

Por ejemplo:

```python
>>> gritar("miguel")
"¡MIGUEL!"
```

> Definí la función `gritar`. Recordá la función `str.upper` que convierte en mayúsculas un string.




### Pistas

Tené en cuenta que los signos de admiración `"¡"` y `"!"` (al igual que los espacios y otros signos de puntuación) son strings y que los strings se pueden concatenar usando el operador `+`.

Por ejemplo:

```python
>>> "todo" + "terreno"
"todoterreno"

>>> "¿" + "Aló" + "?"
"¿Aló?"
```





### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
>>> gritar("miguel")
"¡MIGUEL!"
>>> gritar("gritar")
"¡GRITAR!"
>>> gritar("minuto")
"¡MINUTO!"
```

## 14. Terminando la semana

Ya falta poco para el fin de semana :beach:... ¡o al menos el fin de esta lección! Terminemos combinando todo lo visto :eyes:.

> Definí la función `es_fin_de_semana` que tome un string que represente el nombre de un día de la semana, y nos diga si es `"sábado"` o `"domingo"`:
>
> ```python
> >>> es_fin_de_semana("sábado")
> True
> >>> es_fin_de_semana("martes")
> False
> ```





### Pistas

Para saber si un día es fin de semana, _ese día tiene que ser `"sábado"` o ese día tiene que ser `"domingo"`_. Recordá que el "o lógico" opera booleanos, no strings. :eyes:



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
>>> es_fin_de_semana("sábado") or es_fin_de_semana("sabado")
True
>>> es_fin_de_semana("domingo")
True
>>> es_fin_de_semana("lunes")
False
>>> es_fin_de_semana("viernes")
False
```


### Para pensar

¡Felicitaciones! :tada:

En esta lección aprendiste a definir funciones que, a partir de su reutilización, nos ayudan a evitar la repetición de lógica. También viste la diferencia entre parámetros y argumentos, elementos esenciales para poder hacer lo mismo con distintos valores. :raised_hands:

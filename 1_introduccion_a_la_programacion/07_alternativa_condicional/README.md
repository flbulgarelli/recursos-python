> Basado en https://github.com/mumukiproject/mumuki-guia-python3-alternativa-condicional-2021

# Alternativa Condicional

Hasta ahora, todas las funciones que hicimos sabían con bastante precisión qué iban a recibir y siempre hacían exactamente lo mismo: operar dos o más strings, hacer una cuenta, evaluar una expresión booleana, y así.

Pero en esta lección nos introduciremos en el mundo de lo desconocido, donde la programación cobra aún mucho más sentido. Con la herramienta que veremos podremos resolver problemas nuevos y evitar errores que hasta ahora no podíamos: según lo que recibamos, podremos hacer cuentas diferentes, transformar a nuestros strings de formas distintas, y así.

¿Y cómo haremos esto? Utilizando la capacidad de la computadora para **tomar decisiones**: la _alternativa condicional_ o sentencia `if`.


## 1. Empezando el día

Acaba de empezar el día :sunrise: y ya tenemos que hacer una nueva función :sleeping:.

> Definí la función `saludar_a` que tome un nombre y salude a la persona con un clásico _Buenos días_:
>
> ```python
> >>> saludar_a("May")
> "Buenos días May"
> >>> saludar_a("Gus")
> "Buenos días Gus"
> ```



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
>>> saludar_a("Gus")
"Buenos días Gus"
>>> saludar_a("May")
"Buenos días May"
```



### Para pensar

¡Buenos días a vos también! Hmm...¿o serán buenas noches? :full_moon:

## 2. Hora de tomar una decisión

En realidad no siempre saludamos con _buenos días_: por ejemplo, pasadas ciertas horas decimos _buenas noches_. :night_with_stars:

Por eso, ahora nos gustaría modificar nuestra función `saludar_a` para que tome un parámetro adicional, `horario`, y retorne un saludo diferente según éste:

```python
>>> saludar_a("Dani", 10)
"Buenos días Dani"
>>> saludar_a("Feli", 22)
"Buenas noches Feli"
```

¿Pero cómo podríamos lograr esto? Ninguna introducción al lenguaje Python estaría completa sin mostrar _la estructura de control_ más famosa de la programación: ¡la alternativa condicional!

```python
def saludar_a(quien, horario):
  if horario < 19:
    return "Buenos días " + quien
  else:
    return "Buenas noches " + quien
```

> :hourglass_flowing_sand: Tomate uno minutos para leer este `if` e intentar entender qué está pasando acá. Y después probá en la consola lo siguiente:
>
>  1. saludá a `"Juli"` a las `18`
>  2. saludá a `"Pun Pun"` a las `19`
>
> ¿Sucede lo que esperabas? :thinking:




### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
def saludar_a(quien, horario):
  if horario < 19:
    return "Buenos días " + quien
  else:
    return "Buenas noches " + quien

>>> True
True
```



### Para pensar

En programación decimos que el `if` es _una estructura de control_ porque permite controlar el flujo de ejecución: ejecuta una cosa u otra dependiendo de una condición. En particular, el ejemplo anterior lo podemos leer como:

* _si (`if`) el horario es **menor** a 19, entonces devolver buenos dias concatenado con el nombre_;
* _si no (`else`), devolver buenas noches concatenado con el nombre_;


Por eso es que:

* cuando saludamos a Juli a las 18 se ejecuta `return "Buenos días " + quien`;
* pero cuando saludamos a Pun Pun a las 19 horas (ojo :eye:, 19 **no es menor a** 19) se ejecuta `"Buenas noches " + quien`.




## 3. Esto es lo máximo

_Bueno, quizás no sea para taaaanto, pero sí, el `if` es muy útil_  :stuck_out_tongue_closed_eyes:

Veamos otro ejemplo...

```python
# Equivalente a abs
def valor_absoluto(numero):
  if numero >= 0:
    return numero
  else:
    return -numero
```

...y pongamos nombre a cada parte de la alternativa condicional:

 1. en primer lugar, tenemos la _condición_, que es lo que decide qué acción vamos a ejecutar. Podría ser cualquier _expresión booleana_, o en criollo cualquier cosa que represente una "pregunta" que se pueda responder con sí (`True`) o no (`False`);
 2. luego está _la acción_ del `if`, que retornará lo que queremos en caso de que la condición anterior sea **verdadera**;
 3. por último contamos con  _la acción_ del `else`, que retornará lo que queremos en caso de que la condición anterior sea **falsa**.

Además, a cada una de estas acciones también se las conoce como _ramas_ :deciduous_tree:, porque ramifican el flujo de ejecución, introduciendo en nuestro programa caminios alternativos. Ah, y algo no menor: las tabulaciones `↹` en cada rama son necesarias para que todo ande. :sweat_smile:

> ¡Escribamos nuestro primer `if`! Definí una función `maximo`, que funcione como `max` (¡no vale usarla!) y devuelva el máximo entre dos números:
>
> ```python
> >>> maximo(4, 5)
> 5
> >>> maximo(10, 4)
> 10
> ```



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
>>> maximo(4, 10)
10
>>> maximo(3, 10)
10
>>> maximo(2, 10)
10
>>> maximo(20, 10)
20
>>> maximo(20, 15)
20
```



### Para pensar

¡Felicitaciones! Este es un gran paso hacia adelante :footprints:

A continuación practicaremos un poco lo aprendido para recorrer con más seguridad nuestros nuevos (y alternativos :stuck_out_tongue:) caminos. ¡Acompañanos!

## 4. Cara o ceca

Hay veces en las que tenemos difíciles decisiones que tomar en nuestras vidas _(como por ejemplo, si comer pizzas :pizza: o empanadas  :dumpling:)_, y no tenemos más remedio que dejarlas libradas a la suerte.

Es allí que tomamos una moneda y decimos: _si sale cara, comemos pizzas, si no, empanadas_.

> Definí la función `decision_con_moneda`, que toma tres parámetros y devuelve el segundo si el primero es `"cara"`, o el tercero, si sale `"ceca"`. Por ejemplo:
>
> ```python
> >>> decision_con_moneda("cara", "pizzas", "empanadas")
> "pizzas"
>
> >>> decision_con_moneda("ceca", "pastas", "sopa")
> "sopa"
> ```


### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
>>> decision_con_moneda("cara", "pizzas", "empanadas")
"pizzas"
>>> decision_con_moneda("cara", "asado", "empanadas")
"asado"
>>> decision_con_moneda("ceca", "pizzas", "empanadas")
"empanadas"
>>> decision_con_moneda("ceca", "pizzas", "pastas")
"pastas"
```

### Solución posible

<details>
<summary>:eyes: Ver</summary>

```python
def decision_con_moneda(lado, opcion1, opcion2):
  if lado == "cara":
    return opcion1
  else:
    return opcion2
```

</details>


## 5. El retorno del booleano

Para cerrar, ahora que ya vimos cómo escribir la alternativa condicional, es momento de un pequeño recordatorio:
si usás adecuadamente las expresiones booleanas, ¡no es necesario utilizar esta estructura de control!

Supongamos que queremos desarrollar una función `es_mayor_de_edad`, que nos diga si alguien tiene
18 años o más. Una tentación es escribir lo siguiente:

```python
def es_mayor_de_edad(edad):
  if edad >= 18:
    return True
  else:
    return False
```

Sin embargo, **este `if` es totalmente innecesario**, dado que la expresión `edad >= 18` ya es booleana:

```python
def es_mayor_de_edad(edad):
  return edad >= 18
```

Mucho más simple, ¿no? :wink:

> Para Ema un número es de la suerte si:
>
> * es positivo, y
> * es menor a 100, y
> * no es el 15.
>
> Definí la función `es_numero_de_la_suerte` que dado un número diga si cumple la lógica anterior. ¡No vale usar `if`!




### Pistas

Los números positivos son los mayores a 0. :wink:



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
# positivos menores a 100 diferentes de 15
>>> es_numero_de_la_suerte(2)
True
>>> es_numero_de_la_suerte(5)
True
>>> es_numero_de_la_suerte(9)
True
>>> es_numero_de_la_suerte(45)
True
>>> es_numero_de_la_suerte(97)
True
# mayores a 100
>>> es_numero_de_la_suerte(101)
False
>>> es_numero_de_la_suerte(12456)
False
>>> es_numero_de_la_suerte(3003)
False
# negativos
>>> es_numero_de_la_suerte(-3)
False
# el 15
>>> es_numero_de_la_suerte(15)
False
```



### Para pensar

En general, como regla práctica, si tenés ifs que devuelven `True`s o `False`s, probablemente lo estás haciendo mal :cop:. Y si bien _funcionará_, habrás escrito código innecesariamente complejo y/o extenso.

Recordá: **¡menos código, más felicidad!** :grin:


## 6. Cartelitos

Para una importante conferencia, los organizadores nos pidieron que escribamos cartelitos identificatorios que cada asistente va a tener.

<div align="center">
	<img width="200px" src="https://raw.githubusercontent.com/mumuki/mumuki-guia-javascript-practica-funciones-y-tipos-de-datos/master/assets/name_badge.png"></img>
</div>

Para eso, tenemos que juntar su nombre, su apellido, y su título (_dr._, _dra._, _lic._, etc.) y armar un único string.

> Definí la función `escribir_cartelito`, que tome un título, un nombre y un apellido y forme un único string. Por ejemplo:
>
> ```python
> >>> escribir_cartelito("Dra.", "Ana", "Pérez")
> "Dra. Ana Pérez"
> ```





### Pistas

Tené en cuenta que los espacios para separar las palabras también son caracteres. ¡No te olvides de incluirlos al armar los cartelitos! :wink:

Por ejemplo:

```python
>>> "Pepe" + " " + "Palotes"
"Pepe Palotes"
```




### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
>>> escribir_cartelito("Dra.", "Ana", "Perez")
"Dra. Ana Perez"
>>> escribir_cartelito("Dr.", "Julio", "Gelman")
"Dr. Julio Gelman"
```

### Solución posible

<details>
<summary>:eyes: Ver</summary>

```python
def escribir_cartelito(titulo, nombre, apellido):
  return titulo + " " + nombre + " " + apellido
```

</details>


## 7. Más Cartelitos

Ah, ¡pero no tan rápido! Algunas veces en nuestro cartelito :name_badge: sólo queremos el título y el apellido, sin el nombre.

Por eso ahora nos toca mejorar nuestra función de forma que reciba 4 párámetros:

* El título
* El nombre y el apellido, como hasta ahora
* Un booleano que nos indique si queremos un cartelito corto con sólo título y apellido, o uno largo, como hasta ahora.


> Modificá la función `escribir_cartelito`, de forma que se comporte como se describe arriba.
>
> ```python
> >>> escribir_cartelito("Lic.", "Tomás", "Peralta", True)
> "Lic. Peralta"
> >>> escribir_cartelito("Ing.", "Dana", "Velázquez", False)
> "Ing. Dana Velázquez"
> ```




### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
>>> escribir_cartelito("Dra.", "Ana", "Perez", False)
"Dra. Ana Perez"
>>> escribir_cartelito("Dr.", "Julio", "Gelman", False)
"Dr. Julio Gelman"
>>> escribir_cartelito("Dra.", "Ana", "Perez", True)
"Dra. Perez"
>>> escribir_cartelito("Dr.", "Julio", "Gelman", True)
"Dr. Gelman"
```



### Para pensar

¡Genial! :clap:

Es importante recordar que es recomendable usar nombres expresivos en nuestras funciones y parámetros. No es lo mismo decir `string1`, `string2`, `string3`, `booleano` que `titulo`, `nombre`, `apellido`, `quiere_cartel_corto`. :grimacing:

## 8. Cartelitos óptimos

Ahora que ya podemos escribir nuestros cartelitos identificatorios grandes y chicos, queremos una función que nos dé el cartelito de tamaño óptimo:

* si nombre y apellido tienen, en total, más de 15 letras, queremos un cartelito corto;
* de lo contrario, queremos un cartelito largo.

> Definí la función `escribir_cartelito_optimo` que tome un título, un nombre y un apellido, e invocando `escribir_cartelito` genere un cartelito corto o largo, según las reglas anteriores. Ejemplo:
>
> ```python
> >>> escribir_cartelito_optimo("Ing.", "Carla", "Toledo")
> "Ing. Carla Toledo"
> >>> escribir_cartelito_optimo("Dr.", "Estanislao", "Schwarzschild")
> "Dr. Schwarzschild"
> ```


### Pistas

Recordá que el largo de un string lo podés saber con la función `len` y  que tenés `escribir_cartelito` definida en la Biblioteca. No tenés que definirla, solo invocarla. :wink:

### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
>>> escribir_cartelito_optimo("Ing.", "Carla", "Toledo")
"Ing. Carla Toledo"
>>> escribir_cartelito_optimo("Ing.", "Branco", "Luis")
"Ing. Branco Luis"
>>> escribir_cartelito_optimo("Dr.", "Estanislao", "Schwarzschild"
"Dr. Schwarzschild"
>>> escribir_cartelito_optimo("Ing.", "Katherine", "Boumann"
"Ing. Boumann"
```

## 9. Un mundo de alternativas

Ahora que ya vimos varios `if`s, volvamos a la función con la que iniciamos la lección:

```python
>>> saludar_a("Ivi", 17)
"Buenos días Ivi"
```

¿No es un poco tarde para decir _buen día_? :dizzy_face: ¿No sería mejor que `saludar_a` hiciera lo siguiente?

 1. Si son menos de las 12, que diga _Buenos días_;
 2. **en caso contrario** y si son menos de las 19, que diga _Buenas tardes_;
 3. **en caso contrario**, finalmente, que diga _Buenas noches_.

Sí, ¡eso es exactamente lo que queremos! Demos la bienvenida a un amigo inseparable del `if` y el `else`: el `elif`.

```python
def saludar_a(quien, horario):
  if horario < 12:
    return "Buenos días " + quien
  elif horario < 19:
    return "Buenas tardes " + quien
  else:
    return "Buenas noches " + quien
```

Como vemos, el `elif` nos permite tomar una decisión cuando la condición anterior no se cumplió, y tal como su nombre lo sugiere, funciona como la combinación de un `if` justo después de un `else`.

> :warning: ¿Esto significa que las condiciones se evalúan **en orden**? Esta definición alternativa...
>
> ```python
> def saludar_a_recargado(quien, horario):
>  if horario < 19:
>    return "Buenas tardes " + quien
>  elif horario < 12:
>    return "Buenos días " + quien
>  else:
>    return "Buenas noches " + quien
> ```
>
> ...¿hará lo mismo que la anterior? Te dejamos en la consola a `saludar_a` y `saludar_a_recargado` para que las pruebes y compares.
>
> Cuando termines, escribí `listo()`




### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
def listo():
  pass

def saludar_a(quien, horario):
  if horario < 12:
    return "Buenos días " + quien
  elif horario < 19:
    return "Buenas tardes " + quien
  else:
    return "Buenas noches " + quien

def saludar_a_recargado(quien, horario):
  if horario < 19:
    return "Buenas tardes " + quien
  elif horario < 12:
    return "Buenos días " + quien
  else:
    return "Buenas noches " + quien

>>> True
True
```



### Para pensar

Como vemos, el **orden importa** :exploding_head:.

La condición de `hora < 12` incluye a la condición de `hora < 19`, o en otras palabras, si la segunda se cumple, la primera también. Cuando sucede esto tenemos que tener cuidado y ordenar adecuadamente las condiciones :nerd:

## 10. ¿De qué signo sos?

Necesitamos una función `signo`, que dado un número nos devuelva:

* `1` si el número es positivo
* `0` si el número es cero
* `-1` si el número es negativo

> Definí la función `signo`.



### Pistas

:eyes: Algunas cosas a tener en cuenta:

* Un número es positivo cuando es **mayor a 0** y negativo cuando es **menor a 0**.
* La función `signo` debe devolver los números `1`, `-1` y `0`, no los strings `"1"`, `"-1"` y `"0"`



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
>>> signo(10)
1
>>> signo(1)
1
>>> signo(0)
0
>>> signo(-65)
-1
>>> signo(-87)
-1
```

## 11. Los premios

El jurado de un torneo nos pidió que desarrollemos una función `medalla_segun_puesto` que devuelva la medalla que le corresponde a los primeros puestos, según la siguiente lógica:

* primer puesto: le corresponde `"oro"`
* segundo puesto: le corresponde `"plata"`
* tercer puesto: le corresponde `"bronce"`
* otros puestos: le corresponde `"nada"`

```python
>>> medalla_segun_puesto(1)
"oro"
>>> medalla_segun_puesto(5)
"nada"
```

> Definí la función `medalla_segun_puesto` y probala en la consola.





### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
>>> medalla_segun_puesto(1)
"oro"
>>> medalla_segun_puesto(2)
"plata"
>>> medalla_segun_puesto(3)
"bronce"
>>> medalla_segun_puesto(4)
"nada"
>>> medalla_segun_puesto(5)
"nada"
>>> medalla_segun_puesto(0)
"nada"
```

## 12. ¡Envido!

Queremos saber el valor de las [cartas de truco](https://es.wikipedia.org/wiki/Truco_argentino) cuando jugamos al _envido_. Sabemos que:

* todas las cartas del 1 al 7, inclusive, valen su numeración
* las cartas del 10 al 12, inclusive, valen 0
* no se juega con 8s ni con 9s

> Definí una función `valor_envido` que tome un número de carta y devuelva su valor de envido:
>
> ```python
> >>> valor_envido(12)
> 0
> >>> valor_envido(3)
> 3
> ```
>
> :memo: Asumí que nunca te vamos a pasar cartas con 8 o 9 como valor.




### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
>>> valor_envido(2)
2
>>> valor_envido(1)
1
>>> valor_envido(5)
5
>>> valor_envido(12)
0
>>> valor_envido(11)
0
>>> valor_envido(10)
0
```

### Solución posible

<details>
<summary>:eyes: Ver</summary>

```python
def valor_envido(numero):
  if numero >= 1 and numero <= 7:
    return numero
  else:
    return 0
```

</details>



## 13. ¡Quiero retruco!

Bueno, ehm, no, pará, primero queremos calcular cuántos puntos de envido suma un jugador. Sabemos que:

* Si las dos cartas son del mismo palo, el valor del envido es la suma de sus valores de envido más 20.
* De lo contrario, el valor del envido es el mayor valor de envido entre ellas.

> Invocando la función `valor_envido` que hiciste en el ejercicio anterior, definí la función `puntos_de_envido_totales` que tome los valores y palos de dos cartas y diga cuánto envido suman en total. Ejemplo:
>
> ```python
> >>> puntos_de_envido_totales(1, "espadas", 4, "espadas")
> 25
> >>> puntos_de_envido_totales(2, "copas", 3, "bastos")
> 3
> ```

### Pistas

Para el caso en que las cartas sean de distinto palo te va a servir el ya conocido `max`. :sunglasses:

### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
>>> puntos_de_envido_totales(4, "espadas", 3, "espadas")
27
>>> puntos_de_envido_totales(6, "copas", 11, "copas")
26
>>> puntos_de_envido_totales(5, "oro", 2, "bastos")
5
>>> puntos_de_envido_totales(6, "copas", 7, "espadas")
7
```

### Solución posible

<details>
<summary>:eyes: Ver</summary>

```python
def puntos_de_envido_totales(numero_1, palo_1, numero_2, palo_2):
  if palo_1 == palo_2:
    return valor_envido(numero_1) + valor_envido(numero_2) + 20
  else:
    return max(valor_envido(numero_1), valor_envido(numero_2))
```

</details>


## 14. ¡Quiero vale cuatro!

Cuando se juega al truco, los equipos oponentes alternativamente pueden subir la apuesta. Por ejemplo, si un jugador canta _truco_, otro jugador puede cantarle _retruco_. Obviamente, los puntos que están en juego son cada vez mayores:

<table class="table table-striped" align="center">
   <tr><th>Canto</th><th>Puntos en juego</th></tr>
   <tr><td>truco</td><td>2</td></tr>
   <tr><td>retruco</td><td>3</td></tr>
   <tr><td>vale cuatro</td><td>4</td></tr>
</table>

> Definí la función `valor_canto_truco`, que tome el canto y devuelva cuántos puntos vale.
>
> ```python
> >>> valor_canto_truco("retruco")
> 3
> ```
>
> :warning: Asumí que sólo te van a pasar como argumento un string que represente un canto de truco. Por ejemplo, no vamos a probar la función para el caso `valor_canto_truco("zaraza")`


### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
>>> valor_canto_truco("retruco")
3
>>> valor_canto_truco("truco")
2
>>> valor_canto_truco("vale cuatro")
4
```

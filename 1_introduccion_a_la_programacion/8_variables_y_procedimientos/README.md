> Basado en https://github.com/mumukiproject/mumuki-guia-python3-variables-y-procedimientos-2021


# Variables y Procedimientos

Cuando programamos, ¿siempre vamos a querer retornar algo? ¿Habrá alguna especie de función que no retorne? Y si no retorna, ¿es una función? :thinking:

En esta lección vamos a conocer a las variables y los procedimientos, dos herramientas que nos van a pemitir solucionar nuevos tipos problemas y hacer programas más complejos. :sunglasses:

## 1. El círculo de la vida

En programación buscamos resolver nuestros problemas usando… programas :stuck_out_tongue_winking_eye:. Y entre los problemas que casi nadie quiere resolver están los matemáticos. Sobre todo aquellos en los que aparecen números, como pi, con infinitos decimales imposibles de recordar.  :head_bandage:

> Considerando al número pi igual a `3.14159265358979` (no es infinito pero lo suficientemente preciso para nuestros cáculos),
> definí las funciones `perimetro_circulo` y `area_circulo` que reciben el radio de un círculo y nos devuelven su perímetro y su área.




### Pistas

El perímetro se calcula como dos veces pi por el radio de un círculo. El área, en cambio, es el resultado de hacer pi por radio por radio.



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
>>> perimetro_circulo(1)
6.28318530717958
>>> perimetro_circulo(2)
12.56637061435916
>>> perimetro_circulo(0)
0
>>> area_circulo(1)
3.14159265358979
>>> area_circulo(2)
12.56637061435916
>>> area_circulo(0)
0
````



### Para pensar

Excelente, la precisión de nuestros cálculos es innegable :face_with_monocle:, pero tuvimos que escribir un número larguísimo. Pensemos que pi aparece en un montón de fórmulas matemáticas. ¿Es necesario escribir este número cada vez?¿No podemos hacer algo más cómodo? :thinking:

## 2. PI-enso que así es más fácil

Por suerte existe una herramienta que va a simplificar nuestra tarea de ahora en adelante: las _variables_. :grin:

Las variables nos permiten nombrar y reutilizar _valores_. Similar a cómo las funciones nos permiten dar nombres y reutilizar soluciones a problemas más pequeños. Por ejemplo, si hacemos...

``` python
primer_mes = "enero"
```

...estamos _asignándole_ el valor `"enero"` a la variable `primer_mes`. En criollo, estamos dándole ese valor a la variable. :relieved:

> Cambiá los lugares donde aparece `3.14159265358979` por la variable `pi` en las funciones que tenemos definidas.



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
>>> perimetro_circulo(1)
6.28318530717958
>>> perimetro_circulo(2)
12.56637061435916
>>> perimetro_circulo(0)
0
>>> area_circulo(1)
3.14159265358979
>>> area_circulo(2)
12.56637061435916
>>> area_circulo(0)
0
````



### Para pensar

¡Excelente! Gracias a la variable `pi` no tuvimos que escribir el número cada vez que teníamos que usarlo y ¡nuestro programa quedó mucho más entendible! :raised_hands:

## 3. Esto no tiene valor

Ya que vas entendiendo cómo se **asignan** las variables, te traemos algo para pensar: ¿qué pasa si intento **usar** una variable a la que nunca le asigné un valor? :scream:

> ¡Averigüémoslo! Tenemos esta función definida:
>
> ```python
> def suma_sin_sentido():
>	return numero + 8
> ```
>
> Invocala en la consola y fijate qué sucede.



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
def suma_sin_sentido():
	return numero + 8


````



### Para pensar

Entonces, ¿es necesario darle valor a nuestras variables antes de usarlas? :thinking:

## 4. Todo tiene un inicio

Para evitar errores :x: , antes de utilizar una variable tenemos que darle un valor inicial, es decir, _inicializarla_.

> Definí una función `ascensor_sobrecargado`, que toma una cantidad de personas y dice si entre todas superan la carga máxima:
>
> ```python
> >>> ascensor_sobrecargado(1)
False
> >>> ascensor_sobrecargado(100)
True
> ```
>
> Ah, y ¿cuál es el peso promedio de una persona? ¿Y la carga máxima? Para eso utilizaremos dos variables:
>
* `peso_promedio_persona_en_kilogramos`, la cual ya está incializada,
* `carga_maxima_en_kilogramos` que vas a tener que inicializar en `300`



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
>>> peso_promedio_persona_en_kilogramos = 70
>>> ascensor_sobrecargado(4)
False
>>> peso_promedio_persona_en_kilogramos = 80
>>> ascensor_sobrecargado(4)
True
>>> peso_promedio_persona_en_kilogramos = 80
>>> ascensor_sobrecargado(2)
False
>>> peso_promedio_persona_en_kilogramos = 80
>>> ascensor_sobrecargado(5)
True
````



### Para pensar

¡Excelente! :clap:

Con lo que venimos haciendo cualquier función puede utilizar a las variables, pero ¿qué pasa si no queremos que eso pase? :thinking:

## 5. Jugando de local

Hay veces que no queremos, o simplemente no tiene sentido, que nuestras variables sean accedidas por todas las funciones. Por suerte, podemos inicializar variables tanto directamente en el programa, como dentro de un `def`:

```python
def el_mas_largo_sin_espacios(un_string, otro_string):
  un_string_sin_espacios = str.strip(un_string)
  otro_string_sin_espacios = str.strip(otro_string)

  if(len(un_string_sin_espacios) > len(otro_string_sin_espacios)):
    return un_string_sin_espacios
  else:
    return otro_string_sin_espacios
```

Las variables inicializadas dentro de un `def`, conocidas como _variables locales_, no presentan mayor misterio. Sin embargo, hay que tener un particular cuidado :warning: ya que sólo se pueden utilizar dentro del `def` en cuestión. Si quiero referenciarla desde un programa...

```python
pregunta = "¿" + un_string_sin_espacios + "?"
```

...¡boom! ¡se romperá! :collision:

Sin embargo, las variables inicializadas directamente en el programa, conocidas como _variables globales_, pueden ser leídas desde cualquier `def`. Por ejemplo:

```python
peso_maximo_del_equipaje_en_gramos = 5000

def puede_llevar(peso_equipaje):
  return peso_equipaje <= peso_maximo_del_equipaje_en_gramos
```

> Como te habrás dado cuenta, nunca nos olvidamos de saludar ¡y ahora no es la excepción!

> Modificá la función `saludar_a` para evitar la repetición de lógica. Para eso utilizá una variable local `final_de_saludo`.



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
>>> saludar_a("Gus", 11)
"¡Buenos días Gus!"
>>> saludar_a("May", 12)
"¡Buenas tardes May!"
>>> saludar_a("Lu", 18)
"¡Buenas tardes Lu!"
>>> saludar_a("Guille", 19)
"¡Buenas noches Guille!"
>>> saludar_a("Jor", 20)
"¡Buenas noches Jor!"
````

### Para pensar

¡Excelente! :raised_hands:

Para resumir lo visto:

* las variables globales se inicializan por fuera de las funciones y pueden ser accedidas desde cualquier lugar del programa;
* las variables locales pueden ser accedidas solo desde la función donde la inicializamos.

Si bien ahora conocemos los dos tipos de variables no abusemos de su uso. Recordemos que las variables nos sirven para utilizar un mismo valor en más de un lugar y evitar la repetición de lógica.

## 6. Variemos un poco

_Todo muy lindo hasta acá, pero ¿por qué se llaman variables si no varian?_ :face_with_raised_eyebrow:

Bueno, es que en realidad sí pueden variar :sunglasses: . Veamos un ejemplo:

```python
# inicializamos la variable para que valga 0...
dias_sin_accidentes_con_velocirraptores = 0

# ...y más adelante, la actualizamos
dias_sin_accidentes_con_velocirraptores = dias_sin_accidentes_con_velocirraptores + 1

# ¡ahora vale 1!
dias_sin_accidentes_con_velocirraptores
```

Sin embargo, hay que tener un cuidado particular si trabajamos con variables globales: si queremos modificarlas dentro de una función, deberemos anteponer `global` a su nombre:

```python
# inicializamos la variable al inicio de nuestro programa
dias_sin_accidentes_con_velocirraptores = 0

def pasar_un_dia_normal():
  # indicamos a Python que vamos a realizar modificaciones sobre la variable global
  global dias_sin_accidentes_con_velocirraptores

  # acá adentro la actualizamos
  dias_sin_accidentes_con_velocirraptores = dias_sin_accidentes_con_velocirraptores + 1
```

> Probá en la consola, en orden, lo siguiente:
>
> 1. `dias_sin_accidentes_con_velocirraptores`
> 2. `pasar_un_dia_normal()`
> 3. `pasar_un_dia_normal()`
> 4. `pasar_un_dia_normal()`
> 5. `dias_sin_accidentes_con_velocirraptores`

> Podés usar las flechas de tu teclado para navegar entre comandos ejecutados previamente. :arrow_up_small: :arrow_down_small:



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
dias_sin_accidentes_con_velocirraptores = 0

def pasar_un_dia_normal():
  global dias_sin_accidentes_con_velocirraptores
  dias_sin_accidentes_con_velocirraptores = dias_sin_accidentes_con_velocirraptores + 1


````



### Para pensar

¡Varió! O mutó como solemos decir. Pero tené en cuenta que poder hacerlo, no significa querer hacerlo. No siempre vamos a querer modificar el valor de nuestras variables. :relieved:

Si te preguntas por qué es necesario anteponer `global`, tené en cuenta que las variables globales pueden ser accedidas por cualquier función. Es la manera que tenemos de asegurar que sabemos eso y que aún así queremos modificar nuestra variable. :relieved:


## 7. Procedemos a lo siguiente

¿Notaste algo distinto en la "función" del ejercicio anterior :mag:? Veámosla nuevamente:

```python
def pasar_un_dia_normal():
  global dias_sin_accidentes_con_velocirraptores
  dias_sin_accidentes_con_velocirraptores = dias_sin_accidentes_con_velocirraptores + 1
```

¡No tiene `return`! Pero, ¿las funciones no tienen todas un `return`? :face_with_monocle:

Correcto, es que en realidad `pasar_un_dia_normal()` no es una función, ¡es un _procedimiento_! :open_mouth: Si bien tanto funciones como procedimientos se definen de la misma manera y ambos nos ayudan a simplificar nuestras tareas, tienen algunas diferencias:

* las funciones **retornan un valor y no tienen efecto**, es decir, no cambian nuestras variables;
* los procedimientos **no retornan nada y tienen un efecto** al ser invocados.

> Ahora que sabes la diferencia, definí un procedimiento `aumentar_fortuna` que duplique el valor de la variable global `pesos_en_mi_billetera`. No inicialices la variable, porque ya lo hicimos por vos (con una cantidad secreta de dinero :wink:).



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
pesos_en_mi_billetera = 0

global pesos_en_mi_billetera
pesos_en_mi_billetera = 100
aumentar_fortuna()
self.assertEqual(pesos_en_mi_billetera, 200)
global pesos_en_mi_billetera
pesos_en_mi_billetera = 30
aumentar_fortuna()
aumentar_fortuna()
aumentar_fortuna()
self.assertEqual(pesos_en_mi_billetera, 240)
````



### Para pensar

Actualizaciones como duplicar, triplicar, incrementar en uno o en una cierta cantidad son tan comunes que Python presenta algunos atajos:

```python
x += y # equivalente a x = x + y
x *= y # equivalente a x = x * y
x -= y # equivalente a x = x - y
```

¡Usalos cuando quieras! :wink:

## 8. ¡Que el último apague la luz!

Ahora que conocimos a los procedimientos podemos modelar casos de alternancia utilizando `not`. Por ejemplo, prender y apagar una luz :bulb::

```python
luz_prendida = False

def apretar_interruptor():
  global luz_prendida
  luz_prendida = not luz_prendida
```

¡Ahora te toca a vos!

> Definí el procedimiento `usar_cierre` para que podamos abrir y cerrar nuestra mochila. :school_satchel:



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
usar_cierre()
>>> mochila_abierta
False
global mochila_abierta
mochila_abierta = False
usar_cierre()
>>> mochila_abierta
True
usar_cierre()
usar_cierre()
>>> mochila_abierta
True
````

## 9. Tomate un mate

Con todo lo que aprendimos hasta acá estaría bueno cortar para tomar unos mates, ¿no? :mate: Mejor aún, ¡programemos los mates! :sweat:

Sabiendo que al cebar un mate la cantidad de agua del termo disminuye...

> ...inicializá la variable global `agua_del_termo` (que representa los mililitros que tiene el termo) con 1000. También definí el procedimiento `cebar_mate` que disminuye 30 mililitros del agua en el termo.



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
global agua_del_termo
agua_del_termo = 1000
cebar_mate()
self.assertEqual(agua_del_termo, 970)
global agua_del_termo
agua_del_termo = 1000
cebar_mate()
cebar_mate()
cebar_mate()
self.assertEqual(agua_del_termo, 910)
````

## 10. Se enfrió el agua

Sin importar cuan bueno sea el termo, algunas veces el agua simplemente se enfría. :confounded:

> Definí los procedimientos:

> * `vaciar_termo` que saca todo el `agua_del_termo`, es decir, deja en 0 la variable;
> * `llenar_termo` que vuelve a poner nuestra variable en 1000.



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
global agua_del_termo
agua_del_termo = 1000
vaciar_termo()
self.assertEqual(agua_del_termo, 0)
global agua_del_termo
agua_del_termo = 80
llenar_termo()
self.assertEqual(agua_del_termo, 1000)
````

## 11. No creo tomar mucho más

A veces no hace falta llenar tooooodo el termo, con un poco de agua quizás alcanza. :droplet:

> Definí el procedimiento `cargar_termo` que espere una cantidad de agua como argumento y aumente el `agua_del_termo` en esa cantidad.



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
global agua_del_termo
agua_del_termo = 600
cargar_termo(200)
self.assertEqual(agua_del_termo, 800)
global agua_del_termo
agua_del_termo = 200
cargar_termo(500)
self.assertEqual(agua_del_termo, 700)
````



### Para pensar

Todo bien con el termo, pero ¿dónde está el mate? :mate:

## 12. Jaque, el mate

Ya hicimos toda la lógica relacionada con el agua del termo, pero del mate ni noticias. :unamused:

> Vamos a modificar un poco el programa que teníamos:

> 1. Inicializá la variable `agua_del_mate` en 0.
> 2. Modificá el procedimiento `cebar_mate` para que, además de lo que hacía, aumente en 30 mililitros el `agua_del_mate`.
> 3. Definí el procedimiento `tomar_mate` que deja en 0 el agua del mate.



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
global agua_del_termo
agua_del_termo = 1000
cebar_mate()
self.assertEqual(agua_del_termo, 970)
global agua_del_termo
agua_del_termo = 1000
cebar_mate()
cebar_mate()
cebar_mate()
self.assertEqual(agua_del_termo, 910)
global agua_del_mate
agua_del_mate = 0
cebar_mate()
self.assertEqual(agua_del_mate, 30)
global agua_del_mate
agua_del_mate = 20
tomar_mate()
self.assertEqual(agua_del_mate, 0)
````



### Para pensar

Bueno, ya es bastante mate, ¿no? :eyes:

Recordemos que la educación está ante todo. :relieved:

## 13. ¡Gracias!

Es conocimiento popular que cuando no queremos más mate solo basta con decir _Gracias_. :relaxed:

Para modelar esta lógica vamos a definir el procedimiento `pasar` que no va a hacer nada. Sin embargo, no va a ser un procedimiento vacío sino que va a estar definido de la siguiente manera:

```python
def pasar():
  pass
```

> Probalo en la consola haciendo lo siguiente en orden:

> 1. `agua_del_mate`
> 2. `agua_del_termo`
> 3. `cebar_mate()`
> 4. `agua_del_mate`
> 5. `pasar()`
> 6. `agua_del_mate`
> 7. `agua_del_termo`



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
agua_del_mate = 0
agua_del_termo = 1000

def cebar_mate():
  global agua_del_mate
  global agua_del_termo
  agua_del_termo -= 30
  agua_del_mate += 30

def tomar_mate():
  global agua_del_mate
  agua_del_mate = 0

def pasar():
  pass


````



### Para pensar

Te preguntarás por qué no dejamos vacío el procedimiento y ya, ¿no?

Es que en Python no podemos definir un procedimiento vacío...

```python
def pasar():
```

...tampoco con solo un comentario...

```python
def pasar():
  # Paso
```

...dado que los comentarios son ignorados. Sin embargo, `pass` es tenido en cuenta ya que es la representación en código de "no hacer nada". :exploding_head:

## 14. Bajemos el volumen

Mirá el siguiente programa con atención :eyes: :

```python
volumen = 40

def subir_volumen(decibeles):
	global volumen
	volumen += decibeles

def bajar_volumen(decibeles):
	global volumen
	volumen -= decibeles

def es_volumen_saludable():
	return volumen <= 75
```

> Marcá las afirmaciones correctas:

1. ☐ `volumen` es una variable local
1. ☐ `volumen` es una variable global
1. ☐ `subir_volumen` es una función
1. ☐ `subir_volumen` es un procedimiento
1. ☐ `bajar_volumen` es una función
1. ☐ `bajar_volumen` es un procedimiento
1. ☐ `es_volumen_saludable` es una función
1. ☐ `es_volumen_saludable` es un procedimiento
1. ☐ `subir_volumen` retorna un número
1. ☐ `es_volumen_saludable` retorna un número
1. ☐ `es_volumen_saludable` retorna un booleano

### Respuesta

1. ☒ `volumen` es una variable local
1. ☑️ `volumen` es una variable global
1. ☒ `subir_volumen` es una función
1. ☑️ `subir_volumen` es un procedimiento
1. ☒ `bajar_volumen` es una función
1. ☑️ `bajar_volumen` es un procedimiento
1. ☑️ `es_volumen_saludable` es una función
1. ☒ `es_volumen_saludable` es un procedimiento
1. ☒ `subir_volumen` retorna un número
1. ☒ `es_volumen_saludable` retorna un número
1. ☑️ `es_volumen_saludable` retorna un booleano

### Para pensar

¡Perfecto! :ok_hand:

A lo largo de esta lección hiciste muchas cosas nuevas:

* conociste los procedimientos en el lenguaje Python, que si bien se definen igual que las funciones son bien distintos; :eyes:
* utilizaste los dos tipos de variables, locales y globales, y aprendiste sus diferencias. :sunglasses:

¡Veamos que depara la siguiente lección! :eyes:


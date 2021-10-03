> Basado en https://github.com/mumukiproject/mumuki-guia-fundamentos-python-listas

# Listas

La programación no sería tan divertida y poderosa si sólo pudieramos trabajar con una cosa por vez: muchas veces no vamos a querer simplemente operar un _string_, un booleano o un número, sino varios a la vez.

¡Llegó entonces el momento de aprender a tratar conjuntos de cosas! Presentamos a... ¡las listas! 😁

## 1. Series favoritas

Supongamos que queremos representar al conjunto de nuestras series favoritas. ¿Cómo podríamos hacerlo?

```python
series_favoritas_de_ana = ["Black Mirror", "Breaking Bad", "Recordando el Show de Alejandro Molina", "En Terapia", "Gambito de Dama"]
series_favoritas_de_hector = ["Game of Thrones", "Bojack Horseman", "Attack on Titan"]
```

Como ves, para representar a un conjunto de strings, colocamos todos esos strings que nos interesan, entre corchetes (`[` y `]`) separados por comas. Fácil, ¿no?

> Probá en la consola las siguientes consultas:
>
``` python
>>> series_favoritas_de_ana
>>> series_favoritas_de_hector
>>> ["hola","mundo!"]
>>> ["hola","hola"]
```
> Mirá cada uno de los resultados y contá cuántos strings hay en cada lista





### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
series_favoritas_de_ana = ["Black Mirror", "Breaking Bad", "En Terapia"]
series_favoritas_de_hector = ["Game of Thrones", "Recordando el Show de Alejandro Molina", "House of Cards"]
```



### Para pensar

¡Bien! Acabamos de ver 4 listas diferentes, con cantidades de _elementos_ diferentes. Pero, ¿notaste algo particular en la última lista? ¿Cuántos elementos hay? ¿Uno o dos?

## 2. Y esto, es una lista

Lo que acabamos de ver es cómo modelar fácilmente conjuntos de cosas. Mediante el uso de `[]`, en Python contamos con una manera simple de agrupar esos elementos en listas.

¿Acaso hay una cantidad máxima de elementos? ¡No, no hay límite! Las listas pueden tener cualquier cantidad de elementos.

Y no sólo eso, sino que además, el orden es importante. Por ejemplo, no es lo mismo `["hola", "mundo"]` que `["mundo", "hola"]`: ambos tienen los mismos elementos, pero en posiciones diferentes.

> Probá en la consola las siguientes consultas:
>
``` python
>>> ["hola", "mundo"] == ["mundo", "hola"]
>>> ["hola", "mundo"] == ["hola", "todo", "el", "mundo"]
>>> ["hola"] == ["hola", "mundo"]
>>> ["hola", "mundo"] == ["hola", "mundo"]
```

> ¿Qué conclusiones podés sacar? 💭




### Para pensar

Para que dos listas sean iguales no alcanza con tener los mismos elementos, sino que es necesario que estén en exactamente el mismo orden. 😌

## 3. Juegos de azar

Pero, pero, ¿sólo podemos crear listas de strings? ¿Y si quiero, por ejemplo, representar los números de la lotería que salieron la semana pasada? ¿O las tiradas sucesivas de un dado? 🎲  ¿O si salió cara o ceca en tiradas sucesivas de una moneda? 🤔

> Probá en la consola las siguientes consultas y mirá qué elementos tiene cada lista:
>
``` python
>>> numeros_de_loteria
>>> salio_cara
>>> tiradas_del_dado
>>> lista_de_listas
```



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
numeros_de_loteria = [2, 11, 17, 32, 36, 39]
tiradas_del_dado = [1, 6, 6, 2, 2, 4]
salio_cara = [False, False, True, False]
lista_de_listas = [[1, 2, 3], [4, 5, 6]]


```



### Para pensar

Como ves, también podemos representar conjuntos de números o booleanos de igual forma: escribiéndolos entre corchetes y separados por comas. Podemos tener listas de números, de strings, de booleanos, etc. ¡Incluso listas de listas! 🤯

```python
numeros_de_loteria = [2, 11, 17, 32, 36, 39]
tiradas_del_dado = [1, 6, 6, 2, 2, 4]
salio_cara = [False, False, True, False]
```

## 4. ¿Medio llena o medio vacía?

Genial, ¡parece que una lista puede contener cualquier tipo de elemento! Podemos tener listas de booleanos, de números, de strings, de listas...

Y no sólo eso, sino que además pueden contener cualquier cantidad de elementos: uno, dos, quince, ¡cientos! 😳

¿Podremos entonces tener listas vacías, es decir, que no tengan elementos? 🧐

> ¡Cómo te imaginás que se escribirá una lista que no tiene elementos? Intentá inicializar una variable `una_lista_vacia` con, justamente, una lista sin ningún elemento.


### Para pensar

¡Sí, se puede tener listas vacías! y se inicializan como las que vimos hasta ahora:

```python
un_lista_vacia = []
```


## 5. ¿Cuántos elementos tenés?

Por el momento ya sabemos qué cosas podemos representar con listas, y cómo hacerlo. Pero, ¿qué podemos hacer con ellas?

Empecemos por lo fácil: ¿te acordás de `len`? También funciona con listas.

> Realizá las siguientes consultas en la consola y fijate que hace:
>
``` python
>>> len([])
>>> len([4, 3])
>>> len([[1,2],[8],[14, 87]])
>>> len(numeros_de_loteria)
```



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
numeros_de_loteria = [2, 11, 17, 32, 36, 39]


```



### Para pensar

¡Genial! 😁

Ya sabemos que al invocar `len` con un string nos da su cantidad de caracteres. Al invocarlo con una lista nos da la cantidad de elementos.

## 6. Todo se transforma

Las listas son muy útiles para contener múltiples elementos. ¡Pero hay más! También podemos agregarle elementos en cualquier momento, utilizando la función `list.append`, que recibe dos parámetros: la lista y el elemento. Por ejemplo:

```python
>>> discos = ["Serú Girán", "Artaud", "Almendra", "Quebrado"]
>>> len(discos)
4
>>> list.append(discos, "Vida")
>>> len(discos)
5
```

Como vemos, `list.append` agrega un elemento a la lista, lo cual hace que su tamaño aumente. ¿Pero en qué parte de la lista lo agrega? ¿Al principio? ¿Al final? ¿En el medio? 🤔

> Averigualo vos: inspeccioná en la consola qué elementos contiene `libros`, agregale `"Fundación"` y volvé a inspeccionar `libros`.
>
> Además existe una función `list.remove`, que recibe por parámetro una lista y un elemento de ella. Investigá en la consola qué hace. 👀
>
>Cuando termines, escribí `listo()`.



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
libros = ["Ensayo sobre la ceguera", "Socorro", "Mi planta naranja lima"]

def listo():
  pass


```



### Para pensar

Esto quiere decir que las listas son mutables, es decir, se pueden modificar. 😌

## 7. Esto no va acá

Bueno, ya hablamos bastante; ¡es hora de la acción! 🎥

> Declará un procedimiento `trasladar`, que tome dos listas y un elemento de la primera. `trasladar` debe sacar el elemento de la primera lista y agregarlo en la segunda.
>
> Ejemplo:
>
>```python
> una_lista = [1, 2, 3]
> otra_lista = [4, 5]
>
> trasladar(una_lista, otra_lista, 3)
>
> una_lista # debería ser [1, 2]
> otra_lista # debería ser [4, 5, 3]
>```




### Pistas

¿Tenés dudas sobre cómo quitar y agregar elementos? Repasemos los siguientes procedimientos:

* `list.append(lista, elemento)`: agrega `elemento` al final de `lista`
* `list.remove(lista, elemento)`: saca `elemento` de `lista`




### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
un_array = [1, 2, 3]
otro_array = [4, 5]
trasladar(un_array, otro_array, 3)
self.assertEqual(un_array, [1, 2])
self.assertEqual(otro_array, [4, 5, 3])
un_array = [9, 8, 7]
otro_array = [4, 5]
trasladar(un_array, otro_array, 7)
self.assertEqual(un_array, [9, 8])
self.assertEqual(otro_array, [4, 5, 7])
```



### Para pensar

¡Felicitaciones! 👏

Hasta ahora estuvimos agregando, quitando y consultando longitudes. ¿Qué más podremos hacer con las listas? ¡Seguinos! 💪

## 8. ¿Y dónde está?

Otra cosa que queremos hacer con las listas es saber en qué posición se encuentra un elemento. Para ello utilizamos la función `list.index` de la siguiente manera:

```python
>>> list.index(["a", "la", "grande", "le", "puse", "cuca"], "grande")
2
>>> dias_laborales = ["lunes", "martes", "miercoles", "jueves", "viernes"]
>>>list.index(dias_laborales, "lunes")
0
```

Como ves, lo curioso de esta función es que pareciera devolver siempre uno menos de lo esperado. Por ejemplo, la palabra `"grande"` aparece tercera, no segunda; y `"lunes"` es el primer día laboral, no el cero. ¿Quienes crearon Python se equivocaron? 😕

¡No! 😅 Se trata de que en Python, al igual que en muchos lenguajes, las posiciones de las listas arrancan en 0: el primer elemento está en la posición 0, el segundo en la 1, el tercero en la 2, y así.

> ¿Y qué sucede si le pasás por parámetro a `list.index` un elemento que no tiene? ¡Averigualo!
>
> Probá lo siguiente:
>
> ```python
> >>> list.index(dias_laborales, "osvaldo")
> ```




### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
dias_laborales = ["lunes", "martes", "miercoles", "jueves", "viernes"]


```



### Para pensar

¡Exacto! Arrojará un error. 😢

Pero eso está bueno, ¿qué iba a hacer? 😅 Es preferible que si no existe el elemento nos notifique que hubo un problema a que nos devuelva cualquier cosa, ¿no? 😁

## 9. ¡Acá está!

Bueno, parece que pasan cosas feas cuando queremos saber la posición de un elemento que no está en la lista. Así que para saber si un elemento pertenece o no, alcanzaría con ver si Python lanza un error 💥, ¿no?

Tenemos buenas noticias 📰, ¡Python tiene una manera más fácil de hacer esto!

> Probá en la consola lo siguiente:
>
```python
>>> 7 in [1, 6, 7, 6]
>>> 6 in [1, 6, 7, 6]
>>> 7 in [8, 5]
>>> 7 in []
```





### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
>>> contiene([1, 6, 7, 6], 7)
True
>>> contiene([1, 6, 7, 6], 6)
True
>>> contiene([], 7)
False
>>> contiene([8, 5], 7)
False
>>> contiene([1, 8, 5], 7)
False
>>> contiene([1, 1, 1], 1)
True
```



### Para pensar

¡Menos mal que no hace falta caer en errores para verificar! 😌

Como verás, al igual que `len`, `in` también funciona con strings y con listas. 🙌

## 10. ¿Qué ves cuando me ves?

Muchas veces queremos ver alguna serie en nuestro tiempo de ocio 📺, pero no sabemos cuáles están buenas ¡y cuáles no!

Para eso vamos a hacer una función `serie_no_recomendable`. Por suerte tenemos un ranking con las 10 series más vistas de la televisión. ¿Y cuándo no es recomendable una serie? Cuando no pertenece al ranking o cuando está entre las últimas 5 posiciones.

> Definí la función `serie_no_recomendable`. La lista `ranking` ya está definida. 🕶️



### Pistas

Es importante que respetes el orden de las condiciones:
Una serie no es recomendable _cuando no pertenece al ranking o cuando está entre las últimas 5 posiciones_.

También recordá que las posiciones en las listas comienzan en 0. 😉



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
ranking = ["Breaking bad", "Black mirror", "Better call saul", "Dr. House", "Los simpsons", "El marginal", "The walking dead", "24", "Gotham", "Epitafios"]

>>> serie_no_recomendable("Stranger things")
True
>>> serie_no_recomendable("El marginal")
True
>>> serie_no_recomendable("24")
True
>>> serie_no_recomendable("Breaking bad")
False
>>> serie_no_recomendable("Los simpsons")
False
```



### Para pensar

¿Por qué tuvimos que poner las expresiones en ese orden específico?

* Si preguntábamos primero por la posición de la serie en el ranking, y la serie no estaba en la lista, nuestro código iba a explotar. 💥
* En cambio, como lo hicimos, si la serie no está en el ranking (`not serie in ranking`) no hace falta preguntar su posición, porque ya sabemos que toda esa expresión es verdadera.

Recordemos que para que el operador `or` nos devuelva `True` alcanza con que una de las condiciones sea verdadera. Si la primera es verdadera, ¿para qué va a preguntar por la segunda? 😅

## 11. ¡No te pases!

Así como existe una función para averiguar en qué posición está un elemento, también puede ocurrir que queramos saber lo contrario: qué elemento está en una cierta posición. 😮

Para averiguarlo podemos usar el **operador de indexación**, escribiendo después de la colección y entre corchetes `[]` la posición que queremos para averiguar:

```python
>>> meses_del_anio[0] # recordá que el primer elemento está en la posición 0
"enero"
>>> ["ese", "perro", "tiene", "la", "cola", "peluda"][1]
"perro"
```

¡Ojo! El número que le pases, formalmente llamado **índice**, debe ser menor a la longitud de la lista, o cosas malas pueden suceder. 😲

> Probalo en la consola: ¿qué sucede si le pedís el elemento 0 a una lista vacía? ¿O si le pedís el elemento 48 a los `meses_del_anio`?
>
> Cuando hayas hecho las pruebas escribí `listo()`.




### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
meses_del_anio = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

def listo():
  pass


```



### Para pensar

¡Qué coherencia la de Python! 👏 Tira error cuando queremos acceder al índice de un elemento que no está en la lista, pero también cuando queremos acceder a un elemento en una posición que no tiene.

## 12. Más premios

Como vimos, al pedir un elemento en una posición igual o mayor al tamaño de la lista, se va a producir un error `IndexError: list index out of range`. Así que ¡ojo, no te pases de índice! ⚠️

> Teniendo esto en cuenta, va un desafío: definí nuevamente la función `medalla_segun_puesto`, pero esta vez usando como máximo un único `if`. Quizás las listas te pueden ser útiles acá 😉.
>
> Te recordamos qué hace la función: tiene que devolver la medalla que le corresponde a los primeros puestos de una competencia.
>
>```python
>>>> medalla_segun_puesto(1)
>"oro"
>>>> medalla_segun_puesto(2)
>"plata"
>>>> medalla_segun_puesto(3)
>"bronce"
>>>> medalla_segun_puesto(4)
>"nada"
>>>> medalla_segun_puesto(5)
>"nada"
> ```




### Pistas

¿En qué nos puede ser útil una lista aquí? Pensá que la medalla que recibe la persona está _directamente relacionada_ con la posición en la que sale en la competencia. 💭



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
>>> medalla_segun_puesto(15)
"nada"
>>> medalla_segun_puesto(83)
"nada"
```



### Para pensar

¡Felicitaciones! 👏

Acabas de conocer una estructura de datos que te permite agruparlos: ¡la lista! 😁

También aprendiste qué datos puede tener dentro, cómo agregarle o sacarle elementos, conocer sus posiciones, obtener su longitud y los elementos por posición. 🙌

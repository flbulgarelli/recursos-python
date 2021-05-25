> Basado en https://github.com/mumukiproject/mumuki-guia-python3-recorridos-2021

# 4. Recorridos

En lecciones anteriores definimos funciones, usamos registros y listas. Ahora que tenemos todas esas herramientas, llega el momento de combinarlas y aprender a hacer cosas más complejas recorriéndolas. ¡Acompañanos!

## 1. Todas las ganancias, la ganancia

Ana, contadora de una conocida empresa :office:, tiene diccionarios para representar los balances de cada mes y distintas listas para guardarlos. Por ejemplo:

```python
#En julio ganó $50, en agosto perdió $12, etc.
balances_ultimo_semestre = [
	{ "mes": "julio", "ganancia": 50 },
	{ "mes": "agosto", "ganancia": -12 },
	{ "mes": "septiembre", "ganancia": 1000 },
	{ "mes": "octubre", "ganancia": 300 },
	{ "mes":  "noviembre", "ganancia": 200 },
	{ "mes": "diciembre", "ganancia": 0 }
]

balances_primer_trimestre = [
	{ "mes": "enero", "ganancia": 2 },
	{ "mes": "febrero", "ganancia": 10 },
	{ "mes": "marzo", "ganancia": -20 }
]
```

Dicho esto, Ana necesita saber la ganancia acumulada de un conjunto de balances.

> Definí la función `ganancia_total` que dado una lista de balances cualquiera nos devuelva la suma de todas:
>
```python
>>> ganancia_total(balances_de_un_periodo):
1538
```



### Pistas

Nuestro viejo amigo `for...in` y una variable local nos van a ayudar en esta tarea. Lo importante es pensar con qué valor la inicializamos y qué debemos hacer en cada iteración. :relaxed:



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
>>> ganancia_total([
  { "mes": "enero", "ganancia": 2 },
  { "mes": "febrero", "ganancia": 10 },
  { "mes": "marzo", "ganancia": -20 }])
-8
>>> ganancia_total([
  { "mes": "julio", "ganancia": 50 },
  { "mes": "agosto", "ganancia": -12 },
  { "mes": "septiembre", "ganancia": 1000 },
  { "mes": "octubre", "ganancia": 300 },
  { "mes":  "noviembre", "ganancia": 200 },
  { "mes": "diciembre", "ganancia": 0 }])
1538
```

### Para pensar

¡Excelente! :star_struck:

En este caso como queríamos obtener una sumatoria, nuestra variable tenía que inicializarse en 0 ya que es el valor neutro de la suma. Si por ejemplo quisieramos hacer una productoria (lo mismo que la sumatoria pero multiplicando) deberíamos inicializar nuestra variable en 1. No siempre es fácil darse cuenta qué valor inicial debemos utilizar, pero es muy importante que lo pensemos antes de encarar el `for...in`. :hugging:

## 2. Cuentas claras

¡Ana tiene nuevos requirimientos! Ahora nos pidió lo siguiente: _"Quiero saber cuántos balances fueron positivos, es decir, aquellos en los que la ganancia fue mayor a cero"_. :chart_with_upwards_trend:

> Definí la función `cantidad_de_balances_positivos` que dada una lista de balances nos retorne cuántos son positivos.




### Pistas

Lo importante en este ejercicio es inicializar una variable local e incrementarla solo cuando corresponda. Para eso vas a tener que usar un `if`. :nerd:



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
>>> cantidad_de_balances_positivos([{ "mes": "noviembre", "ganancia": 5 }])
1
>>> cantidad_de_balances_positivos([
  { "mes": "marzo", "ganancia": 8 },
  { "mes": "agosto", "ganancia": 10 }])
2
>>> cantidad_de_balances_positivos([]), 0
>>> cantidad_de_balances_positivos([
  { "mes": "marzo", "ganancia": 0 },
  { "mes": "agosto", "ganancia": 0 }])
0
>>> cantidad_de_balances_positivos([
  { "mes": "enero", "ganancia": 10 },
  { "mes": "febrero", "ganancia": -10 },
  { "mes": "marzo", "ganancia": 2 },
  { "mes": "abril", "ganancia": 100 }])
3
>>> cantidad_de_balances_positivos([
  { "mes": "enero", "ganancia": -1 },
  { "mes": "febrero", "ganancia": -2 },
  { "mes": "marzo", "ganancia": -3 }])
0
```



### Para pensar

La variable local que utilizaste es lo que en programación se conoce como _contador_, una variable que se incrementa cada vez que hacemos algo dentro de un `for...in` o solo aquellas veces que se cumpla una condición (como en este caso). :wink:

## 3. Soy el mapa, soy el mapa

Más allá de las ganancias acumuladas o los balances positivos, Ana quisiera poder obtener todas las ganancias a partir de una lista de balances. Para ello debemos transformar, o _mapear_, cada elemento de la lista. :thumbsup:

> Definí la función `ganancias` que toma una lista de balances y devuelve una lista que posea solo las ganancias de cada uno.
>
> ```python
> >>> ganancias([
      { "mes": "enero", "ganancia": 40 },
      { "mes": "febrero", "ganancia": 12 },
      { "mes": "marzo", "ganancia": 8}
  ])
> [40, 12, 8]
> ```




### Pistas

_¿Y ahora con qué valor inicializamos la variable local?_ :thinking:

En este caso te va a servir una lista vacía, ¡pero no te olvides de agregarle elementos! :wink:



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
self.assertEqual(ganancias([{ "mes": "marzo", "ganancia": 10 }, { "mes": "agosto", "ganancia": 2 }, { "mes": "septiembre", "ganancia":0 }]), [10, 2, 0])
self.assertEqual(ganancias([{ "mes": "marzo", "ganancia": 10 }, { "mes": "agosto", "ganancia": 2 }, { "mes": "septiembre", "ganancia":0 }, { "mes": "diciembre", "ganancia": 8 }]), [10, 2, 0, 8])
self.assertEqual(ganancias([{ "mes": "marzo", "ganancia": 8 }, { "mes": "agosto", "ganancia": 7 }]), [8,7])
```



### Para pensar

¡Excelente! :clap: Ahora ya sabemos cómo transformar cada elemento de una lista para obtener una lista nueva :muscle:. Esta operación es muy común y se conoce como _mapeo_ de una lista.

## 4. ¡Cómo pasan los meses!

¡Ahora que sabemos mapear vamos a practicarlo! :muscle:

> Definí la función `meses` que dada una lista con diccionarios devuelve una lista de meses. :calendar:
>
```python
>>> meses([
    { "mes": "enero", "ganancia": 870 },
    { "mes": "febrero", "ganancia": 1000 },
    { "mes": "marzo", "ganancia": 1020 },
    { "mes": "abril", "ganancia": 2300 },
    { "mes": "mayo", "ganancia": -10 }
  ])
["enero", "febrero", "marzo", "abril", "mayo"]
```



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
self.assertEqual(meses([{ "mes": "enero", "ganancia": 10 }, { "mes": "febrero", "ganancia": 2 }, { "mes": "marzo", "ganancia": 5 }]), ["enero", "febrero", "marzo"])
self.assertEqual(meses([{ "mes": "enero", "ganancia": 10 }, { "mes": "febrero", "ganancia": 2 }, { "mes": "marzo", "ganancia": 5 }, { "mes": "abril", "ganancia": 8 }, { "mes": "mayo", "ganancia": 12 }, { "mes": "junio", "ganancia": 25 }]), ["enero", "febrero", "marzo", "abril", "mayo", "junio"])
```

## 5. Un mapa para comprender

En el ejercicio anterior hicimos un mapeo utilizando `for...in`. En Python contamos con otras formas de hacer eso, ¡las listas por comprensión! :star_struck:

Veamos cómo funcionan, si a partir de una lista de strings quisieramos obtener una lista con los largos de cada uno, podríamos definir:

``` python
def largos(palabras):
  largos = []
  for palabra in palabras:
    list.append(largos, len(palabra))
  return largos
```

Sin embargo, también podríamos hacerlo de esta manera utilizando listas por comprensión:

``` python
def largos(palabras):
  return [len(palabra) for palabra in palabras]
```

> Redefiní la función `meses` para que haga lo mismo que antes pero utilizando listas por comprensión.



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
self.assertEqual(meses([{ "mes": "enero", "ganancia": 10 }, { "mes": "febrero", "ganancia": 2 }, { "mes": "marzo", "ganancia": 5 }]), ["enero", "febrero", "marzo"])
self.assertEqual(meses([{ "mes": "enero", "ganancia": 10 }, { "mes": "febrero", "ganancia": 2 }, { "mes": "marzo", "ganancia": 5 }, { "mes": "abril", "ganancia": 8 }, { "mes": "mayo", "ganancia": 12 }, { "mes": "junio", "ganancia": 25 }]), ["enero", "febrero", "marzo", "abril", "mayo", "junio"])
```



### Para pensar

¡Excelente! :raised_hands:

Lo bueno de conocer más de una manera de hacer lo mismo es que puedas elegir qué herramienta te gusta más para resolver los problemas. :hammer_pick:

## 6. Esto proyecta muy bien

Ana realiza muchas proyecciones sobre los balances de su empresa, por lo que le dijimos que podíamos darle una mano ahora que sabemos mapear. Lo que le interesa hacer es poder ver cuáles serían las ganancias de un balance si todas hubieran sido del doble :moneybag:. Por ejemplo:

``` python
>>> balances_ultimo_semestre = [
	{ "mes": "julio", "ganancia": 50 },
	{ "mes": "agosto", "ganancia": -12 },
	{ "mes": "septiembre", "ganancia": 1000 },
	{ "mes": "octubre", "ganancia": 300 },
	{ "mes":  "noviembre", "ganancia": 200 },
	{ "mes": "diciembre", "ganancia": 0 }
]

>>> doble_de_ganancias(balances_ultimo_semestre)
[100, -24, 2000, 600, 400, 0]
```

Como verás, si las ganancias fueran negativas ahora serán ¡doblemente negativas! :chart_with_downwards_trend:

> Definí la función `doble_de_ganancias`. Podés utilizar tanto `for...in` como listas por comprensión, lo que vos prefieras. :relaxed:



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
self.assertEqual(doble_de_ganancias([{ "mes": "enero", "ganancia": 1000 }, { "mes": "febrero", "ganancia": -200 }, { "mes": "marzo", "ganancia": 500 }]), [2000, -400, 1000])
self.assertEqual(doble_de_ganancias([{ "mes": "enero", "ganancia": -1000 }, { "mes": "febrero", "ganancia": -200 }, { "mes": "marzo", "ganancia": -500 }]), [-2000, -400, -1000])
self.assertEqual(doble_de_ganancias([{ "mes": "enero", "ganancia": 0 }, { "mes": "febrero", "ganancia": 0 }]), [0, 0])
```



### Para pensar

¡Perfecto! :clap:

¿Y si solo quisieramos algunos balances? ¿podemos filtrar utilizando `for...in`? :flushed:

## 7. A filtrar, a filtrar cada cosa en su lugar

Con la programación se puede hacer cualquier cosa, o casi :sweat_smile:. Ya hicimos una función para poder saber la cantidad de balances positivos (`cantidad_de_balances_positivos`), ahora vamos a ver cómo podemos hacer para saber cuáles son esos balances. :calendar:

> Definí la función `balances_positivos` que toma los balances de un período y devuelve una lista con aquellos cuya ganancia fue mayor a cero.




### Pistas

Acá también vas a necesitar empezar con una lista vacía, pero a diferencia de cuando hicimos el mapeo, acá no vas a agregar elementos en cada iteración, solo en algunos casos. :eyes:



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
self.assertEqual(balances_positivos([{ "mes": "marzo", "ganancia": 10 }, { "mes": "agosto", "ganancia": 2 }, { "mes": "septiembre", "ganancia": 8 }]), [{ "mes": "marzo", "ganancia": 10 }, { "mes": "agosto", "ganancia": 2 }, { "mes": "septiembre", "ganancia": 8 }])
self.assertEqual(balances_positivos([{ "mes": "marzo", "ganancia": 10 }, { "mes": "agosto", "ganancia": 2 }, { "mes": "septiembre", "ganancia": 0 }]), [{ "mes": "marzo", "ganancia": 10 }, { "mes": "agosto", "ganancia": 2 }])
self.assertEqual(balances_positivos([{ "mes": "julio", "ganancia": 12 }, { "mes": "agosto", "ganancia": -2 }]), [{ "mes": "julio", "ganancia": 12 }])
self.assertEqual(balances_positivos([{ "mes": "agosto", "ganancia": -12 }, { "mes": "septiembre", "ganancia": 0 }]), [])
```



### Para pensar

¡Muy bien! :raised_hands: Ahora ya sabemos cómo filtrar una lista. En criollo, aprendimos a obtener los elementos de una lista que cumplen una condición determinada. En este caso obtuvimos una nueva lista con los balances que presentaban una ganancia positiva. :moneybag:


## 8. La buena fortuna

¡Practiquemos haciendo un nuevo filtrado! :wink:

> Definí la función `afortunados`, que filtra aquellos balances que tuvieron una ganancia mayor a $1000. :dollar:



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
self.assertEqual(afortunados([{ "mes": "enero", "ganancia": 1000 }, { "mes": "febrero", "ganancia": 2000 }, { "mes": "marzo", "ganancia": 2500 }, { "mes": "abril", "ganancia": 1001 }, { "mes": "mayo", "ganancia": 0 }, { "mes": "junio", "ganancia": -25 }]), [{ "mes": "febrero", "ganancia": 2000 }, { "mes": "marzo", "ganancia": 2500 }, { "mes": "abril", "ganancia": 1001 }])
self.assertEqual(afortunados([{ "mes": "enero", "ganancia": 1000 }, { "mes": "febrero", "ganancia": 0 }, { "mes": "marzo", "ganancia": 200 }, { "mes": "abril", "ganancia": -30 }]), [])
```

## 9. Comprendiendo al filtro

Así como podíamos hacer mapeos utilizando listas por comprensión, también podemos hacer filtrados. :open_hands:

Imaginemos que tenemos la función `mayores_a_5` que dada una lista de números nos retorna una nueva con aquellos que son mayores a 5:

``` python
def mayores_a_5(numeros):
  mayores = []
  for numero in numeros:
    if numero > 5:
      list.append(mayores, numero)
  return mayores
```

Otra manera de definirla sería haciendo:

``` python
def mayores_a_5(numeros):
  return [numero for numero in numeros if numero > 5]
```

> Redefiní la función `afortunados` para que haga lo mismo pero utilizando listas por comprensión.



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
self.assertEqual(afortunados([{ "mes": "enero", "ganancia": 1000 }, { "mes": "febrero", "ganancia": 2000 }, { "mes": "marzo", "ganancia": 2500 }, { "mes": "abril", "ganancia": 1001 }, { "mes": "mayo", "ganancia": 0 }, { "mes": "junio", "ganancia": -25 }]), [{ "mes": "febrero", "ganancia": 2000 }, { "mes": "marzo", "ganancia": 2500 }, { "mes": "abril", "ganancia": 1001 }])
self.assertEqual(afortunados([{ "mes": "enero", "ganancia": 1000 }, { "mes": "febrero", "ganancia": 0 }, { "mes": "marzo", "ganancia": 200 }, { "mes": "abril", "ganancia": -30 }]), [])
```



### Para pensar

¡Excelente! :clap:

También se puede combinar la idea de filtrar y de mapear en las listas por comprensión. Por ejemplo: si quisieramos el doble de los números mayores a 5 podríamos hacer:

``` python
def doble_de_los_mayores_a_5(numeros)
  [numero * 2 for numero in numeros if numero > 5]
```

A modo de resumen, la sintaxis general de las listas por comprensión es `[expresion for elemento in lista if condicion]`. :sunglasses:


## 10. Larguísimo este mes

¿Sabes cuántos tienen 28 días? :thinking:

¡Todos! :stuck_out_tongue_winking_eye:

Fuera del mal chiste, algunos meses son más largos que otros, es por eso que queremos saber de una lista de balances, cuáles corresponden a meses largos. Los meses largos son los que tienen 31 días. Veamos un ejemplo:

``` python
>>> balances_primer_trimestre = [
    { "mes": "enero", "ganancia": 2 },
    { "mes": "febrero", "ganancia": 10 },
    { "mes": "marzo", "ganancia": -20 }
]

>>> balances_de_meses_largos(balances_primer_trimestre)
[{ "mes": "enero", "ganancia": 2 }, { "mes": "marzo", "ganancia": -20 }]
```

> Definí la función `balances_de_meses_largos` que funciona como te mostramos arriba. Podés utilizar `for...in` o listas por comprensión. En ambos casos te va a ser útil el operador `in`.



### Pistas

Por si no te acordás, los meses con 31 días son enero, marzo, mayo, julio, agosto, octubre y diciembre. :calendar_spiral:



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
self.assertEqual(balances_de_meses_largos([{ "mes": "enero", "ganancia": 1000 }, { "mes": "febrero", "ganancia": -200 }, { "mes": "marzo", "ganancia": 500 }, { "mes": "abril", "ganancia": 800 }, { "mes": "mayo", "ganancia": 770 }, { "mes": "junio", "ganancia": 870 }]), [{ "mes": "enero", "ganancia": 1000 }, { "mes": "marzo", "ganancia": 500 }, { "mes": "mayo", "ganancia": 770 }])
self.assertEqual(balances_de_meses_largos([{ "mes": "julio", "ganancia": 500 }, { "mes": "agosto", "ganancia": 900 }, { "mes": "septiembre", "ganancia": 1800 }, { "mes": "octubre", "ganancia": 900 }, { "mes": "noviembre", "ganancia": 2300 }, { "mes": "diciembre", "ganancia": 2000 }]), [{ "mes": "julio", "ganancia": 500 }, { "mes": "agosto", "ganancia": 900 }, { "mes": "octubre", "ganancia": 900 }, { "mes": "diciembre", "ganancia": 2000 }])
self.assertEqual(balances_de_meses_largos([{ "mes": "enero", "ganancia": 1000 }, { "mes": "febrero", "ganancia": -200 }, { "mes": "marzo", "ganancia": 500 }]), [{ "mes": "enero", "ganancia": 1000 }, { "mes": "marzo", "ganancia": 500 }])
self.assertEqual(balances_de_meses_largos([{ "mes": "abril", "ganancia": 800 }, { "mes": "mayo", "ganancia": 770 }, { "mes": "junio", "ganancia": 870 }]), [{ "mes": "mayo", "ganancia": 770 }])
```

## 11. Los mejores meses del año

En ejercicios anteriores ya definimos las funciones `meses` y `afortunados` tanto usando `for...in` como listas por comprensión. :wink:

> Definí la función `meses_afortunados` utilizando listas por comprensión que dada una lista de balances reque nos diga los meses de aquellos que fueron afortunados.





### Pistas

En la `Biblioteca` te dejamos las definiciones de estas funciones que utilizaban listas por comprensión para que recuerdes la lógica.

Pero no podes invocar `meses` ni `afortunados`. Tampoco `for...in`, ¿se te ocurre cómo combinarlas en una nueva lista por comprensión? :thinking:



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
#...solution[5]...#

#...solution[9]...#

self.assertEqual(meses_afortunados([{ "mes": "enero", "ganancia": 1001 }, { "mes": "febrero", "ganancia": -10 }, { "mes": "marzo", "ganancia": 2300 }, { "mes": "abril", "ganancia": 800 }]), ["enero", "marzo"])
self.assertEqual(meses_afortunados([{ "mes": "enero", "ganancia": 999 }, { "mes": "febrero", "ganancia": -10 }, { "mes": "marzo", "ganancia": 20 }, { "mes": "abril", "ganancia": 800 }]), [])
```



### Para pensar

¡Muy bien! :tada:

Si bien esta es una forma de resolver el problema tiene como contra que no aprovechamos las funciones definidas previamente. Vamos a ver otra forma de resolver este problema en el próximo ejercicio. :muscle:

## 12. Afortunadamente

¡Afortunadamente este es el último ejercicio de la lección! :stuck_out_tongue_winking_eye:

Ahora sí, combinemos `meses` y `afortunados` para saber cuáles fueron esos meses en los que nos visitó la buena fortuna. :money_mouth:

> Definí la función `meses_afortunados` que dada una lista de balances devuelve aquellos meses que fueron afortunados. Esta vez no podés usar listas por comprensión.



### Pistas

En este ejercicio no vas a tener que hacer un `for...in`, simplemente invocar correctamente a `meses` y `afortunados`. Para recordarlas podés ver la `Biblioteca`. :relaxed:



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

```python
#...solution[4]...#

#...solution[8]...#

self.assertEqual(meses_afortunados([{ "mes": "enero", "ganancia": 1001 }, { "mes": "febrero", "ganancia": -10 }, { "mes": "marzo", "ganancia": 2300 }, { "mes": "abril", "ganancia": 800 }]), ["enero", "marzo"])
self.assertEqual(meses_afortunados([{ "mes": "enero", "ganancia": 999 }, { "mes": "febrero", "ganancia": -10 }, { "mes": "marzo", "ganancia": 20 }, { "mes": "abril", "ganancia": 800 }]), [])
```



### Para pensar

En esta última lección te reencontraste con el `for...in` y resolviste problemas más complejos con él :exploding_head:. Más especificamente creaste funciones para filtrar y/o transformar los elementos de una lista.

¡Muy buen trabajo! :thumbsup:

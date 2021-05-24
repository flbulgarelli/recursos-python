> Basado en https://github.com/mumukiproject/mumuki-guia-python-logica-booleana

# 2. Lógica booleana

Como ya viste a lo largo de varios ejercicios, cuando programamos trabajamos con booleanos que representan valores de verdad. Podemos operar con ellos mediante lo que denominamos operadores lógicos, como la conjunción y la disyunción. ¡Vamos a aprender un poco más sobre ellos! :muscle:

## 1. Negar no cuesta nada

Empecemos por algo sencillo, ¿te acordás del operador `not` ? Se lo denomina negación o complemento lógico y sirve para negar un valor booleano. Si tengo el booleano representado por `tiene_hambre`, el complemento será `not tiene_hambre`. :no_mouth:

No parece una idea muy interesante pero puede servir para reutilizar la lógica de una función que ya tenemos definida.

Por ejemplo, si contamos con una función `es_par`, basta con negarla para saber si un número es impar.

```python
def es_impar(numero):
  return not es_par(numero)

```

> ¡Ahora te toca a vos! Definí la función `es_mayor_de_edad` y luego `es_menor_de_edad` a partir de ella.




### Pistas

Tanto `es_mayor_de_edad` como `es_menor_de_edad` reciben una edad como argumento. :wink:



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
>>> es_mayor_de_edad(20)
True
>>> es_mayor_de_edad(18)
True
>>> es_mayor_de_edad(17)
False
>>> es_mayor_de_edad(16)
False
>>> es_menor_de_edad(20)
False
>>> es_menor_de_edad(18)
False
>>> es_menor_de_edad(17)
True
>>> es_menor_de_edad(16)
True
````



### Para pensar

Cada una de las funciones representa **un estado de dos posibles**: ser mayor o ser menor de edad. No se puede ser ambos al mismo tiempo y tampoco se puede evitar pertenecer a alguno de los dos grupos y por eso decimos que son complementarios y que juntos forman el _conjunto universal_. :milky_way:

## 2. Peripatéticas

Otro de los operadores con el que ya te encontraste es la conjunción lógica (también llamada _and_), que sólo retorna verdadero cuando las dos expresiones que opera son verdaderas.

Podemos encadenar varias de ellas mediante el operador `and` y si alguna es falsa toda la expresión resultará falsa.

Por ejemplo, si cuento con la función...

```python
 def es_cantante_prolifico(cds_editados, recitales_realizados, grabo_algun_dvd):
  return cds_editados >= 10 and recitales_realizados > 25 and grabo_algun_dvd
```

...basta con que un cantante no haya grabado un DVD para no ser considerado prolífico, incluso aunque haya editado más de 10 CDs y dado más de 25 recitales. :guitar:

> Definí una función `es_peripatetica` que tome el área en que se desempeña una persona, su país de origen y la cantidad de kilómetros que camina por día. Una persona es petipatética cuando se desempeña en filosofía, su país de origen es Grecia y le gusta pasear (camina más de 2 kilómetros por día). Ejemplo:
>
> ```python
> >>> es_peripatetica("filosofía", "Grecia", 5)
True
> >>> es_peripatetica("ingeniería", "Uruguay", 1)
False
> ```




### Pistas

¡No te olvides de las tildes! :eyes:



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
>>> es_peripatetica("filosofia", "Grecia", 3)
False
>>> es_peripatetica("filosofía", "Grecia", 3)
True
>>> es_peripatetica("filosofia", "Grecia", 3) or es_peripatetica("filosofía", "Grecia", 3) or es_peripatetica("filosofía", "grecia", 3) or es_peripatetica("filosofia", "grecia", 3)
True
>>> (es_peripatetica("filosofia", "Grecia", 2) or es_peripatetica("filosofía", "Grecia", 2))
False
>>> es_peripatetica("filosofía", "Argentina", 5)
False
>>> es_peripatetica("atleta", "Grecia", 10)
False
>>> es_peripatetica("profesor", "Colombia", 1)
False
````

## 3. La verdad detrás de la conjunción

En la lógica booleana, se puede definir el comportamiento de un operador con una _tabla de verdad_ donde **A** y **B** son las expresiones o valores de verdad a ser operados y el símbolo **^** representa la conjunción.

<table class="table table-striped table-bordered table-condensed text-center">
  <tr>
    <th class ="text-center" style="width: 75px">A</th>
    <th class ="text-center" style="width: 75px">B</th>
    <th class ="text-center" style="width: 100px">A ^ B</th>
  </tr>
  <tr>
    <td>Verdadero</td>
    <td>Verdadero</td>
    <td>Verdadero</td>
  </tr>
  <tr>
    <td>Verdadero</td>
    <td>Falso</td>
    <td>Falso</td>
  </tr>
  <tr>
    <td>Falso</td>
    <td>Verdadero</td>
    <td>Falso</td>
  </tr>
  <tr>
    <td>Falso</td>
    <td>Falso</td>
    <td>Falso</td>
  </tr>
</table>

En el mundo de la lógica estas expresiones se llaman _proposiciones_. Pero… ¿qué cosas pueden ser una proposición? :thought_balloon: Sólo hace falta que tengan un valor de verdad, es decir, cualquier expresión booleana puede ser una proposición.

> Para comprobarlo, probá en la consola tu función `es_peripatetica` con los siguientes valores y comprobá si se comporta como en la tabla:
>
> ```python
>>> es_peripatetica("atletismo", "Argentina", 10)
>>> es_peripatetica("filosofía", "Argentina", 3)
>>> es_peripatetica("ingeniería", "Canadá", 1)
>>> es_peripatetica("filosofía", "Grecia", 5)
```



### Para pensar

Como podrás ver, sólo `es_peripatetica("filosofía", "Grecia", 5)` es verdadera porque cumple las tres condiciones, o dicho de otra forma, todas sos proposiciones son verdaderas. :nerd:

## 4. ¡Juguemos al T.E.G.!

¿Y si basta con que una de varias condiciones se cumpla para afirmar que una expresión es verdadera? Podemos utilizar otro de los operadores que ya conocés, ¡la disyunción lógica `or`! :bulb:

En el famoso juego T.E.G., un jugador puede ganar de dos formas: cumpliendo su objetivo secreto o alcanzando el objetivo general de conquistar 30 países:

```python
def gano(cumplio_objetivo_secreto, cantidad_de_paises_conquistados):
  return cumplio_objetivo_secreto or cantidad_de_paises_conquistados >= 30

```

> Probá en la consola las siguientes expresiones:
>
``` python
>>> gano(True, 25)
>>> gano(False, 30)
>>> gano(False, 20)
>>> gano(True, 31)
```

> ¿Te animás a construir la tabla de verdad de la disyunción lógica?




### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
def gano(cumplio_objetivo_secreto, cantidad_de_paises_conquistados):
  return cumplio_objetivo_secreto or cantidad_de_paises_conquistados >= 30


````



### Para pensar

Vamos a ver como sería la tabla de verdad de la disyunción para compararla con la tuya:

<table class="table table-striped table-bordered table-condensed text-center">
  <tr>
    <th class ="text-center" style="width: 75px">A</th>
    <th class ="text-center" style="width: 75px">B</th>
    <th class ="text-center" style="width: 100px">A v B</th>
  </tr>
  <tr>
    <td>Verdadero</td>
    <td>Verdadero</td>
    <td>Verdadero</td>
  </tr>
  <tr>
    <td>Verdadero</td>
    <td>Falso</td>
    <td>Verdadero</td>
  </tr>
  <tr>
    <td>Falso</td>
    <td>Verdadero</td>
    <td>Verdadero</td>
  </tr>
  <tr>
    <td>Falso</td>
    <td>Falso</td>
    <td>Falso</td>
  </tr>
</table>

## 5. Y ahora... ¿quién podrá ayudarnos?

¿Nunca te pasó haber querido hacer algún trámite en el banco y llegar sólo para darte cuenta de que estaba cerrado? A Dory :tropical_fish: sí, por lo que vamos a desarrollar una función que ayude a la gente despistada como ella.

Sabemos que el banco está abierto los días de semana que no es feriado, y estamos dentro del horario bancario.

Ya están definidas las funciones:

* `dentro_de_horario_bancario`: recibe un horario :clock10: (una hora en punto que puede ir desde las 0 hasta las 23) y nos dice si está dentro de la franja de atención del banco.
* `es_fin_de_semana`: recibe un día y nos dice si es "sábado" o "domingo".

> Definí la función `es_dia_de_semana` y luego completá `esta_abierto`.




### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
def dentro_de_horario_bancario(horario):
  return horario >= 10 and horario <= 15

def es_fin_de_semana(dia):
  return dia == "sábado" or dia == "domingo"

>>> esta_abierto(True, "lunes", 14)
False
>>> esta_abierto(True, "miércoles", 20)
False
>>> esta_abierto(False, "jueves", 13)
True
>>> esta_abierto(False, "sábado", 11)
False
>>> esta_abierto(False, "domingo", 19)
False
>>> esta_abierto(False, "martes", 16)
False
````

## 6. ¡Buen día!

Todos sabemos que el seguimiento de árboles genealógicos puede tornarse complicado cuando hay muchas personas y relaciones involucradas.

En la familia Buendía ocurre que:

* Arcadio es hijo de José Arcadio y de Pilar Ternera,
* Aureliano José es hijo del Coronel Aureliano y Pilar Ternera,
* Aureliano Segundo y Remedios son hijos de Arcadio y Sofía De La Piedad.

Nosotros definimos por vos las funciones `madre_de` y `padre_de`:

```python
>>> padre_de(aureliano_jose)
"Coronel Aureliano"
>>> madre_de(aureliano_segundo)
"Sofía De La Piedad"
```

> Ahora te toca a vos definir la función `son_medio_hermanos`. Recordá que los medios hermanos pueden compartir madre o padre pero no ambos porque... ¡en ese caso serían hermanos! :sweat_smile:




### Pistas

Quizás te sirva definir las funciones `tienen_la_misma_madre` y `tienen_el_mismo_padre`.




### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
maria_de_los_remedios = {
  'nombre': "María De Los Remedios"
}

pedro_ternera = {
  'nombre': "Pedro Ternera"
}

sofia_montiel = {
  'nombre': "Sofía Montiel"
}

arturo_de_la_piedad = {
  'nombre': "Arturo De La Piedad"
}

pilar_ternera = {
  'nombre': "Pilar Ternera",
  'madre': maria_de_los_remedios,
  'padre': pedro_ternera
}

ursula_iguaran = {
  'nombre': "Úrsula Iguarán"
}

jose_arcadio_padre = {
  'nombre': "José Arcadio"
}

juan_perez = {
  'nombre': "Juan Perez"
}

maria_rodriguez = {
  'nombre': "Maria Rodriguez"
}

dora_ramirez = {
  'nombre': "Dora Ramirez"
}

felipe_perez = {
  'nombre': "Felipe Perez",
  'madre': maria_rodriguez,
  'padre': juan_perez
}

martin_perez = {
  'nombre': "Martín Perez",
  'madre': dora_ramirez,
  'padre': juan_perez
}

jose_arcadio = {
  'nombre': "José Arcadio",
  'madre': ursula_iguaran,
  'padre': jose_arcadio_padre
}

coronel_aureliano = {
  'nombre': "Coronel Aureliano",
  'madre': ursula_iguaran,
  'padre': jose_arcadio_padre
}

sofia_de_la_piedad = {
  'nombre': "Sofía De La Piedad",
  'madre': sofia_montiel,
  'padre': arturo_de_la_piedad
}

arcadio = {
  'nombre': "Arcadio",
  'madre': pilar_ternera,
  'padre': jose_arcadio
}

aureliano_jose = {
  'nombre': "Arcadio",
  'madre': pilar_ternera,
  'padre': coronel_aureliano
}

aureliano_segundo = {
  'nombre': "Aureliano Segundo",
  'madre': sofia_de_la_piedad,
  'padre': arcadio
}

remedios = {
  'nombre': "Remedios",
  'madre': sofia_de_la_piedad,
  'padre': arcadio
}

def madre_de(persona):
  return persona['madre']['nombre']


def padre_de(persona):
  return persona['padre']['nombre']

>>> son_medio_hermanos(arcadio, aureliano_jose)
True
>>> son_medio_hermanos(aureliano_segundo, remedios)
False
>>> son_medio_hermanos(aureliano_segundo, aureliano_jose)
False
>>> son_medio_hermanos(remedios, arcadio)
False
>>> son_medio_hermanos(felipe_perez, martin_perez)
True
````

## 7. La verdad es que no hay una verdad

Ahora pensemos cómo sería la tabla de verdad que representa el comportamiento de la función que acabás de hacer.

Las proposiciones serán `tienen_la_misma_madre` y `tienen_el_mismo_padre`, y los valores de verdad que porten dependerán de qué dos personas estén evaluando.

El booleano final resultará de operarlas mediante `son_medio_hermanos`:

<table class="table table-striped table-bordered table-condensed text-center">
  <tr>
    <th class ="text-center" style="padding: 5px 8px">tienen la misma madre</th>
    <th class ="text-center" style="padding: 5px 8px">tienen el mismo padre</th>
    <th class ="text-center" style="padding: 5px 8px">son medios hermanos</th>
  </tr>
  <tr>
    <td>True</td>
    <td>True</td>
    <td>False</td>
  </tr>
  <tr>
    <td>True</td>
    <td>False</td>
    <td>True</td>
  </tr>
  <tr>
    <td>False</td>
    <td>True</td>
    <td>True</td>
  </tr>
  <tr>
    <td>False</td>
    <td>False</td>
    <td>False</td>
  </tr>
</table>

> Probá tu función `son_medio_hermanos` con los siguientes valores y comprobá si se comporta como la tabla:
>
```python
>>> son_medio_hermanos(aureliano_segundo, remedios)
>>> son_medio_hermanos(aureliano_jose, remedios)
>>> son_medio_hermanos(arcadio, aureliano_jose)
```



### Pistas

Recordá que en la familia Buendía:

* Arcadio es hijo de José Arcadio y de Pilar Ternera,
* Aureliano José es hijo del Coronel Aureliano y Pilar Ternera,
* Aureliano Segundo y Remedios son hijos de Arcadio y Sofía De La Piedad.




### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
maria_de_los_remedios = {
  'nombre': "María De Los Remedios"
}

pedro_ternera = {
  'nombre': "Pedro Ternera"
}

sofia_montiel = {
  'nombre': "Sofía Montiel"
}

arturo_de_la_piedad = {
  'nombre': "Arturo De La Piedad"
}

pilar_ternera = {
  'nombre': "Pilar Ternera",
  'madre': maria_de_los_remedios,
  'padre': pedro_ternera
}

ursula_iguaran = {
  'nombre': "Úrsula Iguarán"
}

jose_arcadio_padre = {
  'nombre': "José Arcadio"
}

jose_arcadio = {
  'nombre': "José Arcadio",
  'madre': ursula_iguaran,
  'padre': jose_arcadio_padre
}

coronel_aureliano = {
  'nombre': "Coronel Aureliano",
  'madre': ursula_iguaran,
  'padre': jose_arcadio_padre
}

sofia_de_la_piedad = {
  'nombre': "Sofía De La Piedad",
  'madre': sofia_montiel,
  'padre': arturo_de_la_piedad
}

arcadio = {
  'nombre': "Arcadio",
  'madre': pilar_ternera,
  'padre': jose_arcadio
}

aureliano_jose = {
  'nombre': "Arcadio",
  'madre': pilar_ternera,
  'padre': coronel_aureliano
}

aureliano_segundo = {
  'nombre': "Aureliano Segundo",
  'madre': sofia_de_la_piedad,
  'padre': arcadio
}

remedios = {
  'nombre': "Remedios",
  'madre': sofia_de_la_piedad,
  'padre': arcadio
}

def madre_de(persona):
  return persona['madre']['nombre']


def padre_de(persona):
  return persona['padre']['nombre']

def tienen_el_mismo_padre(una, otra):
  return padre_de(una) == padre_de(otra)


def tienen_la_misma_madre(una, otra):
  return madre_de(una) == madre_de(otra)


def son_medio_hermanos(una, otra):
  return tienen_la_misma_madre(una, otra) and not tienen_el_mismo_padre(una, otra) or not tienen_la_misma_madre(una, otra) and tienen_el_mismo_padre(una, otra)


````

## 8. ¡Hola! Mi nombre es Xor

Ahora cambiemos las funciones `tienen_la_misma_madre` y `tienen_el_mismo_padre` por proposiciones genéricas **A** y **B**. Además, representemos la operación que realiza `son_medio_hermanos` con el símbolo **⊻**. Lo que obtenemos es... ¡una nueva tabla! :tada:

<table class="table table-striped table-bordered table-condensed text-center">
  <tr>
    <th class ="text-center" style="width: 75px">A</th>
    <th class ="text-center" style="width: 75px">B</th>
    <th class ="text-center" style="width: 100px">A ⊻ B</th>
  </tr>
  <tr>
    <td>Verdadero</td>
    <td>Verdadero</td>
    <td>Falso</td>
  </tr>
  <tr>
    <td>Verdadero</td>
    <td>Falso</td>
    <td>Verdadero</td>
  </tr>
  <tr>
    <td>Falso</td>
    <td>Verdadero</td>
    <td>Verdadero</td>
  </tr>
  <tr>
    <td>Falso</td>
    <td>Falso</td>
    <td>Falso</td>
  </tr>
</table>

Este comportamiento existe como un operador dentro de la lógica y se lo denomina `xor` o disyunción lógica excluyente.

A diferencia del `and`, `or` y `not`, el `xor` no suele estar definido en los lenguajes. :cry: Sin embargo, ahora que sabés cómo funciona, si alguna vez lo necesitás podés definirlo a mano. :wink:

> Veamos si se entiende: definí la función genérica `xor`, que tome dos booleanos y devuelva el valor de verdad correspondiente.




### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
>>> xor(True, True)
False
>>> xor(True, False)
True
>>> xor(False, True)
True
>>> xor(False, False)
False
````

## 9. Precedencia

Cuando una expresión matemática tiene varios operadores, sabemos que las multiplicaciones y divisiones se efectuarán antes que las sumas y las restas:

```python
5 * 3 + 8 / 4 - 3 = 14
```

Al igual que en matemática, cuando usamos operadores lógicos las expresiones se evalúan en un orden determinado llamado _precedencia_.

¿Cuál es ese orden? :thinking:

Teniendo definida la función:

```python
def paga_con_tarjeta(se_cobra_interes, tarjeta, efectivo_disponible):
  return not se_cobra_interes and cuotas(tarjeta) >= 3 or efectivo_disponible < 100
```

> Intentá descubrir cuál es la precedencia de las operaciones booleanas. Te damos unos ejemplos de pruebas...
>
``` python
>>> paga_con_tarjeta(True, "visa", 320)
>>> paga_con_tarjeta(False, "visa", 80)
>>> paga_con_tarjeta(True, "mastercard", 215)
>>> paga_con_tarjeta(True, "mastercard", 32)
```
> ... pero podés probar con los que vos quieras.

> Cuando termines, escribí `listo()`.



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
def listo():
  pass

def cuotas(tarjeta):
  return {
    'visa': 6,
    'mastercard': 2,
  }.get(tarjeta, 1)

def paga_con_tarjeta(se_cobra_interes, tarjeta, efectivo_disponible):
  return not se_cobra_interes and cuotas(tarjeta) >= 3 or efectivo_disponible < 100


````



### Para pensar

¿Descifraste la precedencia de las operaciones booleanas? :thinking: Por las dudas acá tenemos un cuadro con la precedencia de ellas y de algunas operaciones que vimos (y otras que no):


<table class="table table-striped table-bordered table-condensed text-center">
  <tr>
    <th class ="text-center" style="width: 10px">Prioridad</th>
    <th class ="text-center" style="width: 75px">Operaciones</th>
    <th class ="text-center" style="width: 75px">Descripción</th>
  </tr>
  <tr>
    <td>1</td>
    <td>**</td>
    <td>Exponenciación</td>
  </tr>
  <tr>
    <td>2</td>
    <td>*,  /,  %</td>
    <td>Multiplicación, división, resto</td>
  </tr>
  <tr>
    <td>3</td>
    <td>+,  -</td>
    <td>Suma, resta</td>
  </tr>
  <tr>
    <td>4</td>
    <td>in,  <,  <=,  >,  >=,  ==,  !=</td>
    <td>Pertenencia, comparaciones</td>
  </tr>
  <tr>
    <td>5</td>
    <td>not</td>
    <td>Negación lógica</td>
  </tr>
  <tr>
    <td>6</td>
    <td>and</td>
    <td>Conjunción lógica</td>
  </tr>
  <tr>
    <td>7</td>
    <td>or</td>
    <td>Disyunción lógica</td>
  </tr>
</table>

En esta tabla la precedencia va de mayor a menor, es decir, la prioridad 1 es la mayor y la prioridad 7 es la menor. Por ejemplo, si hacemos...

``` python
8 + 2 * 3 < 15 and not 5 == 4
```

... obtendremos `True` ya que resuelve las operaciones en este orden:

1. `2 * 3` que retorna `6` entonces: `8 + 6 < 15 and not 5 == 4`
2. `8 + 6` que retorna `14` entonces: `14 < 15 and not 5 == 4`
3. `14 < 15` que retorna `True` entonces: `True and not 5 == 4`
4. `5 == 4` que retorna `False` entonces: `True and not False`
5. `not False` que retorna `True` entonces: `True and True`
6. `True and True` que finalmente retorna `True`.

## 10. Un ejercicio sin precedentes

Ya comprobaste que la operación con mayor precedencia es la negación, seguida de la conjunción y la disyunción pero ¿qué pasa si quiero alterar el orden en que se resuelven? :thought_balloon:

Al igual que en matemática, podemos usar paréntesis para agrupar las operaciones que queremos que se realicen primero.

> Definí la función `puede_jubilarse` que recibe la edad y el sexo de una persona, además de los años de aportes jubilatorios que posee:

> ```python
> >>> puede_jubilarse(62, 'F', 34)
> True
> ```

> El mínimo de edad para realizar el trámite para las mujeres es de 60 años, mientras que para los hombres es 65. En ambos casos, se deben contar con al menos 30 años de aportes.


> Ah, y por esta vez te vamos a pedir que no definas funciones extra para resolverlo. :see_no_evil:




### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
>>> puede_jubilarse(62, 'F', 40)
True
>>> puede_jubilarse(63, 'F', 25)
False
>>> puede_jubilarse(58, 'F', 35)
False
>>> puede_jubilarse(69, 'F', 40)
True
>>> puede_jubilarse(66, 'M', 40)
True
>>> puede_jubilarse(63, 'M', 35)
False
>>> puede_jubilarse(68, 'M', 26)
False
>>> puede_jubilarse(58, 'M', 35)
False
````



### Para pensar

¿Y si delegamos? Podríamos separar la lógica de la siguiente manera:

```python
def puede_jubilarse(edad, sexo, anios_aportes):
  return cumple_edad_minima(edad, sexo) and tiene_suficientes_aportes(anios_aportes)
```

**Al delegar correctamente**, hay veces en las que no es necesario alterar el orden de precedencia, ¡otro punto a favor de la delegación! :muscle:


## 11. ¿Puedo subir?

En un parque de diversiones de la ciudad instalaron una nueva montaña rusa :roller_coaster: y nos pidieron ayuda para que le digamos a las personas si pueden subirse o no antes de hacer la fila. Los requisitos para subir a la atracción son:

* Alcanzar la altura mínima de 1.5m (o 1.2m si está acompañada por un adulto).
* No tener ninguna afección cardíaca.

> Definí la función de 3 parámetros `puede_subirse` que recibe la altura de una persona en metros, si está acompañada por un adulto y si tiene alguna afección cardíaca. Ejemplo:
>
> ```python
> >>> puede_subirse(1.7, False, True)
> False # no puede subirse
>       # porque aunque tiene mas de 1.5m,
>       # tiene una afección cardíaca
> ```




### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
>>> puede_subirse(1.5, False, False)
True
>>> puede_subirse(1.7, False, True)
False
>>> puede_subirse(1.2, True, False)
True
>>> puede_subirse(1.2, False, False)
False
>>> puede_subirse(1.1, True, False)
False
````


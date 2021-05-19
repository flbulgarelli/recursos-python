# Paradigmas de programación

# Introducción a la programación con objetos

Programación Imperativa / Programación Procedural

```
Problema: 🥟 Preparar Empanadas
  Paradigma De Cocinar en Casa (PCC)
    Necesitamos:
      - ingredientes
      - horno
      - tiempo
      - conocimiento (receta)
      - heladera: guardar ingredientes

  Paradigma de Pedir Afuera (PPA)
    Necesitamos:
      - plata
      - aplicacion / telefono
      - heladera: repositorio de imanes/telefono
    Ventaja:
      - mas facil
    Desventaja:
      - Tenemos menos control
```

```
Problema: 🖥️ Programar
  Paradigma Imperativo/Procedural
    Necesitamos:
      ifs
      procedimientos
      funciones
      variables

  Paradigma Orientado a Objetos:
    Necesitamos:
      if
      variable
```

## Objetos y mensajes

Somos ornitólogos y ornitólogas que estudiamos el comportamiento de las aves, y Pepita es una golondrina.

```python
from aves import pepita
```

¿Qué sabe hacer pepita? ¿Sabe volar_en_circulos?

```
>> pepita.volar_en_circulos()
```

¿Sabe cantar_boleros?

```
>> pepita.cantar_boleros()
# AttributeError: 'Golondrina' object has no attribute 'cantar_boleros'
```

Ups, no 😛. ¿Y sabe comer_alpiste?

```
>> pepita.comer_alpiste()
# TypeError: comer_alpiste() missing 1 required positional argument: 'gramos'
```

Ups, sí, pero tenemos que decirle cuantos gramos de alpiste queremos que coma

```
>> pepita.comer_alpiste(10)
```

> 💡Formalización: `pepita` es un objeto, y como todo **objeto**, entiende algunos **mensajes**.
> En particular, nuestra golondrina entiende los mensajes `comer_alpiste` y `volar_en_circulos`,
> pero no entiende `cantar_boleros` (ni casi ninguna otra cosa que se te ocurra :wink:)
> En otras palabras, `pepita` _sabe_ comer alpiste y volar en circulos.
>
> Por otro lado, si le pedimos a un objeto que haga cosas que no sabe hacer, éste se rehusará.

¿Y qué pasa cuando le _enviamos_ estos mensajes? `pepita` no tiene infinita energía para hacer todo lo que le pidamos, sino que sabe cuanta es la `energia` que le queda:

```python
>> pepita.energia
```

> 🎯 Sabiendo esto, ¿te animás a averiguar cómo queda la energia después de hacerla comer alpiste? ¿y después de hacerla volar en círculos?

Como vemos, cada vez que hacemos que pepita coma y vuele, su energia cambia.

> 💡 Formalización: los objetos pueden tener **estado** (en el caso de pepita, su estado es la energía), el cual puede cambiar a lo largo del tiempo.


> 🎯 ¿Te animás a averiguar según qué formula?


> 💡 Formalización: cada vez que un objeto recibe un mensaje, _hace_ algo, reaccionando al mismo. Por tanto, decimos que los objetos tienen un cierto _comportamiento_ (por ejemplo, cuando pepita come alpiste, su energia sube en tantas unidades como los gramos ingeridos)

## Ambiente e interfaces

`pepita` no es nuestra única golondrina. También contamos con `anastasia`:

```python
>> pepita == anastasia
False
```

Como vemos, aunque las dos son golondrinas, no son el mismo objeto, y por eso si las comparamos con `==` nos dará `False`. De hecho, un objeto sólo es _idéntico_ a sí mismo.

```python
>> pepita == pepita
True
```

> 💡 Formalización: la **identidad** es la propiedad por la que los objetos "saben" que son diferentes a los demás.

¿Y que hay de su energía? ¿Tendrá lan misma?

```
>> pepita.energia
100
>> anastasia.energia
200
```

`anastasia` es otro objeto, y como tal, cuenta con su propio estado. Por eso es que si bien las dos tienen `energia`, presentan valores diferentes. ¿Qué cosas sabrá hacer `anastasia`?


```python
>> anastasia.volar_en_circulos()
>> anastasia.comer_alpiste(10)
```

Como `anastasia` es otra golondrina, sabe hacer las mismas cosas que `pepita`.

> 💡 Formalización: llamaremos _ambiente_ al contexto en el que el viven los objetos, tienen su estado y pueden entender mensajes. En un mismo ambiente podemos contar con varios objetos, como por ejemplo, `pepita` y `anastasia`.
>
> En otras palabras es el mundo que los objetos habitan 🌎 y en que se relacionan . Cada vez que apretamos play en replit, o le damos reset en colab, o cerramos nuestro intérprete de python en nuestra computadora y lo volvemos a iniciar, estamos destruyendo ese mundo y volviendo a empezar.

Pero no sólo contamos con `pepita` y `anastasia`, sino también con `roberta`. ¿Cuánta energía tendrá inicialmente?

```python
>> roberta.energia
```

😮 Ohh, ¡tiene mucha energia! Y también sabrá volar en círculos, ¿no?

```python
>> roberta.volar_en_circulos()
>> roberta.energia
```

Bien, aunque como vemos perdió sólo una unidad de energía, pese a que anastasia y pepita gastan 10 al hacerlo.
Parece que las tres saben hacer lo mismo, pero roberta lo hace de forma _diferente_.

> 💡 Formalización: no todos los objetos tienen que reaccionar de igual forma a los mismos mensajes. En otras palabras, no todos los objetos tienen por qué comportarse igual.

¿Y qué hay sobre `comer_alpiste`?

```python
>> roberta.comer_alpiste(10)
```

Ey, ¡no le gusta el alpiste! Pero nos dijeron que sí le gusta comer peces:

```python
>> roberta.comer_peces(2)
>> roberta.energia
```

> 💡 Formalización: no todos los objetos tienen qué entender los mismos mensajes. Por ejemplo `roberta` no entiende `comer_alpiste`, pero sí entiende `comer_peces` (que anastasia y pepita no entienden, si no nos creés podés comprobarlo vos :smile:). Al conjunto de mensajes que cada objeto expone lo llamaremos **interfaz**, la cual puede ser (y típicamente será) diferente para cada objeto.

Qué rara es nuestra nueva golondrina, ¿no? ¡Es que no es una Golondrina! ¡Es un dragón! 🔥

```python
>> roberta.escupir_fuego()
```

Perdón, esperamos no haber quemado nada 🙈


## Interfaces compartidas

Entonces, ¿`pepita` y `roberta` se comportan igual? ¡No! ¿Y tienen la misma interfaz? ¡Tampoco!
Pero sí tienen una parte común; en otras palabras comparten (parcialmente) una interfaz:


|              | 🌾 `comer_alpiste` | 🐟 `comer_peces` | 🔥 `escupir_fuego` | ✈️ `volar`| 🔄 `volar_en_circulos`|
|:------------:|:----------------:|:-------------:|:-------------:|:------:|:------------------:|
| `pepita`     |   ✅️             |               |               | ✅️     | ✅️                 |
| `anastasia`  |   ✅️             |               |               | ✅️     | ✅️                 |
| `roberta`    |                  |✅️             |✅️             | ✅️     | ✅️                 |


## Clases

Momento, ¿y cómo están definidas `pepita`, `anastasia`  y `roberta`? ¿Dónde dice _qué_ saber hacer cada una y _cómo_?

En el paradigma de objetos, los mismos se crean a partir de _moldes_ llamados **clases**, que sirven para dar vida a objetos que se comporten de igual forma. Por ejemplo nuestras golondrinas `pepita` y `anastasia` se crearán de la siguiente forma....

```
pepita = Golondrina(100)
anastasia = Golondrina(200)
```

... partir de una clase llamada `Golondrina` que se verá así:


```python
class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms
```


> 💡 Formalización: al acto de crear un objeto a partir de una clase se lo denomina _instanciación_, y por tanto a los objetos también se los denomina _instancias_ (de una clase particular). Por ejemplo, `pepita`  es una instancia (de la clase `Golondrina`).
>
> Si bien el término _instancia_ quizás no nos diga mucho, en este contexto significa "ejemplo", dado que cada golondrina como pepita o anastasia son ejemplo concretos (es decir, casos particulares) de la idea más general de una `Golondrina`.

Como vemos, una clase es nuevo tipo de definición, que se suma a las funciones y procedimientos que ya conocíamos. Se escribe mediante la palabra reservada `class`, seguida de un nombre y `:`. Dentro de ella encontraremos los métodos, que son el código que especifica cómo se comportará un objeto cuando reciba un mensaje.

> 📝 Nota: sí, los métodos se definen usando la misma palabra clave `def` que usabamos para funciones y procedimientos. Sin embargo, no son lo mismo: como podemos ver los métodos siempre están "dentro" de una clase, y además tienen como primer parámetro `self`. Más sobre esto, en breve.

## Parecidos pero distintos: métodos vs funciones

Tomemos este método como ejemplo:

```python
class Golondrina:
  def comer_alpiste(self, gramos):
    self.energia = self.energia + 4 * gramos
```

👀 Ojo, porque los métodos y las funciones, si bien se ven parecidos, no son lo mismo.

1. Las funciones se invocan como `funcion(argumentos)`, pero los métodos se evaluan a través el envio de mensajes como `objeto.mensaje(argumentos)`
2. los métodos tienen siempre declaran como primer parámetro `self`, las funciones no
3. los métodos siempre van dentro de un `class`, mientras que las funciones van por fuera

## ¿Quien soy yo?

Habrán notado que una diferencia importante entre una función y un método es el parámetro
`self` (en inglés, _si mismo_) que reciben todos los métodos en su definición. Este parámetro representa al objeto receptor del mensaje, y Python lo pasará automáticamente siempre que enviemos uno.

Por ejemplo cuando hagamos...

```python
>> pepita.comer_alipste(10)
```
... Python pasará automáticamente a `pepita` a través del parámetro `self`. Y si hacemos...

```python
>> anastasia.comer_alipste(10)
```

... `self` representará a `anastasia`. Esto nos permite que definamos métodos que accedan al estado del objeto que está recibiendo el mensaje (como en `comer_alpiste`) o que le enviemos más mensajes (como en `volar_en_circulos`, que envía a `self` el mensaje `volar`).

## Un poco de práctica

Ahora te toca a vos:

1. Creá a la golondrina `maria` con 42 puntos de energía inicial
2. Creá al dragón `chimuelo`, con 200 dientes y 1000 de energía inicial
3. Definí el método `esta_debil`, que nos dice si nuestras "aves" tiene menos de 10 puntos de energia (golondrinas) o menos de 50 puntos de energía (dragones)
4. Definí el método `esta_feliz`, que nos dice si nuestras "aves" tiene más de 500 puntos de eneria (sin importar de qué clase sean)
5. Hace a `hipo`, entrenador de dragones: sabe aceptar a dragones, quienes son sus entrenados y hacerlos entrenar todos los dias, haciendoles dar 20 vueltas en circulos y luego comer su comida favorita hasta saciarse (3 peces)
6. Hacé que hipo pueda entrenar a las golondrinas. ¿Qué comportamiento deberían entender las golondrinas ahora?
7. Definí el m[etodo `entrenamiento_intensivo`, que hace dar vultas en circulos a sus entrenados hasta que estén débiles.

## Constructores

Hacemos un alto en el camino para entender los constructores.

## Herencia

¿Ves algo repetido entre las golondrinas y los dragones? Sí, ¡el método `está_feliz`! Extraigamos la lógica común a una clase `AnimalAlado`.

```python
class AnimalAlado:
  def esta_feliz(self):
    return self.energia >= 500

class Golondrina(AnimalAlado):

  ... etc ...

class Dragon(AnimalAlado):

  ... etc ...
```

Diremos además que esta clase es una _clase abstracta_, porque no existe para tener instancias directas.


## _Por panamericana_

Ah, pero no tan rápido. Ahora te toca a vos: implementá el método `volar_por_panamericana` que nos permite decirle a un animal alado que vuele hasta un cierto lugar a lo largo de ciudades de la Ruta Panamericana. Tené en cuenta algunos puntos notables de la ruta:

* Ushuaia es el km 0
* Buenos Aires es el km 3078
* Valparaiso (Chile) es el km 4533
* Bahía Prudhoe (Alaska) es el km 17958.

> Para pensar: ¿tiene algo _raro_ este nuevo método?

## Aflojá con el aparatito

¡Integremos lo visto con otra situación!

Es innegable que en la actualidad los dispositivos electrónicos atraviesan nuestro día a día :electric_plug:. Desde celulares :iphone: hasta _notebooks_:computer: que están presentes tanto en nuestro ocio como en nuestros trabajos o estudios. Es por eso que vamos a modelar distintos dispositivos utilizando la programación con objetos.

Para entrar en calor vamos a modelar la clase `Celular`, ¿qué sabemos de ellos?

* Todos los celulares tienen su `bateria` en 100 inicialmente;
* Cuando utilizamos un `Celular`, su batería disminuye en la mitad de los minutos que lo hagamos. Por ejemplo: si usamos el celular 30 minutos, su batería bajará en 15.
* Los celulares se pueden `cargar_a_tope` para dejar la batería en 100.

> Definí la clase `Celular` y también los métodos `__init__`, `utilizar` y `cargar_a_tope`.
> No nos vamos a preocupar por ahora en que tenga suficiente `bateria` para poder utilizarlo. :wink:

¡Ahora es el turno de la `Notebook`! :computer:

La clase `Notebook` entiende los mismos mensajes que `Celular` y se comporta parecido pero no exactamente igual. La diferencia está en que a la hora de `utilizar` una notebook, su `bateria` disminuye en la cantidad de minutos que la utilicemos.

> Definí la clase `Notebook`, que sepa entender los mensajes `__init__`, `utilizar` y `cargar_a_tope`.

Sí, definitivamente `Celular` y `Notebook` tienen comportamiento repetido. :face_with_raised_eyebrow:

> Para pensar: ¿qué métodos son iguales en ambas clases?
>
> Con esto en cuenta, definí una clase abstracta común y modificá las clases que definiste anteriormente para evitar que haya métodos repetidos entre `Celular` y `Notebook`. ¿Como la llamarías?

Una de las grandes molestias que nos traen los dispositivos electrónicos es cuando se quedan sin batería. :battery:
Sabemos que tanto los celulares como las notebooks están descargados si tienen 20 o menos de batería. :electric_plug:

> Definí el método `descargado` en donde corresponda.

¿Funciona todo esto que estuvimos haciendo?

> Probá en la consola los siguientes comandos:

```python
un_celu = Celular()
una_notebook = Notebook()
un_celu.descargado()
un_celu.utilizar(180)
un_celu.descargado()
una_notebook.utilizar(100)
una_notebook.cargar_a_tope()
una_notebook.descargado()
```

Ah, pero nos estabamos olvidando de algo fundamental: Lu usa todos los días todos sus dispositivos (con tanta virtualidad no podría ser de otra forma) y necesita recargarlos en su mesita de luz antes de irse a dormir.

> Modelá esta situación, para Lu (o cualquier otra persona dueña de aparatitos electrónicos) pueda cargar a tope todos sus dispositivos en un solo comando.
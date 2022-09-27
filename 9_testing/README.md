
# Introducción al _testing_

¡Hola! Hasta ahora venimos programando sin parar, y en mas de una ocasión nuestro código no ha funcionado como lo deseabamos. Quizás teníamos mal escrito el nombre de una función o una variable y se producía un `NameError`. O quizás, cometíamos un error de sintaxis y nos topabamos con un `SintaxError`. O peor aún: nuestro código no lanzaba ningún error, pero sin embargo no hacía lo que debía: una cuenta era incorrecta, faltaba o sobraba un elemento en una lista, y así.

De hecho, es incluso posible que _rara vez_ nuestros programas hayan hecho lo que deben en el primer intento y hayamos tenido que escribirlo y reescribirlo varias veces hasta lograr el resultado deseado. En definitiva, _errar es humano_ y debemos preparanos para ello. ¡Por eso mismo siempre debemos probar nuestro código! Por ejemplo, si dentro de un archivo `descuento.py` tenemos una función como la siguiente...

```python
def aplicar_descuento_2x1(cantidad, precio_base):
  """
  Aplica el descuento 2 X 1 a un precio: los pares de productos los cobra a la mitad de precio
  """
  if cantidad % 2 == 0:
    return precio_base * cantidad / 2
  else:
    return precio_base * (cantidad - 1) / 2
```

...¿cómo la probaríamos? La forma más sencilla es cargarla en nuestro intérprete con `python -i descuento.py` y luego _someterla_  a diferentes pruebas:

  * Si la cantidad es cero, el precio debería ser cero, sin importar la cantidad
  * Si la cantidad es 2 y el precio base es $100, el precio final debería ser $100
  * Si la cantidad es 4 y el precio base es $150, el precio final debería ser $300
  * Si la cantidad es 1 y el precio base es $200, el precio final debería ser $200 (no hubo descuento)
  * etc...

Esto lo podríamos _traducir_ así:


```python
>>> aplicar_descuento_2x1(0, 450)
0.0
>>> aplicar_descuento_2x1(2, 100)
100
>>> aplicar_descuento_2x1(4, 150)
300
>>> aplicar_descuento_2x1(1, 200)
0.0 # ¡ups!
```

En otras palabras, algunas pruebas arrojaron resultados correctos y otras, no:

  * ✔️ Si la cantidad es cero, el precio debería ser cero, sin importar la cantidad
  * ✔️ Si la cantidad es 2 y el precio base es $100, el precio final debería ser $100
  * ✔️ Si la cantidad es 4 y el precio base es $150, el precio final debería ser $300
  * ❌ Si la cantidad es 1 y el precio base es $200, el precio final debería ser $200 (no hubo descuento)

¿Qué hacemos ahora? Deberíamos volver a nuestro código, revisarlo y descubrir el error. En nuestro caso, era la falta de un `+ 1`:

```python
def aplicar_descuento_2x1(cantidad, precio_base):
  """
  Aplica el descuento 2 X 1 a un precio: los pares de productos los cobra a la mitad de precio
  """
  if cantidad % 2 == 0:
    return precio_base * cantidad / 2
  else:
    return precio_base * (1 + (cantidad - 1) / 2)
```

¿Pero qué nos garantiza que esta vez no hayamos cometido ningún error? ¡Absolutamente nada! Es decir, deberíamos volver a probar el caso que falló anteriormente, para asegurarnos de que hayamos corregido el problema:

```python
>>> aplicar_descuento_2x1(1, 200)
200.0 # ¡bien! ¡pasamos la prueba!
```

¡Pero eso no es suficiente! Perfectamente podríamos haber _roto_ accidentalmente los casos que antes sí funcionaban (lo que se conoce como errores de _regresión_):

```python
>>> aplicar_descuento_2x1(0, 450)
0.0
>>> aplicar_descuento_2x1(2, 100)
100
>>> aplicar_descuento_2x1(4, 150)
300
```

Recién ahora podemos decir que hemos probado todo con resultados satisfactorios 😫:

  * ✔️ Si la cantidad es cero, el precio debería ser cero, sin importar la cantidad
  * ✔️ Si la cantidad es 2 y el precio base es $100, el precio final debería ser $100
  * ✔️ Si la cantidad es 4 y el precio base es $150, el precio final debería ser $300
  * ✔️ Si la cantidad es 1 y el precio base es $200, el precio final debería ser $200 (no hubo descuento)

Como vemos, todo esto es tedioso y propenso a error. ¿Y que hacemos cuando algo es así? ¡Programamos!

## Pruebas unitarias automatizadas

Justamente porque probar es necesario, pero al mismo tiempo hacerlo correctamente y luego de cada cambio es muy molesto y aburrido, es que existen las pruebas unitarias automatizadas: se trata de _programar_ nuestras pruebas, usando una herramienta especializada.

En Python usaremos `pytest`, la cual podemos instalar de la siguiente forma:

```bash
$ pip install pytest
```

Luego de ésto, podremos escribir, en el mismo directorio que nuestro archivo principal, otro llamado `test_descuento.py`, en que el que escribiremos nuestras _pruebas unitarias automatizadas_, es decir:

  * **pruebas** sobre nuestro programa;
  * que evalúan detalladamente pequeñas cada una de sus **unidades** (partes), como por ejemplo cada función o cada procedimiento;
  * y que se pueden ejecutar de forma **automática**, tantas veces como se desee.

Para ello primero debemos _importar_ nuestro código, es decir, leerlo de su archivo y traerlo a aquel que contiene las pruebas...

```python
from descuento import *
```

... y luego, escribiremos cada una de nuestras pruebas unitarias automatizadas, o pruebas unitarias, o simplemente, _tests_:

```python
def test_el_precio_es_cero_cuando_cuando_cantidad_es_cero():
  assert aplicar_descuento_2x1(0, 450) == 0
```

Como vemos, un test consiste simplemente en un procedimiento, con ciertas características:

  1. como todo procedimiento, no debe devolver nada;
  2. su nombre debe empezar con  `test`;
  3. debe probar un escenario de nuestro interés, y realizar validaciones con el comando `assert`;
  4. y debe tener un nombre que exprese qué es lo que se está probando.

Por ejemplo:

  1. el test anterior no devuelve nada;
  2. su nombre empieza con `test`;
  3. existe para probar el primer escenario que discutimos previamente: _si la cantidad es cero, el precio debería ser cero_.
  4. y finalmente verifica mediante el comando `assert` que efectivamente la función retorne el valor esperado (`0`): si la condición booleana es falsa, el test fallará, pero si es verdadera, el test será exitoso.

¿Y cómo hacemos para ejecutar nuestras pruebas? ¡Usando el comando `pytest`!

```bash
$ pytest
============================= test session starts =============================
platform linux -- Python 3.8.10, pytest-7.1.3, pluggy-1.0.0
collected 1 item

test_descuento.py .                                                     [100%]

============================== 1 passed in 0.01s ==============================
```

¡Está vivo! Esto nos indica que el test se ejecutó correctamente 🎊.

Si ahora quisieramos escribir otro test más, para la segunda situación (_Si la cantidad es 2 y el precio base es $100, el precio final debería ser $100_), deberíamos escribirlo así:

```python
def test_el_precio_es_100_cuando_cantidad_es_2_y_precio_es_100():
  assert aplicar_descuento_2x1(2, 100) == 100
```

Y nuevamente podemos ejecutar todos nuestros tests:

```bash
$ pytest
============================= test session starts =============================
platform linux -- Python 3.8.10, pytest-7.1.3, pluggy-1.0.0
collected 2 items

test_descuento.py ..                                                    [100%]

============================== 2 passed in 0.01s ==============================
```

¿Y que pasaría si probáramos el caso _Si la cantidad es 1 y el precio base es $200, el precio final debería ser $200_...

```python
def test_el_precio_es_200_cuando_la_cantidad_es_1_y_el_precio_base_es_200():
  assert aplicar_descuento_2x1(1, 200) == 200
```

... y lo probáramos con la primera versión de nuestro código?


```
$ pytest
============================= test session starts =============================
platform linux -- Python 3.8.10, pytest-7.1.3, pluggy-1.0.0
collected 3 items

test_descuento.py ..F                                                   [100%]

================================== FAILURES ===================================
____ test_el_precio_es_200_cuando_la_cantidad_es_1_y_el_precio_base_es_200 ____

    def test_el_precio_es_200_cuando_la_cantidad_es_1_y_el_precio_base_es_200():
>     assert aplicar_descuento_2x1(1, 200) == 200
E     assert 0.0 == 200
E      +  where 0.0 = aplicar_descuento_2x1(1, 200)

test_descuento.py:10: AssertionError
=========================== short test summary info ===========================
FAILED test_descuento.py::test_el_precio_es_200_cuando_la_cantidad_es_1_y_el_precio_base_es_200
========================= 1 failed, 2 passed in 0.06s =========================
```

💣 ¡El test estalla! Pero lo bueno es que nos lo indica con precisión: nos dice cuántos tests fallaron y cuántos no, qué errores hubo y dónde. Con todo esto ahora corregir nuestro código (recordar que faltaba el `+ 1`) y volver a correr el test es sencillo:

```
$ pytest
============================ test session starts =============================
platform linux -- Python 3.8.10, pytest-7.1.3, pluggy-1.0.0
collected 3 items

test_descuento.py ...                                                  [100%]

============================= 3 passed in 0.01s ==============================
```
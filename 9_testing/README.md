
# Introducción al _testing_

¡Hola! Hasta ahora venimos programando sin parar, y en mas de una ocasión nuestro código no ha funcionado como lo deseabamos. Quizás teníamos mal escrito el nombre de una función o una variable y se producía un `NameError`. O quizás, cometíamos un error de sintaxis y nos topabamos con un `SintaxError`. O peor aún: nuestro código no lanzaba ningún error, pero sin embargo no hacía lo que debía: una cuenta era incorrecta, faltaba o sobraba un elemento en una lista, y así.

De hecho, es incluso posible que _rara vez_ nuestros programas hayan hecho lo que deben en el primer intento y hayamos tenido que escribirlo y reescribirlo varias veces hasta lograr el resultado deseado. En definitiva, _errar es humano_ y debemos preparanos para ello. ¡Por eso mismo siempre debemos probar nuestro código! Por ejemplo, si tenemos una función como la siguiente...

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

...¿cómo la probaríamos? La forma más sencilla es cargarla en nuestro intérprete con `python -i` y luego _someterla_  a diferentes pruebas:

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
    return precio_base * 1 + (cantidad - 1) / 2
```

¿Pero qué nos garantiza que esta vez no hayamos cometido ningún error? ¡Absolutamente nada! Es decir, deberíamos volver a probar el caso que falló anteriormente, para asegurarnos de que hayamos corregido el problema:

```python
>>> aplicar_descuento_2x1(1, 200)
200.0 # ¡bien! ¡pasamos la prueba!
```

¡Pero eso no es suficiente! Perfectamente podríamos haber _roto_ accidentalmente los casos que antes sí funcionaban:

```python
>>> aplicar_descuento_2x1(1, 200)
200.0 # ¡bien! ¡pasamos la prueba!
```

TODO

cada uno de los casos anteriores (y no sólo los que hayan fallado):


Como vemos, todo esto es tedioso y propenso a error. ¿Y que hacemos cuando algo es así? ¡Programamos!


## Pruebas unitarias automatizadas

Justamente porque probar es necesario, pero al mismo tiempo hacerlo correctamente y luego de cada cambio es muy molesto y aburrido, es que existen las pruebas unitarias automatizadas: se trata de _programar_ nuestras pruebas, usando una herramienta especializada.

En Python usaremos `pytest`, la cual podemos instalar de la siguiente forma:

```bash
$ pip install pytest
```

Luego de ésto, podremos escribir, en el mismo directorio que nuestro archivo principal, otro llamado `test_descuento.py`:


```python
from descuento import *

def test_descuento_cuando_cantidad_es_cero():
  assert aplicar_descuento_2x1(0, 450) == 0
```

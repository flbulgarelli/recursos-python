# Acá tenés que importar el código que hayas desarrollado
# Suponiendo que el mismo se encuentra en un archivo main.py, "hermanado" (en el mismo directorio que)
# to test_main.py, deberías hacer el import así:
from main import *

# A partir de acá, podés escribir tus tests.
# Por ejemplo, podemos probar a función hay_stock
# Si bien no es el primer punto del enunciado, nos va a permitir
# probar en el camino a los dos puntos anteriores: registrar_producto y recargar_stock
# con lo que estamos probando también los otros puntos. Aunque es la idea, no siempre es posible
# probar todo "unitariamente", es decir, de forma totalmente aislada del resto del código

# Un escenario posible sería probarlo cuando aún no agregaste nada al listado de productos
def test_hay_stock_producto_inexistente():
  # recordá que los tests deberían ser
  # repetibles e independientes del orden, así que nos tenemos que asegurar de que partamos
  # de un estado conocido.
  # Yo me hice un procedimiento auxiliar en mi archivo main que reinicia la tienda
  # (es decir, (re)inicializa los productos y ventas con una lista vacía)
  reiniciar_tienda()

  assert not hay_stock(100)

# otro escenario posible sería probar buscar un producto (ejemplo: producto con código 100)
# cuando ese producto está registrado, pero no hay stock
def test_hay_stock_producto_existente_sin_stock():
  # de nuevo, tenemos que asegurarnos de partir de un estado conocido (la tienda vacía)...
  reiniciar_tienda()

  # ...a la que le agregamos una remera para probar
  registrar_producto({
    "codigo": 100,
    "nombre": "remera talle m",
    "categoria": "remera",
    "precio": 4500
  })

  # y probamos efectivamente lo que deseamos
  assert not hay_stock(100)


# y ahora otro escenario más (y el más "obvio", probablemente): probamos
# que cuando registremos un producto y le carguemos stock, haya stock:
# (De paso, nos viene bien para recordar la idea de precondición y postcondición que vimos hace dos clases)
def test_hay_stock_producto_existente_con_stock():
  # nuestro estado inicial... (precondición)
  reiniciar_tienda()
  registrar_producto({
    "codigo": 100,
    "nombre": "remera talle m",
    "categoria": "remera",
    "precio": 4500
  })

  # lo que vamos a hacer... (operación)
  recargar_stock(100, 10)

  # lo que debería pasar (postcondición)
  assert hay_stock(100)

# ¡Pero hay mas casos para probar! Por ejemplo, ¿qué pasaría si registramos dos productos,
# le agregamos stock al segundo pero preguntamos por el stock del primero?

# Y así también podemos seguir probando con los demás puntos. Por ejemplo, podemos probar más en detalle
# recargar_stock: ¿qué debería pasar, por ejemplo, si intentamos cargar stock a un producto inexistente?
# ¿o si registramos dos veces un mismo producto? Son todas cosas que podríamos probar acá.

# Obviamente no todos los tests utilizarán hay_stock: acá apareció siempre porque es lo que estabamos probando,
# pero para probar `calcular_precio_final_producto` probablemente todo lo referido al stock sea irrelevante.
# Ejemplo:

def test_calcular_precio_final_con_iva():
  assert calcular_precio_final_producto("...completar...") == "...completar..."

# Quizás en otros tests más conveniente será incluso ver si se agregó
# un elemento a la lista de productos, o a la lista de ventas, o si fue modificado algún elemento
# Por ejemplo, podrías hacer pruebas del estilo siguiente:

def test_al_recargar_el_stock_el_stock_aumenta():
  # precondición
  reiniciar_tienda()
  registrar_producto({
    "codigo": 150,
    "nombre": "remera talle s",
    "categoria": "remera",
    "precio": 4100
  })

  # operación
  recargar_stock(150, 10)

  # postcondición
  assert productos[0]["stock"] == 10


# Y también podrías hace otro test que verifique qué pasaría si hacer dos recargas consecutivas.
# ¿Se incrementará realmente como corresponde?

# Otro test similar a este, pero para realizar_compra, podría ser justamente que si realizas_compra
# el stock disminuya

# Y en la misma línea, que si realizás compra, se cree una nueva venta (que nuevamente podrías resolverlo haciendo un
# assert que pregunte si esa venta se agregó, o si su tamaño cambió, o si la última venta es la que estás esperando)

# ¡Y así! Recordá maximizar la cobertura: idealmente todos los puntos deberán estar probados, con cierto detalle.
# ¡Éxitos!
# MacoWins

## Introducción

MacoWins es una reconocida cadena de ropa formal, con tiendas en muchas ciudades de Argentina. Recientemente, le han pedido a 2Diseños, nuestra consultora de software, que desarrolle un nuevo sistema para la gestión de sus ventas y stock.

## Modelo

MacoWins guarda la información de sus productos en una lista con la siguiente forma:

```python
productos = [
  {
    "codigo": 100,
    "nombre": "remera talle m",
    "categoria": "remera",
    "precio": 4500,
    "stock": 35
  }
]
```

Además, guarda la información de cada venta así:

```python
ventas = [
  {
    "codigo_producto": 100,
    "cantidad": 3,
    "fecha": "2021-09-20",
    "precio": 4500
  }
]
```

## Requerimientos

Sabiendo esto, necesitamos desarrollar y probar las siguientes funciones y procedimientos:

1. `registrar_producto`: recibe un diccionario con `codigo`, `nombre`, `categoria`, `precio` y agrega un producto nuevo a la lista de productos. El `stock` del producto agregado debe estar inicialmente en cero.
1. `recargar_stock`: toma un código de producto y una cantidad de unidad de stock a agregar, e incrementa el stock correspondiente a ese producto. Si el código de producto indicado no existe, debe lanzar una excepción.
1. `hay_stock`: recibe un código de producto y dice si hay stock (es decir, si el `stock`  correspondiente es mayor a cero). Si el código indicado no existe en la lista de productos, debe devolver `False`.
1. `calcular_precio_final`: toma un producto (un diccionario) y un booleano `es_extranjero` y calcula su valor final, según [la siguiente regla](https://www.argentina.gob.ar/reintegrar-impuestos-turistas-extranjeros):
  a. si quien calcula el precio es extranjero y el valor es mayor de $70, es el mismo valor sin cambios.
  b. en caso contrario, es el valor original más un 21%
1. `contar_categorias`: retorna la cantidad de categorías únicas
1. `realizar_compra`: recibe un código de producto y una cantidad de items a comprar. En base a ello, decrementa el `stock` del producto correspondiente y crea una nueva venta con la información correspondiente. Si no hay suficiente stock, lanzar una excepción.
1. `discontinuar_productos`: elimina los `productos` sin `stock`.
1. `valor_ventas_del_dia`: retorna el valor total de las ventas del día de hoy.
1. `ventas_del_anio`: retorna un listado con todas las ventas para el año actual.
1. `productos_mas_vendidos`: toma una cantidad `n` de productos y retorna los nombres de los `n` productos más vendidos
1. `actualizar_precios_por_categoria`: toma una categoría y un porcentaje, y actualiza según ese porcentaje el precio de todos los productos que tengan esa categoría. La búsqueda de categoría en este procedimiento no debe ser exacta: por ejemplo tanto si se pasa como argumento `"REMERA"`, `"   REMERA"` o `"Remera"`, deben actualizarse los productos de la categoría `"remera"`.

## Ejemplos

A continuación, dejamos algunos ejemplos de uso. No son todos y deberemos hacer pruebas más exahustivas y de los requerimientos que falten.


```python
# productos de ejemplo
>>> remera_talle_m = {
  "codigo": 100,
  "nombre": "remera talle m",
  "categoria": "remera",
  "precio": 4500
}
>>> pulserita = {
  "codigo": 1098,
  "nombre": "pulserita de tela verde",
  "categoria": "accesorios",
  "precio": 50
}
>>> remera_talle_s = {
  "codigo": 99,
  "nombre": "remera talle s",
  "categoria": "remera",
  "precio": 4500
}
>>> productos
[] # inicialmente no hay productos cargados
>>> registrar_producto(remera_talle_m)
>>> productos # ahora hay un producto
[
  {
    "codigo": 100,
    "nombre": "remera talle m",
    "categoria": "remera",
    "precio": 4500,
    "stock": 0,
  }
]
>>> recargar_stock(45, 6)
Traceback (most recent call last):
  File (...)
ValueError: producto desconocido # ups, no existía ese producto
>>> recargar_stock(100, 15) # incrementamos una vez veces
>>> recargar_stock(100, 2) # incrementamos otra vez más
>>> productos
[
  {
    "codigo": 100,
    "nombre": "remera talle m",
    "categoria": "remera",
    "precio": 4500,
    "stock": 17
  }
]
>>> hay_stock(100)
True # porque el producto 100 tiene 17 unidades en stock
>>> hay_stock(12)
False # porque ni siquiera existe
>>> calcular_precio_final_producto(remera_talle_m, False)
5445.0
>>> calcular_precio_final_producto(remera_talle_m, True)
4500
>>> contar_categorias()
1
>>> registrar_producto(remera_talle_s)
>>> contar_categorias()
1
>>> registrar_producto(pulserita)
>>> contar_categorias()
2 # recién ahora hay dos categorias: las remeras y los accesorios
```

## Ayudas

### Parámetros opcionales

Si cuando declarás una función, podés indicar un valor por defecto para su último o últimos parámetros. Por ejemplo:

```python
def numero_magico(duplicar=False):
  if duplicar:
    return 84
  else:
    return 42
```

De esa forma, podés invocar tu función como siempre...

```python
>>> numero_magico(False)
42
>>> numero_magico(True)
84
```

Pero también podes hacerlo sin especificar el argumento o explicitando su nombre:

```python
>>> numero_magico()
42
>>> numero_magico(duplicar=True)
84
```

Esto no permite hacer cosas nuevas, pero sí hacer a tu código más simple y claro de usar.

### Día de hoy

Para obtener el día de hoy en formato "2022-09-01" (es decir, _año-mes-dia_) podés hacer lo siguiente:

```python
>>> from datetime import date
>>> date.strftime(date.today(), "%Y-%m-%d")
'2022-09-21'
```

### Lanzar excepciones

Lanzar excepciones nos permite generar errores de forma _controlada_, es decir, sabiendo claramente dónde los estamos produciendo y por qué, e indicando un mensaje claro. Esto se hace mediante el comando `raise`:

```python
raise ValueError("producto desconocido")
```

Cuando se lanza una excepción, el programa, función o procedimiento aborta su ejecución y no se siguen procesando las instrucciones posteriores.

Si estás dentro de una función, te va a convenir escribirlo de la siguiente forma:

```python
def function_misteriosa():
  if condicion_de_error_misteriosa():
    raise ValueError("mensaje descriptivo")

  # resto del código acá
```

## Modalidad de entrega

Entregar como un archivo `.py`, el cual debe tener todas las funciones, procedimientos y datos de ejemplo necesarios para probar el código. Para transportar el código de una máquina a otra, recomendamos alguna de las siguientes opciones: 

  * Usar un pendrive
  * Enviarlo por mail 
  * Guardarlo en un archivo en Google Drive
  * Guardarlo en un gist en https://gist.github.com/. Para ello es necesario hacer antes una cuenta. 



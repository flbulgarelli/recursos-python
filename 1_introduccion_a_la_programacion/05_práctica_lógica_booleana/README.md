> Basado en https://github.com/MumukiProject/mumuki-guia-javascript-ejercitacion-condicionales

# Práctica lógica booleana

## 1. `puede_ver_pelicula(edad, tiene_autorizacion)`

Crear una función `puede_ver_pelicula` que tome como argumentos un número `edad` y un booleano `tiene_autorizacion`, y
devuelva si la persona está habilitada para ver la película. Sólo puede ver la película si: tiene 15 años o más, o tiene autorización de sus padres.

```python
puede_ver_pelicula(12, False) # False
puede_ver_pelicula(12, True)  # True
puede_ver_pelicula(16, False) # True
puede_ver_pelicula(18, True)  # True
```

## 2. `esta_en_rango(valor, minimo, maximo)`

Crear una función `esta_en_rango` que tome como argumentos tres números, un `valor`, un número `minimo` y un número `maximo`, y devuelva si el `valor` se encuentra entre los números `minimo` y `maximo` (si el `valor` es igual a uno de los extremos se considera que está dentro del rango)

```python
esta_en_rango(3, 1, 10)   # True
esta_en_rango(1, 1, 10)   # True
esta_en_rango(10, 1, 10)  # True
esta_en_rango(12, 1, 10)  # False
esta_en_rango(-3, 1, 10)  # False
```

## 3. `puede_avanzar(colo_semaforo)`

Crear una función `puede_avanzar` que tome como argumento un string con el color del semáforo y devuelva si puede avanzar.

```python
puede_avanzar('verde')     # True
puede_avanzar('amarillo')  # False
puede_avanzar('rojo')      # False
```

## 4. `es_vocal(letra)`

Crear una función `es_vocal` que tome como argumento un string `letra` y devuelva si `letra` es una vocal.

```python
es_vocal('a') # True
es_vocal('n') # False
```

## 5. `es_consonante(letra)`

Crear una función `es_consonante` que tome como argumento un string `letra` y devuelva si es una consonante

```python
es_consonante('a') # False
es_consonante('n') # True
```

## 6. `es_hora_valida(hora)`

> Nota: este ejercicio es difícil porque requiere usar la función `str.split`, que la veremos más adelante...
>
> ```python
>>> hora, minuto = str.split("12:30", ":")
>>> hora
'12'
>>> minuto
'30'
>```
>
> ... y también la función `int`, que toma un string y lo conveirte a número, si es posible:
>
>```python
>> int("23")
23
>>> int("hola")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'hola'
>```
>


Crear una función `es_hora_valida` que tome como argumento un string `hora` con el formato `HH:mm` y determine si es una hora válida del día o no

```python
es_hora_valida('12:23') # True
es_hora_valida('12:65') # False
es_hora_valida('28:05') # False
es_hora_valida('00:00') # True
```

## 7. `puede_renovar_carnet(paso_test, tiene_multas_impagas, pago_impuestos)`

Crear una función `puede_renovar_carnet` que tome como argumentos tres booleanos, `paso_test`, `tiene_multas_impagas` y `pago_impuestos`,
y devuelva si una persona está habilitada para renovar su carnet de conducir. Una persona puede renovar su carnet si pasó los tests, no tiene multas impagas y pagó todos los impuestos

```python
puede_renovar_carnet(True, True, True)    # False
puede_renovar_carnet(True, True, False)   # False
puede_renovar_carnet(True, False, True)   # True
puede_renovar_carnet(True, False, False)  # False
puede_renovar_carnet(False, True, True)   # False
puede_renovar_carnet(False, True, False)  # False
puede_renovar_carnet(False, False, True)  # False
puede_renovar_carnet(False, False, False) # False
```

## 8. `puede_graduarse(asistencia, materias_aprobadas, tesisAprobada)`

Crear una función `puede_graduarse` que tome como argumentos dos números `asistencia` y `materias_aprobadas` y
un booleano `tesisAprobada`, y devuelva si una persona puede gruadarse. Una persona puede graduarse si tiene un 75%
de asistencia o más, 50 materias aprobadas o más y la tesis aprobada.

```python
puede_graduarse(80, 50, True)  # True
puede_graduarse(80, 50, False) # False
puede_graduarse(80, 45, True)  # False
puede_graduarse(80, 45, False) # False
puede_graduarse(65, 50, True)  # False
puede_graduarse(33, 55, False) # False
puede_graduarse(42, 45, True)  # False
puede_graduarse(28, 45, False) # False
```


## 9. `comienza_con_a`

Definí una función `comienza_con_a` que, al aplicarla con un string, me diga si el mismo comienza con la letra 'a', sin importar si la palabra está escrita en minusculas o mayúsculas. Por ejemplo:

```python
>> comienza_con_a("aguja")
True

>> comienza_con_a("AGUA")
True

>> comienza_con_a("bote")
False
```

## 10. `es_multiplo_de_3`

Definí la función `es_multiplo_de_3` que dice si un número se puede dividir por 3. Por ejemplo:

```python
>> es_multiplo_de_3(9)
True
>> es_multiplo_de_3(4)
False
```

Consejo: no resuelvas la función directamente. En su lugar dividí en subtareas y creá y usá una función `es_multiplo_de` 😎.

## 11. `es_bisiesto`

Definí la función `es_bisiesto` que indica si un año tiene 366 días.

```python
>> es_bisiesto(2000)
True
```

Tené en cuenta que un año es bisiesto si:

* es múltiplo de 400, o bien
* es múltiplo de 4 pero no de 100

Ah: fijate si alguna de las funciones que definiste en los puntos anteriores te puede ser útil 😇.

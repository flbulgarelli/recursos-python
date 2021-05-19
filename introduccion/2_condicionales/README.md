# Condicionales y operadores lógicos

## Ejercicios con operadores lógicos

### `puede_ver_pelicula(edad, tiene_autorizacion)`

Crear una función `puede_ver_pelicula` que tome como argumentos un número `edad` y un booleano `tiene_autorizacion`, y
devuelva si la persona está habilitada para ver la película. Sólo puede ver la película si: tiene 15 años o más, o tiene autorización de sus padres.

```python
puede_ver_pelicula(12, False) # False
puede_ver_pelicula(12, True)  # True
puede_ver_pelicula(16, False) # True
puede_ver_pelicula(18, True)  # True
```

### `esta_en_rango(valor, minimo, maximo)`

Crear una función `esta_en_rango` que tome como argumentos tres números, un `valor`, un número `minimo` y un número `maximo`, y devuelva si el `valor` se encuentra entre los números `minimo` y `maximo` (si el `valor` es igual a uno de los extremos se considera que está dentro del rango)

```python
esta_en_rango(3, 1, 10)   # True
esta_en_rango(1, 1, 10)   # True
esta_en_rango(10, 1, 10)  # True
esta_en_rango(12, 1, 10)  # False
esta_en_rango(-3, 1, 10)  # False
```

### `puede_avanzar(colo_semaforo)`

Crear una función `puede_avanzar` que tome como argumento un string con el color del semáforo y devuelva si puede avanzar.

```python
puede_avanzar('verde')     # True
puede_avanzar('amarillo')  # False
puede_avanzar('rojo')      # False
```

### `es_vocal(letra)`

Crear una función `es_vocal` que tome como argumento un string `letra` y devuelva si `letra` es una vocal.

```python
es_vocal('a') # True
es_vocal('n') # False
```

### `es_consonante(letra)`

Crear una función `es_consonante` que tome como argumento un string `letra` y devuelva si es una consonante

```python
es_consonante('a') # False
es_consonante('n') # True
```

### `es_hora_valida(hora)`

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

### `puede_renovar_carnet(paso_test, tiene_multas_impagas, pago_impuestos)`

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

### `puede_graduarse(asistencia, materias_aprobadas, tesisAprobada)`

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

## Ejercicios con condicionales

### `par_o_impar(numero)`

Crear una función `par_o_impar` que acepte como argumento un `numero` y devuelva el string `par` si el `numero` es par, o el string `impar` si el `numero` es impar

```python
par_o_impar(3)  # 'impar'
par_o_impar(10) # 'par'
```

### `par_o_impar(numero)`

Crear una función `par_o_impar` que acepte como argumento un `numero` y devuelva el string `positivo` si el `numero` es
positivo, o el string `negativo` si el `numero` es negativo

```python
par_o_impar(3)  # 'positivo'
par_o_impar(-5) # 'negativo'
```

### `avanzar_semaforo(color_actual)`

Crear una función `avanzar_semaforo` que acepte como argumento un string `color_actual` y devuelva un string con el
siguiente color del semáforo, siguiendo el orden: verde -> amarillo -> rojo -> verde

```python
avanzar_semaforo('verde')     # 'amarillo'
avanzar_semaforo('amarillo')  # 'rojo'
avanzar_semaforo('rojo')      # 'verde'
```

### `obtener_dias_mes(mes)`

Crear una función `obtener_dias_mes` que tome como argumento un string `mes` y devuelva un número dependiendo de la
cantidad de días que tenga ese mes

```python
obtener_dias_mes("diciembre") # 31
obtener_dias_mes("febrero")   # 29
```

### `obtener_generacion(anio_nacimiento)`

Crear una función `obtener_generacion` que tome como argumento un número `anio_nacimiento` y devuelva un string con la generación a la que pertenece, siguientdo estas reglas:

| Generación | Años de nacimiento |
| --- | --- |
| Baby boomer | 1949-1968 |
| Generación X | 1969-1980 |
| Millennials | 1981-1993 |
| Generación Z | 1994-2010 |

### `obtener_sensacion(temperatura)`

Crear una función `obtener_sensacion` que tome como argumento un número `temperatura` y devuelva un string dependiendo de la `temperatura`,
con las siguientes reglas:

| Temperatura | Mensaje |
| --- | --- |
| Menor a 0° | ¡Está helando!
| Mayor o igual a 0° y menor a 15° | ¡Hace frío!
| Mayor o igual a 15° y menor a 25° | Está lindo
| Mayor o igual a entre 25° y menor a 30° | Hace calor
| Mayor o igual de 30° | ¡Hace mucho calor!

```python
obtener_sensacion(33) # "¡Hace mucho calor!"
```

### `obtener_nota(puntaje)`

Crear una función `obtener_nota` que tome como argumento un número `puntaje` y devuelva un string dependiendo del `puntaje`
redondeado, con las siguientes reglas:

| Puntaje | Nota |
| --- | --- |
| Menor a 6 | Desaprobado
| Mayor o igual a 6 y menor a 7 | Regular
| Mayor o igual a 7 y menor a 8 | Bueno
| Mayor o igual a entre 8 y menor a 10 | Muy bueno
| 10 | Excelente
| Menor a 0 o mayor a 10 | Puntaje inválido

```python
obtener_nota(7)    # "Bueno"
obtener_nota(9.6)  # "Excelente"
obtener_nota(12)   # "Puntaje inválido"
```

### `jugar_piedra_papel_tijera(a, b)`

Crear una función `jugar_piedra_papel_tijera` que tome como argumentos dos strings que representen una jugada (`piedra`, `papel`, `tijera`) y
dependiendo el devuelva un string con un mensaje avisando qué jugada ganó (o si hubo empate)

```python
jugar_piedra_papel_tijera('tijera', 'piedra')  # ¡Ganó piedra!
jugar_piedra_papel_tijera('piedra', 'tijera')  # ¡Ganó piedra!
jugar_piedra_papel_tijera('papel', 'piedra')   # ¡Ganó papel!
jugar_piedra_papel_tijera('piedra', 'papel')   # ¡Ganó papel!
jugar_piedra_papel_tijera('papel', 'tijera')   # ¡Ganó tijera!
jugar_piedra_papel_tijera('tijera', 'papel')   # ¡Ganó tijera!
jugar_piedra_papel_tijera('piedra', 'piedra')  # ¡Empate!
jugar_piedra_papel_tijera('papel', 'papel')    # ¡Empate!
jugar_piedra_papel_tijera('tijera', 'tijera')  # ¡Empate!
```

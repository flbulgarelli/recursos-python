# Funciones

> Basado en https://github.com/MumukiProject/mumuki-guia-javascript-ejercitacion-funciones

## Ejercicios

### `sumar(a, b)`

Creá una función `sumar` que tome dos números y devuelva la suma de ellos

```python
sumar(2, 3) # 5
sumar(1.2, 3.4) # 4.6
sumar(3, -5) # -2
```

### `restar(a, b)`

Creá una función `restar` que tome dos números y devuelva la resta de ellos

```python
restar(3, 2) # 1
restar(10, 5.5) # 4.5
restar(3, 5) # -2
```

### `multiplicar(a, b)`

Creá una función `multiplicar` que tome dos números y devuelva la multiplicación de ellos

```python
multiplicar(2, 3) # 6
multiplicar(4, 0.5) # 2
```

### `dividir(a, b)`

Creá una función `dividir` que tome dos números y devuelva la suma de ellos

```python
dividir(12, 3) # 4
dividir(8, 4) # 2
sumar(30, 6) # 5
```

### `es_par(numero)`

Creá una función `es_par` que tome como argumento un número y si dicho números es par

**TIP**: un número es par si divido por 2 el resto (o módulo) de esa operación es 0

```python
es_par(2) # True
es_par(3) # False
```

### `es_impar(numero)`

Creá una función `es_impar` que tome como argumento un número y si dicho números es impar

**TIP**: un número es impar si divido por 2 el resto (o módulo) de esa operación no es 0

```python
es_impar(2) # False
es_impar(3) # True
```

### `calcular_area_triangulo(base, altura)`

Creá una función `calcular_area_triangulo` que tome la base y la altura de un triángulo y devuelva el área del mismo

```python
calcular_area_triangulo(3, 4) # 6
calcular_area_triangulo(5, 6) # 40
```

### `gritar(str)`

Creá una función `gritar` que tome como argumento un string y devuelva el mismo string con un signo de exclamación al principio y al final del mismo

```python
gritar('hola') # ¡hola!
gritar('aaaaaa') # ¡aaaaaa!
```

### `obtener_nombre_completo(nombre, apellido)`

Creá una función `obtener_nombre_completo` que tome como argumento un nombre y un apellido y devuelva un string con la unión de ambos valores

```python
obtener_nombre_completo('Ada', 'Lovelace') # 'Ada Lovelace'
```

### `saludar(nombre)`

Creá una función `saludar` que tome un nombre y devuelva un saludo que lo incluya.

```python
saludar('Ada') # 'Hola Ada, un gusto conocerte'
```

### `saludar_gritando(nombre, apellido)`

Usando las funciones anteriores (`obtener_nombre_completo`, `saludar` y `gritar`), creá una función `saludar_gritando` que tome un nombre y un apellido y devuelva un saludo con signos de exclamación.

```python
saludar_gritando('Ada', 'Lovelace') # ¡Hola Ada Lovelace, un gusto conocerte!
```


### obtener_datos_ciudad(nombre, poblacion, pais)

Creá una función `obtener_datos_ciudad` que tome un string `nombre`, un número `poblacion` y un string `pais` y devuelva string con el siguiente formato: `La ciudad de NOMBRE tiene una población de POBLACION habitantes y está ubicada en PAIS`

```python
obtener_datos_ciudad('Santa Fe', 545606, 'Argentina') # 'La ciudad de Santa Fe tiene una población de 545606 habitantes y está ubicada en Argentina'
```


### `convertir_horas_en_segundos(horas)`

Creá una función `convertir_horas_en_segundos` que tome como argumento un número de horas y devuelva la conversión a segundos de dicha cantidad de horas

```python
convertir_horas_en_segundos(1) # 3600
convertir_horas_en_segundos(3) # 10800
convertir_horas_en_segundos(4.5) # 16200
```

### `calcular_perimetro_rectangulo(ancho, alto)`

Creá una función `calcular_area_triangulo` que tome el ancho y el alto de un rectángulo y devuelva su perímetro

```python
calcular_perimetro_rectangulo(3.2, 5) # 16.4
calcular_perimetro_rectangulo(10, 20) # 60
```

### `calcular_porcentaje(numero, porcentaje)`

Creá una función `calcular_porcentaje` que tome un número y un porcentaje y devuelva el valor del porcentaje correspondiente al número

```python
calcular_porcentaje(100, 15) # 15
calcular_porcentaje(10, 50) # 5
calcular_porcentaje(200, 10) # 20
```

### `sumar_porcentaje(numero, porcentaje)`

Creá una función `sumar_porcentaje` que tome un número y un porcentaje y devuelva la suma de dicho número con la de su porcentaje. Usá la función `calcular_porcentaje` para obtener el porcentaje a sumar

```python
sumar_porcentaje(100, 15) # 115
sumar_porcentaje(10, 50) # 15
sumar_porcentaje(200, 10) # 220
```

### `restar_porcentaje(numero, porcentaje)`

Creá una función `restar_porcentaje` que tome un número y un porcentaje y devuelva la resta de dicho número con la de su porcentaje. Usá la función `calcular_porcentaje` para obtener el porcentaje a restar

```python
restar_porcentaje(100, 15) # 85
restar_porcentaje(10, 40) # 6
restar_porcentaje(200, 10) # 180
```

### `calcular_fps(fps, minutos)`

FPS son _cuadros por segundo_ (_frames per second_). Creá una una función `calcular_fps` que tome una cantidad de cuadros por segundo y una cantidad de minutos, y devuelva cuántos cuadros hubo en esa cantidad de minutos

```python
calcular_fps(1, 1) # 60
calcular_fps(10, 2) # 1200
calcular_fps(2, 3) # 360
```


### `obtener_competencia(a, b)`

Creá una función `obtener_competencia` que tome dos strings `a` y `b` y devuelva un string con el formato `a vs. b`

```python
obtener_rivales('python', 'Python') # `python vs. Python`
obtener_rivales('Coca', 'Pepsi') # `Coca vs. Pepsi`
obtener_rivales('Perros', 'Gatos') # `Perros vs. Gatos`
```

### `generar_email(usuario, dominio)`

Creá una función `generar_email` que tome dos string `usuario` y `dominio` y el un string email con el formato `usuario@dominio.com`

```python
generar_email('adalovelace', 'gmail') # 'adalovelace@gmail.com'
```

### `es_mayor_de_edad(edad)`

Creá una función `es_mayor_de_edad` que tome como argumento un número `edad` y si es mayor de edad (18 o más)

```python
es_mayor_de_edad(15) # False
es_mayor_de_edad(18) # True
es_mayor_de_edad(27) # True
```

### `hace_calor(temperatura)`

Creá una función `hace_calor` que tome como argumento un número `temperatura` y si hace calor (22 grados o más)

```python
hace_calor(12) # False
hace_calor(22) # True
hace_calor(32) # True
```

### `hace_frio(temperatura)`

Creá una función `hace_calor` que tome como argumento un número `temperatura` y si hace frio (12 grados o menos)

```python
hace_frio(12) # True
hace_frio(22) # False
hace_frio(3) # True
hace_frio(-2) # True
```

### `calcular_puntaje(facil, normal, dificil)`

Creá una función `calcular_puntaje` que calcule el puntaje de un examen que consiste en ejercicios de distinto nivel. Debe tomar como argumento tres que consisten en la cantidad de ejercicios resueltos en cada nivel y devolver un número con el puntaje correspondiente.

El puntaje se calcula de la siguiente forma:

```
facil: 3 puntos
normal: 5 puntos
dificil: 10 puntos
```

```python
calcular_puntaje(3, 0, 0) # 9
calcular_puntaje(0, 2, 1) # 20
calcular_puntaje(5, 1, 2) # 40
```

### `acepta_deposito(monto)`

Creá una función `acepta_deposito` que tome como argumento un número `monto` y si el `monto` es divisible por 10

```python
acepta_deposito(440) # True
acepta_deposito(123) # False
acepta_deposito(500.50) # False
acepta_deposito(1000) # True
```

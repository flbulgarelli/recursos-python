> Basado en http://github.com/mumukiproject/mumuki-guia-funcional-practica-valores-y-funciones-pdep-utn
> y en https://github.com/MumukiProject/mumuki-guia-javascript-ejercitacion-condicionales


## 1. `inversa`

Definí una función `inversa`, que al aplicarla con un número cualquiera me devuelve el resultado de dividir a 1 por ese número.

```python
>> inversa(4)
0.25

>> inversa(0.5)
2.0
```

## 2. `par_o_impar(numero)`

Crear una función `par_o_impar` que acepte como argumento un `numero` y devuelva el string `par` si el `numero` es par, o el string `impar` si el `numero` es impar

```python
par_o_impar(3)  # 'impar'
par_o_impar(10) # 'par'
```

## 3. `positivo_o_negativo(numero)`

Crear una función `positivo_o_negativo` que acepte como argumento un `numero` y devuelva el string `positivo` si el `numero` es positivo, o el string `negativo` si el `numero` es negativo

```python
positivo_o_negativo(3)  # 'positivo'
positivo_o_negativo(-5) # 'negativo'
```

> 🤔 Para pensar: ¿ves algo parecido entre esta función y la anterior? ¿Se te ocurre alguna forma de extraer a una nueva función las partes comunes de `positivo_o_negativo` y `par_o_impar` y luego modificarlas para no repetir código? ¡Intentalo!

## 4. `avanzar_semaforo(color_actual)`

Crear una función `avanzar_semaforo` que acepte como argumento un string `color_actual` y devuelva un string con el
siguiente color del semáforo, siguiendo el orden: verde -> amarillo -> rojo -> verde

```python
avanzar_semaforo('verde')     # 'amarillo'
avanzar_semaforo('amarillo')  # 'rojo'
avanzar_semaforo('rojo')      # 'verde'
```

## 5. `obtener_dias_mes(mes)`

Crear una función `obtener_dias_mes` que tome como argumento un string `mes` y devuelva un número dependiendo de la
cantidad de días que tenga ese mes

```python
obtener_dias_mes("diciembre") # 31
obtener_dias_mes("febrero")   # 29
```

## 6. `obtener_generacion(anio_nacimiento)`

Crear una función `obtener_generacion` que tome como argumento un número `anio_nacimiento` y devuelva un string con la generación a la que pertenece, siguientdo estas reglas:

| Generación | Años de nacimiento |
| --- | --- |
| Baby boomer | 1949-1968 |
| Generación X | 1969-1980 |
| Millennials | 1981-1993 |
| Generación Z | 1994-2010 |

## 7. `obtener_sensacion(temperatura)`

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

## 8. `obtener_nota(puntaje)`

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

## 9. `jugar_piedra_papel_tijera(a, b)`

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


## 10. Celsius a Farenheit

La temperatura se mide en _grados_, pero en algunos países se usan grados _"diferentes"_.

En Argentina, Uruguay y Chile se usan _grados Celsius_ (abreviado _°C_), pero en en Estados Unidos se utilizan _grados Farenheit_ (_°F_). Por ejemplo 10°C son 50°F.

¿Y cómo hacemos para convertir grados Celsius en grados Farenheit? ¡Usando la siguiente fórmula!

```
GradosFarenheit = GradosCelsius × 1.8 + 32
```

> Sabiendo ésto, definí la función `celsius_a_farenheit` que, a partir de una cantidad de grados en escala Celsius, devuelve el equivalente en escala Fahrenheit.
>
> ```python
> >> celsius_a_farenheit(10)
> 50  # porque 10°C son 50°F
> >> celsius_a_farenheit(0)
> 32 # porque 0°C son 32°F
> ```

## 11. Farenheit a Celsius

Ahora hagamos el proceso inverso: aprendamos a convertir una temperatura en grados Farenheit a grados Celsius. La fórmula es la siguiente:

```
GradosCelsius = (GradosFarenheit - 32) / 1.8
```

> Definí la función `farenheit_a_celsius` que, a partir de una cantidad de grados en escala Fahrenheit, devuelve el equivalente en escala Celsius.
>
> ```python
> >> farenheit_a_celsius(32)
> 0 #- porque 32°F son 0°C
> >> farenheit_a_celsius(50)
> 10 #- porque 50°F son 10°C
> ```


## 12. Hace frío internacional

¡Se vino el frío! ❄️ Y necesitamos programar las siguientes funciones:

* `hace_frio_celsius` que nos diga si hace menos de 8 grados Celsius
* `hace_frio_farenheit` que también nos diga si hace frío, pero que tome una temperatura expresada en grados Farenheit.

Ejemplo:

```python
>> hace_frio_celsius(10)
False # porque son más de 8°C
>> hace_frio_celsius(0)
True # porque son menos de 8°C
>> hace_frio_farenheit(50) # recordá que 50°F son 10°C
False
>> hace_frio_farenheit(32) # recordá que 32°F son 0°C
True
```

> Definí las funciones `hace_frio_celsius` y `hace_frio_farenheit`, que nos digan si una temperatura (en Celsius y Farenheit, respectivamente) es fría.
>
> Como desafío adicional, definí `hace_frio_farenheit` reutilizando `hace_frio_celsius` y las funciones anteriores que necesites

## 13. Dispersión

Trabajamos con tres enteros que representan el nivel de un río en tres días consecutivos 📆. Por ejemplo: medimos los días 1, 2 y 3, y las mediciones son: 22 cm, 283 cm, y 294 cm.

Usando estas mediciones nos gustaría saber tres cosas:

* `maximo_entre_tres`: toma tres mediciones y nos da la más alta;
* `minimo_entre_tres`: toma tres mediciones y nos da la mas baja;
*  `dispersion`: toma los tres mediciones y devuelve la diferencia entre la más alta y la más baja. Ejemplo:

```python
>> maximo_entre_tres(22, 283, 294)
294
>> minimo_entre_tres(22, 283, 294)
22
>> dispersion(22, 283, 294)
272 # Porque 294 menos 22 es 272.
```

> ¡Desarrollá estas tres funciones! Y no repitas código: reutilizá `maximo_entre_tres` y `minimo_entre_tres` en la definición de `dispersion` 🕶️


## 14. Pasan los días

Siguiendo con el problema anterior, ahora que contamos con la  función `dispersion`, necesitamos definir las siguientes funciones, que reciben los valores de los tres días, y nos responden si son días parejos, locos o normales:

* `dias_parejos`: son días parejos si la dispersión es chica (menos de 30 cm)
* `dias_locos`: son días locos si la dispersión es grande (más de un metro)
* `dias_normales`, son días normales si no son ni parejos ni locos.

Ejemplo:

```python
>> dias_parejos(110, 98, 100)
True
```

```python
>> dias_normales(1, 200, 500)
False
```

> Definí `dias_normales`, `dias_parejos` y `dias_locos`. Asumí que `dispersion` ya está definida.


## 15. Pinos

En una plantación de pinos, de cada árbol se conoce la altura expresada en **metros**. El peso de un pino se puede calcular a partir de la altura así:

* 3 kg por cada centímetro hasta 3 metros,
* 2 kg por cada centímetro arriba de los 3 metros.


![](https://raw.githubusercontent.com/MumukiProject/mumuki-guia-funcional-practica-valores-y-funciones/master/images/pino.png)


Por ejemplo:

* 2 metros pesan 600 kg, porque 200 * 3 = 600
* 5 metros pesan 1300 kg, porque los primeros 3 metros pesan 900 kg y los siguientes 2 pesan los 400 restantes.

![](https://raw.githubusercontent.com/MumukiProject/mumuki-guia-funcional-practica-valores-y-funciones/master/images/pinos.png)



Los pinos se usan para llevarlos a una fábrica de muebles, a la que le sirven árboles de entre 400 y 1000 kilos, un pino fuera de este rango no le sirve a la fábrica.

> * Definí la función `peso_pino`, recibe la altura de un pino en metros y devuelve su peso.
> * Definí la función `es_peso_util`, recibe un peso en kg y  responde si un pino de ese peso le sirve a la fábrica
> * Definí la función `sirve_pino`, recibe la altura de un pino y responde si un pino de ese peso le sirve a la fábrica.
>

## 16. ¡Puntos para setenta!


En el conocido juego de [la escoba de 15](https://es.wikipedia.org/wiki/Escoba_del_15) tenemos que una forma de ganar puntos es mediante el criterio de "setenta" en el cual una carta tiene un valor especifico dependiendo su número:

* El as (1) tienen 5.5 puntos
* Las figuras (10, 11, 12) tienen 0.5 puntos
* Todas las demás cartas tienen tantos puntos como su número.

Escribí y explicitá el tipo de `punto_para_setenta` la cual recibe el número de la carta y debe devolver la cantidad de puntos según el criterio anterior.

Asumí que el parametro que recibe la función ya es un número de una carta válida.

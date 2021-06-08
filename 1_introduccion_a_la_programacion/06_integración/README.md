> Ejercicios basados en http://github.com/mumukiproject/mumuki-guia-funcional-practica-valores-y-funciones-pdep-utn

## Inversa

Definí una función `inversa`, que al aplicarla con un número cualquiera me devuelve el resultado de dividir a 1 por ese número.

```python
>> inversa(4)
0.25

>> inversa(0.5)
2.0
```


## Comienza con A

Definí una función `comienza_con_a` que, al aplicarla con un string, me diga si el mismo comienza con la letra 'a'.
Por ejemplo:

```python
>> comienza_con_a("aguja")
True

>> comienza_con_a("bote")
False
```

## Es múltiplo de 3

Definí la función `es_multiplo_de_3` que dice si un número se puede dividir por 3. Por ejemplo:

```python
>> es_multiplo_de_3(9)
True
>> es_multiplo_de_3(4)
False
```

## Es Bisiesto

Definí la función `es_bisiesto` que indica si un año tiene 366 días.

```python
>> es_bisiesto(2000)
True
```

Un año es bisiesto si:

* es múltiplo de 400, o bien
* es múltiplo de 4 pero no de 100

## Celsius a Farenheit

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

## Farenheit a Celsius

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


## Hace frío internacional

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

## Dispersión

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


## Pasan los días

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


## Pinos

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

## ¡Puntos para setenta!


En el conocido juego de [la escoba de 15](https://es.wikipedia.org/wiki/Escoba_del_15) tenemos que una forma de ganar puntos es mediante el criterio de "setenta" en el cual una carta tiene un valor especifico dependiendo su número:

* El as (1) tienen 5.5 puntos
* Las figuras (10, 11, 12) tienen 0.5 puntos
* Todas las demás cartas tienen tantos puntos como su número.

Escribí y explicitá el tipo de `punto_para_setenta` la cual recibe el número de la carta y debe devolver la cantidad de puntos según el criterio anterior.

Asumí que el parametro que recibe la función ya es un número de una carta válida.

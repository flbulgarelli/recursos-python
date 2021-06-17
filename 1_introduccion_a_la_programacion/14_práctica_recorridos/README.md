# Práctica recorridos

## 1. Números más diez

Usando `map`, definí una función `numeros_mas_diez` que tome una lista de `numeros` y devuelva un nuevo array incrementando cada elemento original en 10

```python
>>> numeros = [1, 2, 3, 4, 5]
>>> numeros_mas_diez(numeros)
[10, 20, 30, 40, 50]
```

## 2. Dobles

Usando `map` definí la función `dobles` que tome una lista de `numeros` y devuelva un nuevo array con cada valor multiplicado por dos

```python
>>> numeros = [3, 7, 13, 99]
>>> dobles(numeros)
[6, 14, 26, 198]
```

## 3. Longitudes

Usando `map`, definí una función `longitudes` que tome una lista de `frases` y devuelva un nuevo array que contenga la longitud de cada frase.

```python
>>> frases = ['Labore sea dolor.', 'Justo rebum dolor.', 'Stet lorem amet.']

>>> longitudes(frases)
[ 17, 18, 16 ]
```

## 4. Enlistar

Usando map definí la función `enlistar` que tome una lista de `libros` con libros para leer y devuelva un nuevo array en donde cada título de los libros esté dentro de una etiqueta `<li</li>`.
>
```python
>>> libros_programacion = ['JavaScript for Kids: A Playful Introduction to Programming','Composing Software','Eloquent JavaScript: A Modern Introduction to Programming','JavaScript: The Good Parts','Programming JavaScript Applications: Robust Web Architecture with Node, HTML5, and Moderns python Libraries','Effective JavaScript: 68 Specific Ways to Harness the Power of JavaScript','JavaScript: The Definitive Guide','You Don’t Know python','JavaScript Allongé: The Six Edition']
>>> enlistar(libros_programacion)
['<li>JavaScript for Kids: A Playful Introduction to Programming</li>','<li>Composing Software</li>','<li>Eloquent JavaScript: A Modern Introduction to Programming</li>','<li>JavaScript: The Good Parts</li>','<li>Programming JavaScript Applications: Robust Web Architecture with Node, HTML5, and Moderns python Libraries</li>','<li>Effective JavaScript: 68 Specific Ways to Harness the Power of JavaScript</li>','<li>JavaScript: The Definitive Guide</li>','<li>You Don’t Know python</li>','<li>JavaScript Allongé: The Six Edition</li>']
```

## 5. Posiciones

Usando `map`, definí la función `posiciones` que tome una lista de canciones de una playlist y devuelva un nuevo array con los números de las posiciones de cada canción.
>
```python
>>> playlist = ['Everlong', 'The Pretender', 'Learn to Fly']
>>> posiciones(playlist)
 [ '0 - Everlong', '1 - The Pretender', '2 - Learn to Fly' ]
```

## 6. Precios finales

Necesitamos calcular los precios finales de unos productos :money_mouth:. Para ello tenemos que:

  1. aplicarle la ganancia sobre su costo
  2. aplicarle el IVA sobre el resultado anterior.


Usando `map`, definí la función `preciosFinales` que tome una lista de costos de diferentes productos y devuelva un nuevo array con el precio final de cada uno.

```python
>>> costos = [ 12.5, 56, 98, 45.75 ]
>>> preciosFinales(costos)
[22.6875, 101.64, 177.87, 83.03625]
```


## 7. Corresponder

Usando `map`, definí la función `corresponder` que tome una lista de `costos` con números que representan costos de diferentes articulos y una lista de `productos` con los nombres de cada producto y devuelva un nuevo array en donde el nombre de un producto en una posición, se corresponde con el precio final que está en la misma posición. Por ejemplo: el producto que está en la posición **1** tiene un precio igual al elemento en la posición **1** del array `costos`

```python
>>> productos = ['celular', 'notebook', 'monitor' ]
>>> costos = [12.5, 56, 98]
>>> corresponder(costos,productos)
 ['celular 22.6875', 'notebook 101.64', 'monitor 177.87']
```


## 8. Los más caros

Usando `filter`, definí la función `los_mas_caros` que tome una lista de `costos` que representan costos de diferentes productos y devuelva un nuevo array con los precios más caros (mayores a 50)

```python
>>> costos = [ 39, 53, 17, 99, 7, 9, 6, 68, 54, 97, 27, 90, 92, 75, 26, 86, 22, 42, 20, 14 ]
>>> los_mas_caros(costos)
 [53, 99, 68, 54, 97, 90, 92, 75, 86]
```

## 9. Pares e impares

Usando `filter`, definí la función `separando_pares` que tome una lista de `numeros` con números al azar y devuelva un nuevo array con los números pares.
Y otra función `separando_impares` que también tome una lista de números y devuelva un nuevo array con los números impares.

```python
>>> numeros = [43, 11, 18, 46, 44, 37, 42, 29, 9, 3, 37, 0, 40, 10, 38, 34, 25, 40, 4, 32]
>>> separando_pares(numeros)
[18, 46, 44, 42, 0, 40, 10, 38, 34, 40, 4, 32]
>>> separando_impares(numeros)
[43, 11, 37, 29, 9, 3, 37, 25]
```

## 10. Playlist sin escuchar

Nuestra página de múscia favorita nos está recomendando canciones que ya escuchamos :sleepy:. ¿No podemos hacer algo?

Usando `filter`, definí la función `playlistSinEscuchar` que tome una lista `playlist` con canciones sugeridas y otra lista `playlistEscuchada` con canciones que ya escuchamos y devuelva un array con aquellas canciones de la `playlist` que no están en `playlistEscuchada` :headphones:

```python
>>> playlist = ['Smells Like Teen Spirit', 'Everlong', 'Come As You Are', 'The Pretender', 'Heart-Shaped Box', 'Learn to Fly', 'Lithium']
>>> playlistEscuchada = ['The Pretender', 'Lithium', 'Come As You Are']
>>> playlistSinEscuchar(playlist, playlistEscuchada)
 [ 'Smells Like Teen Spirit', 'Everlong', 'Heart-Shaped Box', 'Learn to Fly' ]
```

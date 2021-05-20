> Ejercicios basados en https://github.com/MumukiProject/mumuki-guia-javascript-ejercitacion-bucles

### `obtener_indice(valor, lista)`

Definí una función `obtener_indice` que tome como argumento un valor cualquiera `valor` y un lista cualquiera `lista` y devuelva el índice del _primer ítem_ con dicho valor en la lista, o -1 si no hay ninguno.

```python
obtener_indice(12, [5, 7, 12, 34, 54, 2, 12])
2
obtener_indice(83, [5, 7, 12, 34, 54, 2, 12])
-1
```

### `repetir(valor, cantidad)`

Definí una función `repetir` que tome como argumento un valor `valor` y un número entero `cantidad`, y devuelva una lista con `valor` repetido `cantidad` de veces.

```python
repetir('lovelace', 3)
['lovelace', 'lovelace', 'lovelace']
repetir('a', 5)
['a', 'a', 'a', 'a', 'a']
repetir('html', 0)
[]
```

### `sumar_impares_hasta(numero)`

Definí una función `sumar_impares_hasta` que tome como argumento un número `numero` y que devuelva la suma de todos los impares empezando desde 0 hasta dicho `numero` inclusive.

```python
sumar_impares_hasta(5)
9 #(1 + 3 + 5 = 9)
sumar_impares_hasta(13)
49
sumar_impares_hasta(47)
576
```

### `cuenta_regresiva(numero_inicial)`

Definí una función `cuenta_regresiva` que tome como argumento un número entero `numero_inicial` y que devuelva un lista con cuyo primer ítem sea `numero_inicial` y los demás ítems sean números enteros sucesivos descendientes, hasta llegar a 0.

```python
cuenta_regresiva(3)
[3, 2, 1, 0]
cuenta_regresiva(5)
[5, 4, 3, 2, 1, 0]
```

### `invertir(lista)`

Definí una función `invertir` que tome como argumento un lista `lista` y que devuelva un lista con los mismos valores pero en orden invertido.

```python
invertir([1, 2, 3])
[3, 2, 1]
invertir([5, 7, 99, 34, 54, 2, 12])
[12, 2, 54, 34, 99, 7, 5]
```

### `removerDuplicados(lista)`

Definí una función `removerDuplicados` que tome como argumento un lista `lista` y que devuelva un lista con los mismos valores de `lista` pero sin valores duplicados.

```python
removerDuplicados([1, 1, 1])
[1]
removerDuplicados([1, 1, 2, 2, 3, 3])
[1, 2 ,3]
removerDuplicados([5, 23, 8, 5, 5, 44, 23])
[5, 23 ,8, 44]
```

### `repetir_letras(palabra, cantidad)`

Definí una función `repetir_letras` que tome como argumento un string `palabra` y un número entero `cantidad`, y devuelva una string donde cada letra de `palabra` esté repetida `cantidad` de veces.

```python
repetir_letras('hola', 2)
'hhoollaa'
repetir_letras('ada', 3)
'aaadddaaa'
repetir_letras('ah!', 5)
'aaaaahhhhh!!!!!'
repetir_letras('basta', 1)
'basta'
```

### `capitalizar_palabras(string)`

Definí una función `capitalizar_palabras` tome como argumento un string `string` y devuelva un string donde cada palabra está capitalizada (con la primera letra máyuscula). Dejar las demás letras como están.

```python
capitalizar_palabras('Esto es un título')
'Esto Es Un Título'
capitalizar_palabras('había una vez')
'Había Una Vez'
capitalizar_palabras('OMG')
'OMG'
```

### `sumar_seccion(lista, comienzo, cantidad)`

Definí una función `sumar_seccion` que tome como argumento un lista de números enteros `lista`, un número entero `comienzo` y un número entero `cantidad`, y que devuelva la suma de `cantidad` de números de `lista` empezando a contar desde el ítem con índice `comienzo`.

```python
sumar_seccion([2, 2, 4, 3, 10, 20, 5], 0, 3)
8 #(2 + 2 + 4 = 8)
sumar_seccion([2, 2, 4, 3, 10, 20, 5], 2, 4)
37 #(4 + 3 + 10 + 20 = 37)
sumar_seccion([2, 2, 4, 3, 10, 20, 5], 4, 1)
3
```

### `es_subconjunto(subconjunto, conjunto)`

Definí una función `es_subconjunto` que tome como argumento dos listas, `subconjunto` y `conjunto`, y devuelva `True` si `subconjunto` es realmente subconjunto de `conjunto`, es decir, si todos los valores de `subconjunto` están en `conjunto`.

```python
es_subconjunto([1], [1, 2, 3])
True
es_subconjunto([1, 2, 3], [1, 2, 3, 4, 5])
True
es_subconjunto([27, 49, 54], [54, 27, 8, 27, 49])
True
es_subconjunto([1, 2, 3], [1, 2])
False
es_subconjunto([1], [2, 3, 4])
False
```

### `tiene_bloque(lista)`

Definí una función `tiene_bloque` que tome como argumento un lista `lista` y devuelva `True` si dicho `lista` tiene un bloque de 3 o más ítems consecutivos idénticos, o `False` si no tiene.

```python
tiene_bloque([1, 2, 3])
False
tiene_bloque([1, 1, 1, 2, 3])
True
tiene_bloque([1, 2, 3, 3, 3])
True
tiene_bloque([1, 2, 3, 3, 3, 8])
True
tiene_bloque([1, 2, 2, 3, 3, 4])
False
```

### `es_palindromo(palabra)`

Definí una función `es_palindromo` que tenga como parámetro un string `palabra` y devuelva `True` si dicha palabra es palíndroma, es decir, si puede leerse de igual manera de izquierda a derecha que de derecha a izquierda, o `False` sino.

```python
es_palindromo('ada')
True
es_palindromo('reconocer')
True
es_palindromo('mama')
False
es_palindromo('python')
False
```

# Práctica Agregaciones

Cuando tenemos un conjunto de datos (es decir, de varios elementos, como por ejemplo...

  * Los meses del año representados como strings (ejemplo `['Enero', 'Febrero', 'Marzo', ...]`)
  * Las notas de un parcial para un curso representadas como una lista de números (ejemplo `[10, 4, 2, 9, 8, 8]`)
  * La lista de los animales de una reserva natural como `["loro", "caraya", "ñandún"]`, `[15, 5, 9]` (esto último lo llamamos identificador único, o también ID)
   * Las bicicletarías de CABA como una `DataFrame` con nombre, direccion, email, si tiene servicio mecánico, etc.

 ... es común que necesitemos calcular un único resultado (que puede ser o no del mismo tipo de datos que los elementos del conjunto) que de alguna forma nos describa a esos datos. Por ejemplo:

  * máximos y mínimos (`max`, `min`)
  * cantidad de elementos (`len`)
  * cantidad de elementos únicos (`nunique`)
  * sumatoria (`sum` )
  * promedio o media (`mean`)
  * moda (`mode`)
  * mediana (`median`)

A este tipo de cálculos, que usualmente podemos resolver recorriendo cada elemento del conjunto mediante un `for`, los denominamos _agregaciones_.

¡Practiquémoslas!

## 1. `promedio`

> Definí la función `promedio` que calcule el promedio de una lista (no vacía) de números.

## 2. `maximo` y `minimo`

> Definí las funciones `maximo` y `mínimo` que obtengan el valor más grande y más chico de una lista (no vacía) de números, respectivamente.

## 3. `mediana`

Definí la función `mediana`, que devuelva la mediana de una lista (no vacía) de números. Ejemplo:

```python
>>> mediana([1, 2, 3, 4, 18, 20])
3
>>> mediana([48, 18, 2, 4])
4
```

### Ayuda

1. la mediana se obtiene obteniendo el elemento del medio tras ordenar la lista de menor a mayor.
2. las siguientes funciones pueden ser útiles:  `int`, `rount`, `sorted`

## 4. `cuantil`

> Definí la función `cuantil`, que tome una lista y un número entre 0 y 1 y retorne el valor del cuantil correspondiente:

```python
>>> cuantil([1, 2, 3, 4, 18, 20], 0.5)
3
>>> cuantil([48, 18, 2, 4], 0.25)
2
>>> cuantil([48, 18, 2, 4], 0.75)
18
```

## 5. Brecha ecológica

Vamos a definir como la _brecha ecológica_ de una ciudad a la diferencia entre la cantidad de árboles que hay entre el barrio que más tiene y el barrio que menos tiene.

> Partiendo del [lote de datos de arbolado público lineal de CABA](http://cdn.buenosaires.gob.ar/datosabiertos/datasets/arbolado-publico-lineal/arbolado-publico-lineal.csv), definí una función `brecha_ecologica`, que resuelva este cálculo.

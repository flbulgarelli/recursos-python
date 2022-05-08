# Introducción a pandas

_¡Qué queremos? ¡Trabajar con datos! ¿Y dónde los vamos a buscar? Eh... en un... ¿conjunto de datos?🤔_

Cuando queramos analizar datos, con mucha frecuencia los encontraremos en archivos llamados (no muy originalmente 😛) _lotes de datos_ (_datasets_, en inglés). ¿Pero cómo se ven estos lotes? ¿Dónde los podemos encontrar publicados? ¿Cómo los podemos procesar?

¡Muchas preguntas! En esta lección responderemos alguans de ellas. Y en el camino, conoceremos a `pandas` 🐼, una biblioteca que poco tiene con los simpáticos osos oriundos de las regiones montañosas de China 🇨🇳, pero que nos ayudará enormemente a trabajar con estos lotes de datos.

¡Empecemos!

## 1. Abierto al público

Primero lo primero: entendamos dónde encontrar nuestros tan deseados lotes de datos. O mejor dicho, entendamos que _no siempre_ podremos encontrarlos 😓. Esto se debe a las organizaciones que los recopilan (estados, empresas, ONGs, etc) a veces los _publican_ y otras veces, no.

Por eso es que tenemos dos grandes familias de lotes de datos:

 * 🔓 Los datos abiertos: pueden ser consultados por cualquier persona y usados para casi cualquier fin.
 * 🔒 Los datos cerrados: sólo los pueden consultar personas que pertenezcan a las organizaciones que los producen, o personas externas pero con fuertes limitaciones en su acceso y uso (por ejemplo, a través de un pago)

> 🏅 Desafío: las siguientes son páginas de estados que ofrecen datos abiertos. Exploralas e identificá qué tipo de información publican y **en qué formatos**.
>
> * 🇦🇷 [www.datos.gob.ar](https://www.datos.gob.ar/)
> * 🇺🇾 [www.gub.uy/datos-abiertos](https://www.gub.uy/datos-abiertos)
> * 🇲🇽 [datos.gob.mx](https://datos.gob.mx/)
> * 🇨🇱 [datos.gob.cl](https://datos.gob.cl/)

## 2. Manteniendo las formas

Si exploraste las páginas anteriores, quizás hayas notado que casi todos los lotes de datos están publicados en forma de tablas. Y dentro de tooodos los formatos que existen, uno de los más frecuentes (y fáciles de usuar) se llama CSV.

Momento, ¿cesequé? ¡Ce-ese-vé! Se trata de un acrónimo en inglés de _Comma Separated Value_, es decir, un archivo de texto con valores separados por comas. Por ejemplo así se ve un archivo `datos_ejemplo.csv`:

```csv
Feli,Perez,24
Dani,Lopez,32
Juani,Vazquez,19
```

> Para pensar 🤔: ¿qué está intentando representar este CSV de ejemplo? ¿Qué información contiene cada renglón?

## 3. Sin título

El archivo CSV que vimos antes contenía información de personas, o al menos eso parece. Quizás se traten de sus nombres, apellidos y sus edades, o quizás sean estudiantes de una carrera y nos esté informando la cantidad de materias aprobadas.

Para evitar este tipo de ambigüedad, normalmente los archivos CSV contendrán en su primer renglón los títulos de cada columna. Por ejemplo así podría verse ahora nuestro `datos_ejemplo.csv`:

```csv
nombre,apellido,edad
Feli,Perez,24
Dani,Lopez,32
Juani,Vazquez,19
```

> Para pensar 🤔: Y si ahora quisieras agregar la información de cuál es su gusto de helado favorito, ¿cómo harías?

## 4. Comerciando código

Para poder trabajar con estas tablas en formato `csv` vamos a necesitar nuevas funciones, procedimientos, tipos de datos y otras yerbas 🧉, especialmente diseñadas para este fin. Y como no queremos gastar tiempo en escribirlas a mano, vamos a recurrir a una _biblioteca_: código que otras personas ya programaron y empaquetaron para que podamos incluirlo y usarlo en nuestros programas. Hay bibliotecas para miles de tareas diferentes: procesar imágenes, hacer cuentas sofisticadas, producir música, analizar textos, y mucho más 🤯.

En particular, la biblioteca que nos va a interesar ahora se llama `pandas`, una herramienta poderosa para el lenguaje Python, que posibilita manipular datos de un lote de forma programática. En otras palabaras, va a permitirnos hacer las mismas operaciones que haríamos en una hoja de cálculo, pero utilizando código.

¡Carguemos a nuestra biblioteca de ositos 🐼!

```python
import pandas as pd
```

Con esta sentencia estamos cargando (o _importando_) en nuestro programa, y dejándola lista para ser utilizada, bajo el nombre `pd`. Podríamos leerlo como _"computadora: andá a buscar la biblioteca `pandas` y nombrala como `pd`"_.

📝 Nota: El nombre `pd` es totalmente arbitrario y podríamos haberle dado cualquier otro. Pero casi todo el mundo que la usa (sobre todo en internet) en suele abreviar _pandas_ de esa forma 🤷.

## 5. A cargar, a cargar, cada tabla en su lugar

Ahora que importamos la biblioteca `pandas`, el siguiente paso es conseguir un lote de datos, como por ejemplo, el listado de bicicleterías 🚴 que hay que CABA, cuya dirección es [ésta](https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte/bicicleterias/bicicleterias-de-la-ciudad.csv)

Un vez que hayamos encontrado la dirección (y copiado en nuestro portapeles 📋, para no tener que escribir la dirección a mano), podremos finalmente cargarla en un `DataFrame` llamado `bicicleterias`,
utilizando la función `pd.read_csv`:

```python
bicicleterias = pd.read_csv("https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte/bicicleterias/bicicleterias-de-la-ciudad.csv")
bicicleterias
```

> Probá éste código y observá qué sucede

### Solución posible

<details>
<summary>👀 Ver</summary>

Deberías ver una tabla con los datos de las bicicleterías:

```python
>>> bicicleterias
0    POINT (-58.4256879365174 -34.5923050897605)    1  ...        Palermo  Comuna 14
1     POINT (-58.4259820523858 -34.581377735346)    2  ...        Palermo  Comuna 14
2    POINT (-58.4153429603451 -34.6533516212895)    3  ...  Nueva Pompeya   Comuna 4
3    POINT (-58.4432441275002 -34.5943508729756)    4  ...   Villa Crespo  Comuna 15
4    POINT (-58.3773343753292 -34.6083635891506)    5  ...      Monserrat   Comuna 1
..                                           ...  ...  ...            ...        ...
107  POINT (-58.4514064416743 -34.6064832870543)  119  ...      Caballito   Comuna 6
108     POINT (-58.41682788474 -34.595271412766)  120  ...        Palermo  Comuna 14
109  POINT (-58.4352606531347 -34.5676102200762)  121  ...        Palermo  Comuna 14
110  POINT (-58.4540104298256 -34.6132076385661)  122  ...      Caballito   Comuna 6
111  POINT (-58.4221769107392 -34.5994544804325)  123  ...        Almagro   Comuna 5

[112 rows x 15 columns]
```
</details>


### Para pensar

¡Está vivo! ⚡ ¡Apareció una tabla! Pero, momento...  ¿un `DataFrame`?  ¿Qué es eso? ¡Resolvamos el misterio! 🦇🎃


## 6. ¡Hay tabla!

Hasta ahora veníamos trabajando con valores como números (por ejemplo, el `1`, el `42` y el `30410`), cadenas de caracteres (`"estro es un string"`) o booleanos (`True` o `False`)...

```python
# type es una función que nos permite saber el tipo de dato de un valor
>>> type(1)
<class 'int'>
>>> type("hola mundo")
<class 'str'>
>>> type(True)
<class 'bool'>
```
... pero eso es muy limitado. Por eso vamos a usar ahora un nuevo tipo de dato llamado `DataFrame`, que es el tipo de la variable `bicicleterias`:

```python
>>> type(bicicleterias)
<class 'pandas.core.frame.DataFrame'>
```

Los `DataFrame` representan justamente tablas, compuestas por columnas y filas.

## 7. Hablando de cantidades

¿Y cómo hacemos para saber cuántas filas y columnas tiene un `DataFrame`? Con nuestra vieja y querida función `len`:

```python
# cantidad de filas
>>> len(bicicleterias)
112
# cantidad de columnas
>>> len(bicicleterias.columns)
15
```

💡 Como vemos, si consultamos simplemente la longitud de la tabla, esta se corresponde con la cantidad de filas, lo cual tiene bastante sentido. Como veremos a partir de ahora muchas de las operaciones justamente tendrán que ver con la cantidad o posición de filas.

## 8. De la cabeza a los pies

Como si de un gusanito 🪱 se tratara, las tablas tienen _cabeza_ y _cola_: la cabeza refiere a las primeras `n` filas, mientras que la cola a las últimas `n`. Para obtener la cabeza podemos usar la función infija (más comunmente llamada _método_) `head`:

```python
>>> bicicleterias.head(5)
0  POINT (-58.4256879365174 -34.5923050897605)   1       Bicicletas Araoz  ...                         ARAOZ 1458        Palermo  Comuna 14
1   POINT (-58.4259820523858 -34.581377735346)   2               Roda2oro  ...  FRAY JUSTO SANTAMARIA DE ORO 2305        Palermo  Comuna 14
2  POINT (-58.4153429603451 -34.6533516212895)   3                 Walter  ...                         LYNCH 3914  Nueva Pompeya   Comuna 4
3  POINT (-58.4432441275002 -34.5943508729756)   4              Bici Shop  ...                    VILLARROEL 1093   Villa Crespo  Comuna 15
4  POINT (-58.3773343753292 -34.6083635891506)   5  Bicicleterias El colo  ...                  RIVADAVIA AV. 770      Monserrat   Comuna 1

[5 rows x 15 columns]
```

⚠️ Es importante notar que `head` no orden la tabla bajo ningún criterio, sino que sólo nos da las primeras filas, según la posición en la que originalmente estuvieran.

De forma análoga podemos obtener la cola:

```python
>>> bicicleterias.tail(3)
                                             WKT   id                      nombre  ...                         direccion_     barrio     comuna
109  POINT (-58.4352606531347 -34.5676102200762)  121                       Bicis  ...                NEWBERY, JORGE 1741    Palermo  Comuna 14
110  POINT (-58.4540104298256 -34.6132076385661)  122    Bicicletería Bike Doctor  ...        FRAGATA PRES. SARMIENTO 966  Caballito   Comuna 6
111  POINT (-58.4221769107392 -34.5994544804325)  123  Rodados La Esquina Express  ...  ACUÑA DE FIGUEROA, FRANCISCO 1000    Almagro   Comuna 5

[3 rows x 15 columns]
```

## 9. Ordená, ¡es una orden!

```python
# sort_values también es una función infija
# tabla.sort_values(nombre_columna)
bicicleterias.sort_values("comuna")
```

## 10. Del derecho y del revés

```python
bicicleterias.sort_values("comuna", ascending=False)
```

## 11. Haciendo valer el orden

> Desafío: obtené las últimas 3 bicileterías, según su nombre por orden alfabético.

## 12. Un gráfico vale más que mil filas

Podemos hacer un gráfico de barras con el resultado de un `value_counts` usando `plot.bar` de la siguiente manera:

```python
bicileterias.plot.bar(figsize=(tamanio_x_en_pulgadas, tamanio_y_en_pulgadas))
```

## 13. Combinando todo

> Desafío: ¿cómo podríamos hacer para obtener todas las filas desde la décima y hasta la veinteva? ¡Escribilo!

### Solución posible

<details>
<summary>👀 Ver</summary>

```python
bicicleterias.head(20).tail(10)
```

</details>

## 14. Matrices recargadas

Y ahora combinemos todo... ¡de nuevo!

> Definí una función `entre_limites`, que generalice lo que hicimos en el ejercicio anterior: debe tomar una tabla y dos números, y devolvernos un `DataFrame` que contenga las filas entre los índices dados.

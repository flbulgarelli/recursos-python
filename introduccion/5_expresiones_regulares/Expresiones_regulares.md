# *Python avanzado*
En este recorrido aprenderemos los conceptos básicos de expresiones regulares en [Python](https://www.python.org.ar/). Para ello vas a necesitar instalarte el módulo [RE](https://pypi.org/project/regex/).


# Guias de Trabajo
* [1. Lo esencial es invisible a los ojos](#1-Escape-characters)
* [2. ¿Qué son las expresiones regulares?](#2-ER)
* [3. Metacaracteres](#3-Metacaracteres)
* [4. Expresiones regulares en Python ](#4-RE) 
* [5. Coincidencias o Matches](#5-matches)
* [6. Reemplazos o sustituciones masivas](#6-sub)

[1. Lo esencial es invisible a los ojos](#1-Escape-characters)

Cuando trabajamos con archivos de texto, suele pasar desapercibida la presencia de caracteres que dan formato legible al texto y que no se representan por así decirlo "graficamente explicitos". Un ejemplo de ello es el espacio entre las palabras que tipeamos para constuir una oración. Este tipo de caracteres, comunmente conocidos como caracteres especiales, se encuentran respresentados por _secuencias de escape_. 

Las _secuencias de escape_ son una combinación de caracteres que tiene un significado distinto de los caracteres literales contenidos en ella y se utilizan para definir ciertos caracteres especiales dentro de cadenas de texto, tipicamente aquellos que dan formato al mismo. Y aún cuando son un conjunto de caracteres, una secuencia de escape se considerada un carácter único.

Estas combinaciones constan tipicamente de una barra invertida (`\`) seguida de una letra o de una combinación de dígitos, que tendrá un significado distinto según cuales sean. Por ejemplo, para representar un carácter de _salto de línea_ se utiliza la secuencia de espace `\n`.

Vamos a ver algunas de las secuencias de escape más frecuentes:

| Secuencia de escape| representación | 
|-------------	|----------	|
| \n | salto de línea | 
| \t | Tab o cambio de pestaña |
| \s | espacio |
| \' | Comillas simples |
| \" | Comillas dobles |   



[2. ¿Qué son las expresiones regulares?](#2-ER)

Las expresiones regulares son cadenas de caracteres basadas en reglas sintácticas, que permiten describir secuencias de caracteres. Es decir es un criterio para buscar, capturar o reemplazar texto utilizando patrones. Estas son una herramienta poderosa a la hora de hacer búsquedas sofisticadas en Strings de forma simple.


Las expresiones regulares se pueden concatenar para formar nuevas expresiones regulares; si, por ejemplo, A y B son expresiones regulares, AB también es una expresión regular.


> Para pensar 🤔: ¿Qué usos crees que podemos darle a las expresiones regulares? Proponé una aplicación concreta para tu carrera/disciplina.
>

[3. Metacaracteres](#3-Metacaracteres)

Los `metacaracteres` son caracteres especiales que, dependiendo del contexto, tienen un significado especial para las expresiones regulares. 

Existen lo que se conoce como `metacaracteres delimitadores`, que nos permitirán delimitar dónde queremos buscar los patrones de búsqueda. Entre ellos tenemos:


| Metacaracter| Significado | 
|-------------	|----------	|
| ^	| Inicio de línea | 
| $ | Fin de linea |
| \A | Inicio de texto |
| \Z | Fin de texto |
| . | Coincide con cualquier caracter en una línea dada | 

> Para pensar 🤔: Dado el siguiente texto:
```python
texto = 'Esta es la linea uno\npalabra en la linea dos\n'
```
>¿Cómo crees que darán las siguientes búsquedas? 
>
>expresion regular a: `'^palabra'`
>
>expresion regular b: `'\Apalabra'`
>
>expresion regular c: `'palabra$'`
>
>expresion regular d: `'palabra\Z'`
>

Ya vimos que en programación suele ser útil repetir la ejecución de porciones de código. Las expresiones regulares nos permiten no solo delimitar la porción de texto donde deseamos buscar, sino que también permite repitir cierta cantidad de veces una busqueda dada. Para ello se utilizan los `metacaracteres cuantificadores`:


| Metacaracter| Significado | 
|-------------	|----------	|
|  *	| Cero o más: todas las ocurrencias de un dado substring |	
|  +	| Una o más ocurrencias del patrón|	
|? | Cero o una|
|{n} | Exactamente n veces|
|{n,m} | Por lo menos n pero no más de m veces.|


>
> Para pensar 🤔: ¿Qué significará la expresión regular `"X(.*)Y"`? Ennumera algunas de las posibles strings que cumplen con dicha condición.
>
>
> 🧗‍♀️ Desafío I: ¿Construí la expresión regular que obtenga al menos 4 dígitos?
>
> 🧗‍♀️ Desafío II: ¿Construí la expresión regular que obtenga al entre 3 y 6 letras minúsculas?
>
> 🧗‍♀️ Desafío III: ¿Construí la expresión regular que obtenga todas las apariciones del patrón `ab` en un string?
>

<details>
  <summary>Respuestas</summary>

```bash
Desafio I: \d{4,}

Desafio II: [a-z]{3,6}

Desafio III: ab*

```
</details>

> Para pensar 🤔: ¿Existe una única respuesta para los ejercicios? ¿Qué otras alternativas se te ocurren?

Los dígitos entre llaves de la forma {n,m}, especifican el mínimo número de ocurrencias en n y el máximo en m.

Existen tambien metacaracteres predefinidos, que nos facilitan el uso de las expresiones regulares:

| Metacaracter| Significado | 
|-------------	|----------	|
|  \w	| Caracter alfanumércio|
|  \W	| Caracter NO alfanumércio|	
|  \d	| Caracter numércio|	
|  \D	| Caracter NO numércio|	
|  \s	| Un espacio, de cualquier tipo (\t\n\r\f)|	
|  \S	| Cualquier caracter que no sea un espacio|	


Como ya hemos visto, estos metacaracteres puden combinarse para lograr expresiones regulares complejas. 

>
> 🧗‍♀️Desafio IV: ¿Qué expresión regular usarías para extraer el número de estudiantes que hay en una clase según el siguiente texto:
>
```python
texto = 'En la clase de Introducción a la programación hay 30 estudiantes' 
```
>

<details>
  <summary>Respuestas</summary>

```bash
Desafío IV: /d+
```
</details>

**Rangos**

Un rango es una clase de caracteres abreviada que se crea escribiendo el primer caracter del rango, un guión y el último caracter del rango. Sirve para listar un conjunto de caracteres de interés, de este modo se encontrará uno cualquiera de los caracteres de la lista. Por ejemplo:

    - El rango [a-d] equivale al [abcd]
    - El rango [1-10] equivale al substring [12345678910]
    - El rango [Dd] equivale a buscar una D mayúscula y una d minúscula

Así como podemos listar los caracteres posibles en cierta posición de la cadena, también podemos listar caracteres que no deben aparecer utilizando el `^`. Así, por ejemplo rango [^a-d] coincide con cualquier caracter que no sea `abcd`.

[4. Expresiones regulares en Python ](#4-RE) 


Para trabajar con expresiones regulares en Python, es necesaria la librería [RE](https://docs.python.org/3/library/re.html), que puede ser instalada usando el instalador de Python (PIP):

```bash
pip install re
```
De todos modos, antes de instalar una librería siempre es importante comprobar si esta está o no instalada. Para ello, desde una terminal de Python debemos escribir:

```python
import re
```
Si la librería está instalada no nos aparecerá ningún error. 


[5. Coincidencias o Matches](#5-matches)


Comenzaremos por aprender sobre las expresiones regulares más simples posibles. Dado que las expresiones regulares se utilizan para operar en strings, vamos a empezas con la tarea más común: los caracteres coincidentes. 

Si un String se corresponde con el criterio que define una expresión regular, se dice que el String hace match con la expresión, y equivalentemente, se dice que la expresión acepta al String.

Podemos encontrar patrones en un texto con el función _search_:

```python
>>> import re
>>> texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
>>> patron = "amet"
>>> re.search(patron, texto)
```

> Para pensar 🤔: ¿Qué resultado obtenemos al ejecutar en la última linea?
>
> 🧗‍♀️Desafio V: imprimí el fragmento del texto entre la posición 22 y 26 ¿Qué resultado obtenés? ¿Qué quiere decir el mensaje _span_?
>
Ahora veamos qué hace _match()_:

```python
>>> import re
>>> texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
>>> patron = "amet"
>>> re.match(patron, texto)
```

>
>Para pensar 🤔: ¿Qué resultado obtenemos con _search()_?¿Qué diferencias observan con _match()_?
>


<details>
  <sumary> Comentarios </sumary>

  El función **match()** de re busca el patrón y devuelve la primera aparición y solo al principio de la cadena. Si se encuentra una coincidencia en la primera línea, devuelve el objeto de coincidencia. Pero, si se encuentra una coincidencia en alguna otra línea, devulve un valor nulo.
</details>

Vamos a ejecutar la última linea con una modificación:

```python
>>> import re
>>> texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
>>> patron = "amet"
>>> re.search(patron, texto).group()
```

>
>Para pensar 🤔: ¿Qué resultado obtenemos? ¿Para qué sirve la función group()?
>
>


Utilicemos ahora otro método que nos permita obtener todas las ocurrencias del substring "amet"

```python
>>> re.findall(patron, texto)
```

>
>Para pensar 🤔: ¿Qué resultado obtenemos? 
>
> 🧗‍♀️Desafio VI: Expresá el patron de búsqueda utilizando lo visto anteriormente sobre metacaracteres y rangos.
>

Como vimos hasta acá el método ```group()``` sirve para mostrar el resultado de una búsqueda, pero veamos:

```python
>>> import re
>>> texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
>>> patron = "amet"
>>> re.search(patron, texto).group()
'amet'
>>> re.search(patron, texto).group(0)
'amet'
```

El método ```group()``` (o ```group(0)```) nos devuelve la coincidencia. Sin embargo si lo que se quiere no es encontrar un patrón en particular, sino obtener lo que está dentro de cierto patrón (por ejemplo lo que hay entre ciertas palabras) hay que modificar el patrón. 
Vamos a ver el siguiente ejemplo:

```Python
>>> import re
>>> texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
>>> patron = "ipsum(.*)sit"
>>> re.search(patron, texto).group()
'ipsum dolor sit amet, consectetur ipsum elit. Amet sit'
>>> re.search(patron, texto).group(0)
'ipsum dolor sit amet, consectetur ipsum elit. Amet sit'
>>> re.search(patron, texto).group(1)
' dolor sit amet, consectetur ipsum elit. Amet '
```

Acá se utilizaron algunos metacaracteres, como lo son el punto (**.**) para indicar que puede ser cualquier carácter, y el asterísco (__*__) para indicar que puede haber 0 o más de estos caracteres. De esta manera obtenemos como resultado lo que se encuentre entre las palabras "ipsum" y "sit", sin embargo observen dos cosas. Primero, el string que nos devuelve tiene dentro un substring que debería haber sido encontrado en la búsqueda: "ipsum dolor sit", pero que sin embargo no aparece. Segundo, nuevamente al hacer ```group()``` o ```group(0)``` obtenemos la coincidencia, pero si nos queremos quedar con el substring que está contenido entre estas palabras debemos utilizar ```group(1)```.
Ahora bien, como vimos, usar el patrón de búsqueda de esta manera prioriza los matches externos, es decir, busca el primer delimitador ("ipsum" en nuestro caso) y luego abarca todo hasta la última aparición del segundo delimitador ("sit"). Existe una forma de priorizar los matches internos y es con el metacarácter ```?```:

```Python
>>> import re
>>> texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
>>> patron = "ipsum(.*?)sit"
>>> re.search(patron, texto).group()
'ipsum dolor sit'
>>> re.search(patron, texto).group(0)
'ipsum dolor sit'
>>> re.search(patron, texto).group(1)
' dolor  '
```

Cuando se quieren obtener todas las apariciones del patrón se utiliza el método ```findall``` el cual actúa para cada coincidencia como si devolviera el ```group(1)```, es decir devuelve en una lista la parte que se encuentra dentro de los delimitadores.

```Python
>>> import re
>>> texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
>>> patron = "ipsum(.*?)sit"
>>> re.findall(patron, texto)
[' dolor ', ' elit. Amet ']
```


[6. Reemplazos o sustituciones masivas](#6-sub)

Ejecutemos ahora la siguiente línea:


```python
>>> re.sub(patron, "###", texto)
```

>
>Para pensar 🤔: ¿Qué resultado obtenemos? ¿Para qué sirve la función _sub_?
>

La función _sub_ permite reemplazar todos las ocurrencias del patrón por otro patrón en un String.

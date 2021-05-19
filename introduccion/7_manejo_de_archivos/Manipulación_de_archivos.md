# *Lectura & Escritura de archivos con Python*

# Guias de Trabajo
* [1. Archivos](#1-archs)
* [2. Apertura de archivos](#2-open)
* [3. Cierre de archivos](#3-cierre)
* [4. Rutas absolutas y relativas](#4-paths)
* [5. Automatización en la construcción de rutas](#5-os)
* [6. Lectura y escritura de archivos](#6-read)


[1. Archivos](#1-archs)


Python tiene la capacidad de acceder y realizar operaciones de lectura/escritura sobre los documentos localizados en un sistema de archivos

Los sistemas _UNIX_, _MacOS_ X y _GNU/Linux_ se basan en la premisa de que todo es un archivo o un directorio, por lo que es común acceder a flujos de datos del dispositivos y/o procesos como si se accediera a un archivo binario. En los sistemas operativos de Windows sin embargo esta premisa no se cumple.

Para Python existen dos tipos de archivos: de texto o binarios. Estos se manipulan de modos distintos. Los **archivos de texto** están formados por una secuencia de líneas, donde cada línea incluye una secuencia de carácteres. Típicamente, cada línea finaliza con el carácter especial de _fin de linea_ (EOL). Si bien existen distintos tipos de carácteres de fin de línea, el más común es ([\n](https://github.com/AJVelezRueda/UCEMA_Fundamentos_de_informatica/blob/master/Python_intro/Expresiones_regulares.md)).

Un **archivo binario** es cualquier tipo de archivo que no es un archivo de texto. Estos solo pueden ser interpretados o leídos por aplicaciones.


[2. Apertura de archivos](#2-open)

Para abrir un archivo de texto, ya sea para usarlo o escribir en el, podemos usar la función nativa de Python `open()`:

```python
open(path_al_archivo, modo) 
```

Donde:

    - "path_al_archivo" es un objeto de tipo str que indica la ruta en la que se encuentra el archivo. 
    
    - "modo" es un objeto de tipo str que indica la forma en la que Python accederá al archivo en cuestión.

Podés encontrar en la siguiente tabla algunos de los modos de lectura más frecuentes y sus difrerencias: 

| Modo de apertura| Significado | 
|-------------	|----------	|
|  r	| abre un archivo solo para lectura|
|  r+	| abre un archivo para lectura y escritura|
|  a	| Abre un archivo para agregar información. Si el archivo no existe, crea un nuevo archivo para escritura|	
|  w	| Abre un archivo solo para escritura. Sobreescribe el archivo si este ya existe. Si el archivo no existe, crea un nuevo archivo para escritura|	


Ahora que sabemos cómo abrir un archivo, el paso siguiente es aprender a cerrarlos. 

[3. Cierre de archivos](#3-cierre)

⚠️ ¡Es muy importante cerrar los archivos una vez abiertos! ¡Como los signos de admiración!

🤔 Pero ¿Por qué? Bueno, aquí van algunas razones:


- Dejar los archivos abiertos, pone al archivo/script en manos de los recolectores de basura.  Aunque el archivo en teoría se cerrará automáticamente, puede que no sea posible.

- De no cerrar los archivos, se puede ralentizar la máquina. Con demasiadas cosas abiertas, pse utiliza más RAM, lo que afectará el rendimiento de la máquina y del programa que estemos creando.

- Muchos cambios en los archivos en Python no entran en vigencia hasta que se cierra el archivo, por lo que si su secuencia de comandos edita, deja abierto y lee un archivo, no se verán las ediciones.


Ahora bien, ¿cómo podemos entonces cerrar un archivo luego de abrirlo? Existe un método `close()`:

```python
archivo = open(path_al_archivo, modo) 
archivo.close()
```

Sin embargo, existe otra forma de apertura de archivos que nos ahorra este paso y siempre nos asegura el cierre de adecuado:


```python
with open(path_al_archivo, modo) as miarch:
    #Aquí van las líneas de procesamiento del archivo
```
Este modo de apertura nos asegura el cierre del archivo al salir del bloque `with`, aún cuando aparezcan errores. Es por eso que esta es la forma más recomendada para la apertura de archivos.


* [4. Rutas absolutas y relativas](#4-paths)

En todos los sistemas operativos modernos la estructura de archivos es jerárquica y depende de los directorios. Semejante a una estructua arbórea en la que existe un nodo (un directorio o carpeta), que contiene los restantes directorios o archivos.

El path o ruta a un archivo, será entonces, el recorrido de directorios o carpetas que debemos recorrer para llegar a nuestro archivo. Esta se escribe separando los nombres de los respectivos directorios separados por `/`. Esto es lo que se conoce como la ruta absoluta al archivo:


```bash
windows  "C:\home\Facultad\Fundamentos\Manipulación_de_archivos.md"
Linux  "/home/Facultad/Fundamentos/Manipulación_de_archivos.md"
```

Las rutas tambien pueden ser escritas de un modo más compacto o acortado. Se suelen escribir de forma relativa a un determinado directorio. Veamos un ejemplo:


```
/
└── home/  ← carpeta de referencia
    │
    ├── Facultad/ ← Directorio de trabajo
    |   └── Estadística 
    │   └── Fundamentos/  
    │       └── Manipulación_de_archivos.md
    └── Fotos  ← Otro directorio
```

Imaginemos que esta es la estructura de archivos de nuestra computadora, donde existen dos carpetas en el home: _Fotos_ y _Facultad_. Dentro de la carpeta _Facultad_, podemos encontrar a su vez dos directorios: _Fundamentos_ y _Estadistica_. Nuestra carpeta de trabajo actual es la de Fundamentos, donde tenemos nuestro archivo de interes _Manipulación_de_archivos.md_. 

Desde el directorio _Facultad_ podemos escribir la ruta relativa a nuestro archivo del siguiente modo:

```bash
./Fundamentos/Manipulación_de_archivos.md
/Fundamentos/Manipulación_de_archivos.md
```
Ahora si quisieramos acceder a las _Fotos_, podemos hacer:

```bash
cd ../Fotos
```

Como seguramente pudiste deducir un punto (.) se utiliza para referenciar al "directorio actual" y los dos puntos seguidos (..) se utilizan para subir en la jerarquía


>
> 🧗‍♀️ Desafío I: Creá un archivo de prueba (`bio.txt`) en la carpeta destinada a los prácticos de la materia.
>

[5. Automatización en la construcción de rutas](#5-os)

Cada programa que se ejecuta en su computadora tiene un directorio de trabajo actual, o `cwd`. Se asume que cualquier nombre de archivo o ruta que no comience con la carpeta raíz se encuentra en el directorio de trabajo actual. Se puede obtener el directorio de trabajo actual como un _string_, utilizando la biblioteca _**`os`**_. 


Esta biblioteca del sistema operativo de Python proporciona funciones para interactuar con el sistema operativo. Esta incluye métodos que como ```os.getcwd()``` o ```os.chdir()```, que nos permitirá conocer el directorio de trabajo o cambiar de directorio de forma automática:
```Python
>>> import os
>>> os.getcwd()
'/home/Ana'
>>> os.chdir('/home/Ana/Documents')
>>> os.getcwd()
'/home/Ana/Documents'
```
Aquí, el directorio de trabajo actual es '/home/Ana' y cambiamos al directorio '/home/Ana/Documents'. Python mostrará un [error](https://github.com/AJVelezRueda/UCEMA_Fundamentos_de_informatica/blob/master/Python_intro/Manejo_excepciones.md) si intenta cambiar a un directorio que no existe.

>
> 🧗‍♀️ Desafío II: Investigá sobre los métodos ```os.mkdir()``` y ```os.listdir()```
>


[6. Lectura y escritura de archivos](#6-read)

Ya a esta altura se estarán preguntando qué tipo de procesamientos o manipulaciones podemos hacer de un archivo. Bueno, la respuesta más obvia dado el título de esta sección es "leerlos y escribir" ¡Si, exactamente eso es lo que aprenderemos ahora mismo! 

La escritura de los archivos en Python se hace de forma sencilla con el método `write()`, que toma como parámetro un string con el contenido que desamos almacenar en el archivo:


```python
with open(path_al_archivo, modo) as miarch:
    miarch.write("Este es el contenido del archivo")
```
>
> 🧗‍♀️ Desafío III: Abrí el archivo `bio.txt` y escribí una mini biografía de presentación.
> Para pensar 🤔:¿Cómo darías formato al texto que estas creando?
>

Hemos visto que resulta relativamente sencillo escribir archivos con Python, sin embargo, la lectura de los archivos puede realizarse de múltiples formas. Como vimos anteriormente, los *archivos de texto* están formados por una secuencia de lineas, sepradas por un caracter especial de fin de línea. Por ello resulta lógico pensar  que existan más de una manera de leer un archivo:

- Línea a linea
- Archivo completo

Para que quede más claro veamos un ejemplo concreto. Ejucutá las siguientes líneas (recordá adaptar el path a tu archivo de prueba).

```python
bio = open("bio.txt", "r")
bio.read()
```

Ahora probemos las siguientes líneas de código:

```python
bio = open("bio.txt", "r")
bio.readlines()
```

>
> Para pensar 🤔:¿Qué diferencias notás? ¿Para qué sirve cada método? ¿Que tipo de dato obtenemos en cada caso? Usá la función type() para explorarlo:
>

<details>
  <summary>Ayuda</summary>
type(bio.readlines())
</details>


En resumen, podemos utilizar los siguientes modos de lectura de archivos:

 * `.read()` Lee del archivo según el número de bytes de tamaño. Si no se pasa ningún, entonces lee todo el archivo.
 
 * `.readline()` Lee como máximo el número de caracteres de tamaño de la línea. Esto continúa hasta el final de la línea y luego regresa. 
 
 * `.readlines()` Esto lee las líneas restantes del objeto de archivo y las devuelve como una lista. 

>
> 🧗‍♀️Desafio IV: Descargá el archivo [`manipulacion_archivos.txt`](https://github.com/AJVelezRueda/UCEMA_Fundamentos_de_informatica/blob/master/Python_intro/manipulacion_archivos.txt) y creá un programa que lea su contenido y lo imprima en pantalla el resultado de la búsqueda de la expresión `-(.*)-`
>
>Para pensar 🤔: ¿Qué significa dicha expresión regular? Imprimí todo el contenido del archivo y descubrí qué hace este personaje incógnito
>
>Para pensar 🤔: ¿Creés que habrá una forma más práctica de leer archivos estructurados o tabulados?
>
> ¡Te dejo con la intriga hasta nuestro capítulo de análisis de datos! Por ahora, hasta aquí llegamos 👋 
>
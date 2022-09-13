> Nota: esta guía está orientada a una instalación local en Linux.

# Entorno local

Para utilizar Python localmente (es decir, en tu computadora en lugar de en una plataforma online como [Replit](https://replit.com/) o [Mumuki](https://mumuki.io)) vamos a tener que instalar algunos programas y aprender a usar terminales. ¡Acompañános!

## 1. Terminales

Abrí una terminal. Notarás que aparece algo similar a lo siguiente:

```shell
mi_nombre@mi_computadora:~$
```

Esto lo que está indicando es que iniciaste sesión en la computadora `mi_computadora` con un usuario llamado `mi_nombre`. Además, el signo `$` (también llamado prompt) indica que la terminal está lista para aceptar comandos. Por último, el símbolo `~` indica que estás en el directorio principal de `mi_nombre`, también denominado _home_.

¿Y qué comandos podés ejecutar? Estos son algunos de los (tantísimos) disponibles:

  * `cd`: cambia de directorio
  * `ls`: muestra los contenidos del directorio
  * `pwd`: muestra el directorio actual

## 2. Instalación de Python

La forma más sencilla para instalar Python en Ubuntu (20.04 o superior) es con el siguiente comando:

```bash
$ sudo apt install python3 python-is-python3 python3-pip
```

## 3. Instalación de Visual Code

Visual Code es uno de los editores de código más comunes y flexibles (en 2022). Para instalarlo en Ubuntu ejecutaremos lo siguiente:

```bash
$ sudo snap install code
```

O, si este comando genera una advertencia, podremos hacer lo siguiente:

```bash
$ sudo snap install code --classic
```

## 4. Probando todo

Para editar un archivo, podés abrir Visual Code desde el menú de aplicaciones, o ejecutando en una terminal el comando `code`. Ejemplo:

```bash
$ code programa.py
```

Luego, para ejecutar los contenidos del archivo, podés hacer:

```bash
$ python <programa.py>
# en modo interactivo
$ python -i <programa.py>
```

## 5. Proyectos

Cuando empezamos a tener muchos archivos de código, conviene hacer orden 🧹. Por eso vamos a organizar nuestros `.py` dentro de un directorio que representará un _proyecto_, es decir, un conjunto de materiales que están relacionados de alguna forma.

¿Y cómo creamos directorios la terminal de Linux? ¡Con el comando `mkdir`!

```bash
# crea un directorio (inicialmente) vacío
$ mkdir mi_proyecto
```

¿Y si nos arrepentimos? Podemos borrar el directorio con `rmdir`:

```bash
$ rmdir mi_proyecto
```

¡Pero cuidado! Esto funcionará sólo si el directorio está vacío (y esto es bueno, porque si nos equivocamos podríamos estar borrando de más 😅).

Finalmente, si queremos _abrir_ un proyecto y editar sus archivos, podremos navegar movernos hacia el directorio correspondiente y luego abrir VisualCode allí:

```bash
$ mv mi_proyecto
# el . significa "el directorio donde estoy actualmente"
$ code .
```

## 6. De acá para allá

Otros comandos que serán útiles para la gestión de archivos son los siguientes:

  * `cat`: muestra los contenidos de un archivo (entre otras cosas)
  * `cp`: copia un archivo
  * `mv`: mueve un archivo
  * `touch`: crea un archivo vacío
  * `sed`: realiza ediciones (sencillas) sobre un archivo
  * `echo`: imprime un mensaje por consola

# 1. Terminales

Abrí una terminal. Notarás que aparece algo similar a lo siguiente:

```shell
mi_nombre@mi_computadora:~$
```

Esto lo que está indicando es que iniciaste sesión en la computadora `mi_computadora` con un usuario llamado `mi_nombre`. Además, el signo `$` (también llamado prompt) indica que la terminal está lista para aceptar comandos. Por último, el símbolo `~` indica que estás en el directorio principal de `mi_nombre`, también denominado _home_.

¿Y qué comandos podés ejecutar? Estos son algunos de los (tantísimos) disponibles:

  * `cd`: cambia de directorio
  * `ls`: muestra los contenidos del directorio
  * `pwd`: muestra el directorio actual
  * `cat`: muestra los contenidos de un archivo (entre otras cosas)
  * `cp`: copia un archivo
  * `mv`: mueve un archivo
  * `touch`: crea un archivo vacío
  * `mkdir`: crea un directorio vacío
  * `sed`: realiza ediciones (sencillas) sobre un archivo
  * `echo`: imprime un mensaje por consola

# 2. Instalación de Python

La forma más sencilla para instalar Python en Ubuntu (20.04 o superior) es con el siguiente comando:

```bash
sudo apt install python3 python-is-python3 python3-pip
```

# 3. Instalación de Viscual Code

Visual Code es uno de los editores de código más comunes y flexibles (en 2022). Para instalarlo en Ubuntu ejecutaremos lo siguiente:

```bash
sudo snap install code
```

O, si este comando genera una advertencia, podremos hacer lo siguiente:

```bash
sudo snap install code --classic
```

# 4. Probando todo

Para editar un archivo, podés abrir Visual Code desde el menú de aplicaciones, o ejecutando en una terminal el comando `code`. Ejemplo:

```bash
code programa.py
```

Luego, para ejecutar los contenidos del archivo, podés hacer:

```bash
python <programa.py>
# en modo interactivo
python -i <programa.py>
```
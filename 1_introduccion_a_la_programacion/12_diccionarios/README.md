> Basado en https://github.com/mumukiproject/mumuki-guia-python-registros

# 3. Diccionarios

Muchas veces, cuando representamos cosas de la vida real en nuestros programas, necesitamos poder agrupar múltiples características de esas cosas de alguna forma.

Te presentamos una estructura que nos va a ayudar en esa tarea: los diccionarios. :grin:

## 1. Que ejercicio monumental

Una historiadora está recopilando información acerca de distintos monumentos a lo largo y ancho del mundo :earth_americas:. En principio solo quiso saber el nombre, ubicación, y año de construcción de cada monumento. :moyai:

Para eso almacenó cada dato en una variable:

```python
nombre_estatua_de_la_libertad = "Estatua de la Libertad"
locacion_estatua_de_la_libertad = "Nueva York"
anio_de_construccion_estatua_de_la_libertad = "1886"
nombre_cristo_redentor = "Cristo Redentor"
locacion_cristo_redentor = "Rio De Janeiro"
anio_de_construccion_cristo_redentor = "1931"
```

Ahí es cuando se dio cuenta que no era conveniente :unamused:: si bien la información entre las variables estaba relacionada, la estaba almacenando por separado. Entonces pensó: ¿no existirá alguna forma de representar las distintas características o propiedades de una misma cosa de forma agrupada?

> Luego de investigar un poco, encontró una mejor manera para guardar la información de los monumentos. Podés verla escribiendo en la consola:

> ```python
>>> estatua_de_la_libertad
>>> cristo_redentor
>>> torre_eiffel
>>> taj_mahal
>>> coliseo
```




### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
estatua_de_la_libertad = { "nombre": "Estatua de la Libertad", "locacion": "Nueva York, Estados Unidos de América", "anio_de_construccion": 1886 }
cristo_redentor = { "nombre": "Cristo Redentor", "locacion": "Rio de Janeiro, Brasil", "anio_de_construccion": 1931 }
torre_eiffel = { "nombre": "Torre Eiffel", "locacion": "París, Francia", "anio_de_construccion": 1889 }
taj_mahal = { "nombre": "Taj Mahal", "locacion": "Agra, India", "anio_de_construccion": 1653 }
coliseo = { "nombre": "Coliseo", "locacion": "Roma, Italia", "anio_de_construccion": 80 }


````



### Para pensar

¡Wow! Mucho más organizado, ¿no? :nerd:

Para modelar estos monumentos las variables se inicializaron así:

``` python
estatua_de_la_libertad = { "nombre": "Estatua de la Libertad", "locacion": "Nueva York, Estados Unidos de América", "anio_de_construccion": 1886 }
cristo_redentor = { "nombre": "Cristo Redentor", "locacion": "Rio de Janeiro, Brasil", "anio_de_construccion": 1931 }
torre_eiffel = { "nombre": "Torre Eiffel", "locacion": "París, Francia", "anio_de_construccion": 1889 }
taj_mahal = { "nombre": "Taj Mahal", "locacion": "Agra, India", "anio_de_construccion": 1653 }
coliseo = { "nombre": "Coliseo", "locacion": "Roma, Italia", "anio_de_construccion": 80 }
```




## 2. Tu propio monumento

Los monumentos que probaste en el ejercicio anterior están representados como _diccionarios_, y cada una de sus características (nombre, locación, año de construcción) son _campos_ del diccionario. Por cierto, ¡podemos crear diccionarios de cualquier cosa, con los campos que querramos!

Por ejemplo, podríamos almacenar un libro de modo que cada campo del diccionario fuese alguna característica: su título, su autor, su fecha de publicación, y más. :books:

> ¡Es tu momento del monumento! Inicializa las variables `torre_azadi` y `monumento_nacional_a_la_bandera` con diccionarios de esos monumentos, oriundos de las ciudades de `Teherán, Irán` y `Rosario, Argentina` respectivamente. ¿Te animás a investigar en qué año se terminaron de construir para completar ese campo? :satisfied:




### Pistas

Si no te acordas como inicializamos a los monumentos te mostramos nuevamente a la Torre Eiffel:

```python
torre_eiffel = { "nombre": "Torre Eiffel", "locacion": "París, Francia", "anio_de_construccion": 1889 }
```



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
self.assertEqual(torre_azadi["nombre"].lower(), "torre azadi")
self.assertEqual(torre_azadi["locacion"], "Teherán, Irán")
self.assertEqual(torre_azadi["anio_de_construccion"], 1971)
self.assertEqual(monumento_nacional_a_la_bandera["nombre"].lower(), "monumento nacional a la bandera")
self.assertEqual(monumento_nacional_a_la_bandera["locacion"], "Rosario, Argentina")
self.assertEqual(monumento_nacional_a_la_bandera["anio_de_construccion"], 1957)
````



### Para pensar

¡Buenas habilidades de búsqueda! :mag_right::wink:

Los diccionarios, al igual que las listas, son una _estructura de datos_ porque nos permiten organizar información. Pero ¿en qué se diferencia un diccionario de una lista? :thinking:

En las listas podemos guardar muchos elementos de un mismo tipo que representen una misma cosa (por ejemplo todos números, o todos strings). No existen límites para las listas: pueden tener muchos elementos, ¡o ninguno!

En un diccionario vamos a guardar información relacionada a una única cosa (por ejemplo **un** monumento o **una** persona), pero los tipos de los campos pueden cambiar. Por ejemplo, el nombre y la ubicación de un monumento son strings, pero su año de construcción es un número.


## 3. Los campos de Marte

Cuando consultaste los diccionarios existentes, se veía algo parecido a lo siguiente:

```python
>>> taj_mahal
{ "nombre": "Taj Mahal", "locacion": "Agra, India", "anio_de_construccion": 1653 }
```

Esa consulta era porque estábamos viendo al diccionario `taj_mahal` completo, incluyendo todos sus campos. ¡Pero también se puede consultar por un campo particular! Mirá :eyes::

```python
>>> taj_mahal["locacion"]
"Agra, India"
>>> taj_mahal["anio_de_construccion"]
1653
```

> Inicializamos los planetas `mercurio`, `marte` y `saturno` como diccionarios con los campos `nombre`, `temperatura_promedio` y si `tiene_anillos`.

> Miralos en la consola y cuando termines escribí `listo()`.




### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
mercurio = { "nombre": "Mercurio", "temperatura_promedio": 67, "tiene_anillos": False }
marte = { "nombre": "Marte", "temperatura_promedio": -63, "tiene_anillos": False }
saturno = { "nombre": "Saturno", "temperatura_promedio": -139, "tiene_anillos": True }

def listo():
  pass


````

## 4. Temperatura de planeta

Ahora que agregamos diccionarios de planetas, ¡trabajemos un poco con ellos! :muscle:

> Definí una función `temperatura_de_planeta` que reciba por parámetro un diccionario de planeta y devuelva un string que indica su nombre y su temperatura promedio. ¡Tiene que funcionar para cualquier planeta! :earth_americas: Por ejemplo:

> ```
>>> temperatura_de_planeta(mercurio)
"Mercurio tiene una temperatura promedio de 67 grados"
>>> temperatura_de_planeta(saturno)
"Saturno tiene una temperatura promedio de -139 grados"
>>> temperatura_de_planeta(venus)
"Venus tiene una temperatura promedio de 462 grados"
```




### Pistas

¡Prestá atención a los strings que devuelven los ejemplos! Sólo la parte correspondiente a cada planeta varía, como el `nombre` y la `temperatura_promedio`. Además, tenés que dejar espacios entre las palabras que rodean a `nombre` y `temperatura_promedio`.

También recordá que para concatenar un número a un string, antes debemos convertilo utilizando `str`. :wink:



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
mercurio = { "nombre": "Mercurio", "temperatura_promedio": 67, "tiene_anillos": False }
marte = { "nombre": "Marte", "temperatura_promedio": -63, "tiene_anillos": False }
saturno = { "nombre": "Saturno", "temperatura_promedio": -139, "tiene_anillos": True }
venus = { "nombre": "Venus", "temperatura_promedio": 462, "tiene_anillos": False }

self.assertEqual(temperatura_de_planeta(mercurio), "Mercurio tiene una temperatura promedio de 67 grados")
self.assertEqual(temperatura_de_planeta(saturno), "Saturno tiene una temperatura promedio de -139 grados")
self.assertEqual(temperatura_de_planeta(venus), "Venus tiene una temperatura promedio de 462 grados")
self.assertEqual(temperatura_de_planeta(marte), "Marte tiene una temperatura promedio de -63 grados")
self.assertEqual(temperatura_de_planeta({"nombre":"cualquier planeta", "temperatura_promedio":999}), "cualquier planeta tiene una temperatura promedio de 999 grados")
````

## 5. Moviendo archivos

Por el momento estuvimos creando y consultando diccionarios. ¿No sería interesante poder... modificarlos? :smirk:

La sintaxis para modificar campos de diccionarios es muy similar a lo que hacemos para cambiar los valores de las variables. Por ejemplo, para cambiar la temperatura de un planeta:

```python
>>> saturno["temperatura_promedio"] = -140
```
Ahora imaginá que tenemos un diccionario para representar un archivo, del que sabemos su ruta (dónde está guardado) y su fecha de creación. Si queremos cambiar su ruta podemos hacer...

```python
>>> leeme
{ "ruta": "C:\leeme.txt", "creacion": "23/09/2004" }

>>> mover_archivo(leeme, "C:\documentos\leeme.txt") }
```

Luego el diccionario `leeme` tendrá modificada su ruta:

```python
>>> leeme
{ "ruta": "C:\documentos\leeme.txt", "creacion": "23/09/2004" }
```

> ¡Es tu turno! Definí el procedimiento `mover_archivo`, que recibe un diccionario y una nueva ruta y modifica el archivo con la nueva ruta.




### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
archivo = {"ruta":"/usr/miarchivo.doc", "creacion":"15/02/2019"}
mover_archivo(archivo, "/home/miarchivo.doc")
self.assertEqual(archivo["ruta"], "/home/miarchivo.doc")
archivo = {"ruta":"/usr/miarchivo.doc", "creacion":"15/02/2019"}
mover_archivo(archivo, "/usr/miarchivo.doc")
self.assertEqual(archivo["ruta"], "/usr/miarchivo.doc")
archivo = {"ruta":"/usr/miarchivo.doc", "creacion":"15/02/2019"}
mover_archivo(archivo, "/home/miarchivo.doc")
self.assertEqual(archivo["creacion"], "15/02/2019")
````

## 6. Diccionarios de dos milenios

En el ejercicio anterior modificamos la ruta del diccionario, pero no utilizamos su fecha de creación. ¡Usémosla! Queremos saber si un archivo es del milenio pasado, lo que ocurre cuando su año es anterior al 2000 :back: :

```python
>>> es_del_milenio_pasado({ "ruta": "D:\fotonacimiento.jpg", "creacion": "14/09/1989" })
True

>>> es_del_milenio_pasado({ "ruta": "D:\fotocasamiento.jpg", "creacion": "25/09/2017" })
False
```

> Definí la función `es_del_milenio_pasado`. Te va a ser de ayuda la función `anio` que funciona así:
>
```python
>>> anio("04/11/1993")
1993
```





### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
def anio(anio):
  return int(anio[-4:])

archivo = {"ruta":"", "creacion":"01/01/2012"}
>>> es_del_milenio_pasado(archivo)
False
archivo = {"ruta":"", "creacion":"01/01/2000"}
>>> es_del_milenio_pasado(archivo)
False
archivo = {"ruta":"", "creacion":"23/09/1994"}
>>> es_del_milenio_pasado(archivo)
True
archivo = {"ruta":"", "creacion":"23/09/1994"}
>>> es_del_milenio_pasado(archivo)
True
````

## 7. Postres complejos

 Unos ejercicios atrás te contamos la diferencia entre listas y diccionarios. ¡Pero eso no significa que no podamos usar ambas estructuras a la vez! :wink:

Por ejemplo, una lista puede ser el campo de un diccionario. Mirá estos diccionarios de postres, de los cuales sabemos cuántos minutos de cocción requieren y sus ingredientes:

```python
>>> flan_casero = { "ingredientes": ["huevos", "leche", "azúcar", "vainilla"], "tiempo_de_coccion": 50 }
>>> cheesecake = { "ingredientes": ["queso crema", "frambuesas"], "tiempo_de_coccion": 80 }
>>> lemon_pie = { "ingredientes": ["jugo de limón", "almidón de maíz", "leche", "huevos"], "tiempo_de_coccion": 65 }
```

> Definí la función `mas_dificil_de_cocinar`, que recibe dos diccionarios de postres como argumento y retorna el que tiene más ingredientes de los dos:

> ```python
>>> mas_dificil_de_cocinar(flan_casero, cheesecake)
{ "ingredientes": ["huevos", "leche", "azúcar", "vainilla"], "tiempo_de_coccion": 50 }
```




### Pistas

¡Recordá que existe la función `len`! Y si los dos postres tienen la misma cantidad de ingredientes, podés devolver cualquiera de los dos. :satisfied:



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
self.flan_casero = { "ingredientes": ["huevos", "leche", "azúcar", "vainilla"], "tiempo_de_coccion": 50 }
self.cheesecake = { "ingredientes": ["queso crema", "frambuesas"], "tiempo_de_coccion": 80 }
self.lemon_pie = { "ingredientes": ["jugo de limón", "almidón de maíz", "leche", "huevos"], "tiempo_de_coccion": 65 }
self.assertEqual(mas_dificil_de_cocinar(self.flan_casero, self.cheesecake), self.flan_casero)
self.assertEqual(mas_dificil_de_cocinar(self.cheesecake, self.lemon_pie), self.lemon_pie)
mas_dificil = mas_dificil_de_cocinar(self.flan_casero, self.lemon_pie)
>>> mas_dificil == self.flan_casero or mas_dificil == self.lemon_pie
True
````

## 8. Listas de diccionarios

En el ejercicio anterior te mostramos que un diccionario puede tener una lista entre sus campos. ¿Y al revés? ¿Podemos tener una lista de diccionarios? :thought_balloon:

> Mirá en la consola las listas `monumentos_de_america` y `postres_favoritos`. Hay un postre que no mostramos antes, ¿te das cuenta cuál es solamente leyendo sus ingredientes? :smirk:



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
monumentos_de_america = [ { "nombre": "Monumento Nacional a la Bandera", "locacion": "Rosario, Argentina", "anio_de_construccion": 1957 }, { "nombre": "Estatua de la Libertad", "locacion": "Nueva York, Estados Unidos de América", "anio_de_construccion": 1886 }, { "nombre": "Cristo Redentor", "locacion": "Rio de Janeiro, Brasil", "anio_de_construccion": 1931 } ]

postres_favoritos = [ { "ingredientes": ["galletitas", "dulce de leche", "crema"], "tiempo_de_coccion": 20 }, { "ingredientes": ["huevos", "leche", "azúcar", "vainilla"], "tiempo_de_coccion": 50 }, { "ingredientes": ["queso crema", "frambuesas"], "tiempo_de_coccion": 80 }, { "ingredientes": ["jugo de limón", "almidón de maíz", "leche", "huevos"], "tiempo_de_coccion": 65 } ]


````



### Para pensar

Así como trabajamos con listas de números, booleanos, strings o más listas, también podemos listar diccionarios. Se puede hacer todo lo que hacías antes, como por ejemplo remover (`list.remove`), saber su longitud (`len`) o preguntar por el elemento de cierta posición utilizando los corchetes `[]`. :star_struck:

## 9. 60 dulces minutos

A veces no sólo queremos comer algo rico, sino que queremos comerlo lo antes posible. :smirk: :cake:

> Definí el procedimiento `agregar_a_postres_rapidos`, que recibe una lista con postres rápidos y un postre por parámetro. Si el tiempo de cocción es de una hora o menos, se agrega el diccionario a la lista.



### Pistas

¡Recordá que `tiempo_de_coccion` está expresado en minutos! Por lo tanto, si queremos que se cocine en una hora o menos, tenés que fijarte que ese `tiempo_de_coccion` sea menor a 60 minutos. :wink:

Ah, si es mayor a 60 no tenemos que hacer nada. :sweat_smile:



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
postres_rapidos = [ { "ingredientes": ["galletitas", "dulceDeLeche", "crema"], "tiempo_de_coccion": 20 }, { "ingredientes": ["huevos", "leche", "azúcar", "vainilla"], "tiempo_de_coccion": 50 } ]
postre_de_leche = {"ingredientes":["leche"], "tiempo_de_coccion":90}
agregar_a_postres_rapidos(postres_rapidos, postre_de_leche)
self.assertEqual(len(postres_rapidos), 2)
postres_rapidos = [ { "ingredientes": ["galletitas", "dulceDeLeche", "crema"], "tiempo_de_coccion": 20 }, { "ingredientes": ["huevos", "leche", "azúcar", "vainilla"], "tiempo_de_coccion": 50 } ]
postre_de_leche = {"ingredientes":["leche"], "tiempo_de_coccion":30}
agregar_a_postres_rapidos(postres_rapidos, postre_de_leche)
self.assertEqual(len(postres_rapidos), 3)
self.assertEqual(postres_rapidos[-1], postre_de_leche)
postres_rapidos = [ { "ingredientes": ["galletitas", "dulceDeLeche", "crema"], "tiempo_de_coccion": 20 }, { "ingredientes": ["huevos", "leche", "azúcar", "vainilla"], "tiempo_de_coccion": 50 } ]
postre_de_leche = {"ingredientes":["leche"], "tiempo_de_coccion": 60}
agregar_a_postres_rapidos(postres_rapidos, postre_de_leche)
self.assertEqual(len(postres_rapidos), 3)
self.assertEqual(postres_rapidos[-1], postre_de_leche)
````

## 10. Hay un diccionario en mi diccionario

¿Te acordás cuando vimos que una lista podía estar compuesta por otras listas? ¡Con los diccionarios aplica la misma idea! :hushed: Si tenemos alguna estructura de datos compleja, puede ocurrir que no alcance con representarla únicamente mediante strings, números, booleanos y listas, sino que necesitemos _otro_ diccionario dentro.

¡No se puede vivir a base de postres! Bueno, quizás sí, pero mantengamos una alimentación saludable :stuck_out_tongue_winking_eye:. Mediante un diccionario queremos modelar un menú completo: consiste en un plato principal :curry:, los vegetales de la ensalada que acompaña :tomato:, y un postre :custard: como lo veníamos trabajando, es decir, sigue siendo un diccionario.

Por ejemplo, el siguiente es un menú con bife de lomo como plato principal, una ensalada de lechuga, tomate y zanahoria como acompañamiento y un cheesecake de postre. Como el diccionario es un poco extenso, y para que sea más legible, lo vamos a escribir de la siguiente forma:

```python
menu_del_dia = {
  "plato_principal": "milanesas de berenjena",
  "ensalada": ["papa", "zanahoria", "arvejas"],
  "postre": { "ingredientes": ["queso crema", "frambuesas"], "tiempo_de_coccion": 80 }
}
```

> Averiguá los `ingredientes` del `postre` del `menu_infantil`. Es un diccionario dentro de otro, así que vamos a tener que acceder primero al campo `postre` y luego a su campo `ingredientes`. Si no se te ocurre como podés mirar la pista. :mag:





### Pistas

Veamos un ejemplo. Si quisieras saber los `ingredientes` del `postre` del `menu_del_dia` deberías hacer:

``` python
ム menu_del_dia["postre"]["ingredientes"]
```




### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
menu_del_dia = {
  "plato_principal": "milanesas de berenjena",
  "ensalada": ["papa", "zanahoria", "arvejas"],
  "postre": { "ingredientes": ["queso crema", "frambuesas"], "tiempo_de_coccion": 80 }
}

menu_infantil = {
  "plato_principal": "pizza",
  "ensalada": ["lechuga", "tomate", "zanahoria"],
  "postre": { "ingredientes": ["galletitas", "dulce de leche", "crema"], "tiempo_de_coccion": 20 }
}


````



### Para pensar

Y también podríamos tener diccionarios que adentro tengan diccionarios que adentro tengan dic.... :flushed:

## 11. ¡Azúcar!

Para terminar, trabajemos una vez más con los menúes. :page_facing_up:

> Definí un procedimiento `endulzar_menu`, que recibe un menú y le agrega `azúcar` a los ingredientes de su postre. Si ya tiene azúcar, no importa... ¡le agrega más! :stuck_out_tongue:




### Pistas

Recordá que cada menú tiene un `postre` y que cada postre tiene `ingredientes`. :custard:



### Autoevaluación

Probá las siguientes consultas y verificá que devuelvan lo mismo:

````python
menu = {"plato_principal": "bife de lomo", "ensalada": ["papa", "zanahoria", "arvejas"], "postre": { "ingredientes": ["queso crema", "frambuesas"], "tiempo_de_coccion": 80 }}
endulzar_menu(menu)
self.assertEqual(len(menu["postre"]["ingredientes"]), 3)
>>> menu["postre"]["ingredientes"][-1] == "azúcar" or menu["postre"]["ingredientes"][-1] == "azucar"
True
menu = {"plato_principal": "milanesas", "ensalada": ["lechuga", "cebolla"], "postre": { "ingredientes": ["dulce de leche", "vainillas", "azucar"], "tiempo_de_coccion": 60 }}
endulzar_menu(menu)
self.assertEqual(len(menu["postre"]["ingredientes"]), 4)
>>> menu["postre"]["ingredientes"][-1] == "azúcar" or menu["postre"]["ingredientes"][-1] == "azucar"
True
````



### Para pensar

Durante la lección aprendiste cuál es la utilidad de esta estructura de datos llamada diccionario, cómo acceder a sus campos y modificarlos, y hasta viste que pueden _anidarse_ (es decir, que haya un diccionario dentro de otro). ¡Felicitaciones! :clap:


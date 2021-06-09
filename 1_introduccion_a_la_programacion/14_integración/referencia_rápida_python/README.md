> Basado en https://github.com/MumukiProject/mumuki-apendice-imperativa-javascript

<ul>

<li><a title="" href="#referencia-rapida-del-lenguaje-python">Referencia rápida del lenguaje Python</a>
<ul>
<li><a title="" href="#declaracion-de-funciones">Declaración de Funciones</a></li>
<li><a title="" href="#declaracion-de-procedimientos">Declaración de Procedimientos</a></li>
<li><a title="" href="#operadores-matematicos">Operadores matemáticos</a></li>
<li><a title="" href="#operadores-logicos">Operadores lógicos</a></li>
<li><a title="" href="#comparaciones">Comparaciones</a></li>
<li><a title="" href="#alternativa-condicional">Alternativa Condicional</a></li>
<li><a title="" href="#variables">Variables</a></li>
<li><a title="" href="#repeticion-indexada">Repetición indexada</a></li>
</ul>
</li>
</ul>

<h2 id="referencia-rapida-del-lenguaje-python"> Referencia rápida del lenguaje Python</h2>

El lenguaje Python es utilizado ampliamente para construir software en todo el mundo, siendo una herramienta muy frecuente para el análisis de datos y la construcción de aplicaciones.

<h3 id="declaracion-de-funciones">Declaración de Funciones</h3>

Las funciones en Python se declaran mediante la _palabra clave_ `def` y:

  * los parámetros se declaran entre paréntesis (`(` y `)`), separados por comas (`,`) ;
  * la primera línea (llamada cabecera) se separa del resto (cuerpo) usando un `:`;
  * el cuerpo se declara aplicando un nivel de tabulación;
  * el cuerpo de la función debe tener al menos un retorno, que se expresa mediante `return`.

Ejemplo:

```python
def nombre_de_la_funcion(parametro1, parametro2, parametro3):
  return ...
```

Por otro lado, las mismas pueden ser invocadas escribiendo su nombre y, entre paréntesis y separados por comas, pasando sus argumentos:

```python
nombre_de_la_funcion(argumento1, argumento2, argumento3)
```

Esta forma de invocación se llama _posicional_ porque el orden de los argumentos se corresponde directamente con el orden de los parámetros. Alternativamente, se pueden pasar los argumentos de forma _nombrada_ (o _etiquetada_), en la que la correspondencia se especifica explícitamente...

```python
nombre_de_la_funcion(parametro1 = argumento1, parametro2 = argumento2, parametro3 = argumento3)
```

... y ya no es necesario respetar el orden de los parámetros:

```python
nombre_de_la_funcion(parametro2 = argumento2, parametro3 = argumento3, parametro1 = argumento1)
```

<h3 id="declaracion-de-procedimientos">Declaración de Procedimientos</h3>

Los procedimientos se declaran de forma similar a las funciones, pero sin colocar un `return`. Además, el cuerpo del procedimiento debe tener algún tipo de _efecto_ (es decir, modificar algún elemento del programa), como por ejemplo:

  * modificar una variable global;
  * modificar una estructura de datos tal listas, diccionarios, etc.

Ejemplo:

```python
def nombre_del_procedimiento(parametro1, parametro2, parametro3):
  # acá hay que producir algún efecto
```

Por otro lado, los procedimientos se invocan de la misma forma que las funciones, pero al no tener un `return`, no devolverán nada (o lo que es lo mismo, devuelve `None`, que significa _nada_ en inglés).


<h3 id="operadores-matematicos">Operadores matemáticos</h3>

```python
4 + 5
10 - 5
8 * 9
10 / 5
```

<h3 id="operadores-logicos">Operadores lógicos</h3>

```python
true or false
true and false
not false
```

<h3 id="comparaciones">Comparaciones</h3>

```python
# para cualquier tipo de dato
"hola" == "hola"
"hola" != "chau"

# para números
4 >= 5
4 > 5
4 <= 5
4 < 5
```

<h3 id="alternativa-condicional">Alternativa Condicional</h3>

Los `if`s en Python llevan su condición delante de un `:` y su cuerpo tabulado:

```python
if hay_personas_en_espera():
  llamar_siguiente_persona()
```

Además, los `if`s pueden opcionalmente tener un `else`:

```python
if hay_personas_en_espera():
  llamar_siguiente_persona()
else:
  esperar_siguiente_persona()
```

Por último, podemos combinar varios `if`s para tomar decisiones ante múltiples condiciones usando `elif`:

```python
if hay_personas_en_espera():
  llamar_siguiente_persona()
elif el_puesto_debe_seguir_abierto():
  esperar_siguiente_persona()
else:
  cerrar_puesto()
```

<h3 id="variables">Variables</h3>

Las variables nos permiten _recordar_ valores y les daremos un valor inicial usando `=`:

```python
pesos_en_mi_billetera = 100
dias_que_faltan_para_el_verano = 10
```

La mismas se actualizan de la misma forma, también mediante `=`:

```python
pesos_en_mi_billetera = 65
dias_que_faltan_para_el_verano = 7
```

En ocasiones las asignaremos usando el valor anterior:

```python
pesos_en_mi_billetera = pesos_en_mi_billetera * 2
dias_que_faltan_para_el_verano = dias_que_faltan_para_el_verano - 1
```

La asignación anterior se puede compactar combinando el signo `=` y la operación:

```python
pesos_en_mi_billetera *= 2
dias_que_faltan_para_el_verano -= 1
```

<h3 id="repeticion-indexada">Repetición indexada</h3>

Las listas pueden ser _recorridas_, visitando y haciendo algo con cada uno de sus elementos. Para ello contamos con la estructura de control `for..in`, que lleva su generador delante de dos puntos (`:`) y su cuerpo tabulado:

```python
patrimonios_de_la_humanidad = [
  {"declarado": 1979, "nombre": "Parque nacional Tikal", "pais": "Guatemala"},
  {"declarado": 1983, "nombre": "Santuario histórico de Machu Picchu", "pais": "Perú"},
  {"declarado": 1986, "nombre": "Parque nacional do Iguaçu", "pais": "Brasil"},
  {"declarado": 1995, "nombre": "Parque nacional de Rapa Nui", "pais": "Chile"},
  {"declarado": 2003, "nombre": "Quebrada de Humahuaca", "pais": "Argentina"}
 ]

cantidad_patrimonios_declarados_en_este_siglo = 0
for patrimonio in patrimonios_de_la_humanidad:
  if patrimonio["declarado"] >= 2000:
    cantidad_patrimonios_declarados_en_este_siglo += 1
```
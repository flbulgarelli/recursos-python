> Tutorial basado en https://github.com/flbulgarelli/http-tutorial

# Tutorial WEB
[Contenido del recorrido](#1-Web)
  * [1. Internte](#1-interntet)
  * [2. La Web](#2-web)
  * [3. Introducción al concepto de CLoud Computing](#3-Cloud-computing)
  * [4. Protocolos de comunicación](#4-protocolos)

[1. Internet](#1-interntet)

Internet se podría definir como la red de redes de computadoras, conectadas por medio de un cableado físico que permite intercambiar información entre todos sus usuarios.

Para acceder al servicio que ofrece la información, debemos tener dos programas que se ejecutan en dos computadoras diferentes y que nos permiten compartir recursos.

A la computadora que ejecuta el programa que proporciona el recurso o información se la denomina **servidor** y a la computadora que consume un recurso o información se la denomina **cliente**. En la computadora del cliente se ejecutará entonces el programa que le permite utilizar el recurso o leer la información.

Pero ¿Qué tipo de recursos pueden brindarse o consimirse a través de internet? Por medio de Internet podemos enviar mensajes, programas ejecutables, archivos de texto, consultar bases de datos, etc.

[2. La Web](#2-web)
La Web en particular, diminutivo de World Wide Web, es un conjunto de páginas interconectadas por las cuales podemos navegar.

Estas páginas web están pensadas para consumir contenido hipertextual, es decir  contenido que contiene vínculos o enlaces a otros contenidos.

[3. Introducción al concepto de CLoud Computing](#2-Cloud-computing)

La computación en la nube o Cloud Computing es el consumo o prestación bajo demanda de recursos tecnologicos a través de Internet.

En lugar de comprar y mantener servidores y centros de datos físicos(es decir una super duper máquina en tu casa), podés consumir los servicios tecnológicos, como potencia informática, almacenamiento y bases de datos, según te sea necesario, en el momento que te sea necesario, de un proveedor.

[4. Protocolos de comunicación](#4-protocolos)

¿Alguna vez te preguntaste cómo es que logramos comunicarnos los seres humanos? ¿Cómo es que las palabras pueden estructurarse en conversaciones ordenadas? Bueno tal y como explica el Dr. Juan Eduardo Bonnin,<a href="https://www.youtube.com/watch?v=jrA70HwWnts&t=9s">en su video</a>, los seres humanos somos capaces de estructurar las palabras, y estas en oraciones que devienen en conversaciones. En este proceso se pone en juego no solo cuestiones ficiológicas, sino también cuestiones culturales y personales, como: la lengua, las normas sociales, los valores culturales, los intereses y propósitos individuales. Por tanto, lo que pensamos como un simple intercambio de palabras, se convierte en una actividad compleja, matizada con el ritmo de todo esta información extra...o meta 😝

Los protocolos, como verás, forman parte de nuestras vidas más de lo que pensábamos. Y estos pueden variar según el entorno en el que nos movemos. Cada ámbito posee sus propias reglas para la comunicación. No nos expresamos de igual modo cuando estamos en un recital, que cuando estamos en la facultad ¿No? 🙏

Este conjunto de reglas de comunicación, implícitas o explícitas, se denomina protocolo y en Internet hay uno específico para establecer la comunicación entre servidores y clientes. Este protocolo fue creado para la transferencia de archivos hipertextuales y se llama justamente HTTP, por las siglas en inglés de protocolo de transferencia de hipertexto (HyperText Transfer Protocol).


👇🏽 Vamos a ver un poco de qué se trata


# Tutorial HTTP
- [Tutorial HTTP](#tutorial--http)
  * [1. Primeros pedidos](#1-primeros-pedidos)
  * [2. Códigos de respuesta](#2-codigos-de-respuesta)
  * [3. Parámetros](#3-parametros)
  * [4. Paginación](#4-paginacion)
  * [6. URLs y URIs](#6-urls-y-uris)
  * [7. Resolución de dominios](#7-resolucion-de-dominios)
  * [8. Cabeceras](#8-cabeceras)
  * [9. Compresión](#9-compresion)
  * [10. Desde el navegador](#10-desde-el-navegador)
  * [11. Borrando contenido](#11-borrando-contenido)
  * [12. Creando y actualizando contenido](#12-creando-y-actualizando-contenido)
  * [13. Sobre la semántica de los verbos](#13-sobre-la-semantica-de-los-verbos)
  * [14. Recursos](#14-recursos)
  * [15. Paréntesis: servidores y despliegue](#15-parentesis-servidores-y-despliegue)
  * [16. Redirecciones](#16-redirecciones)
  * [17. Seguridad](#17-seguridad)
  * [18. HTTP es stateless](#18-http-es-stateless)
  * [19. Negociación de contenido](#19-negociacion-de-contenido)
  * [20. Requests condicionales](#20-requests-condicionales)
  * [21. Contenido estático y dinámico](#21-contenido-estatico-y-dinamico)

> 🏁 Antes de empezar, repasemos: ¿qué es una arquitectura cliente-servidor? ¿cómo funciona? ¿Cuál es el cliente por antomasia de la Web?
>
> 🤔 Para pensar: ¿qué tecnologías se usan en la Web? ¿En qué se desarrolla un cliente? ¿Y un servidor?
>
>📚 Para indagar antes de empezar: ¿Cuál es la diferencia entre un sitio Web y una API web?

## 1. Primeros pedidos

Cada recurso de la web es localizable gracias a un identificador unívoco llamado URL, por las siglas en inglés de Localizador Uniforme de Recurso (Uniform Resource Locator). Las URL nos dan tanto la ubicación de un recurso como la manera de conseguirlo.

> 🤔 Para pensar: ¿a qué corresponde cada parte de una URL?

Para empezar, intentemos establecer nuestra primera comunicación con un servidor, para romper el hielo de esta conversación 🤣


Vamos a hacer nuestro primer pedido, para ello usaremos la biblioteca <a href="https://2.python-requests.org/es/latest/user/quickstart.html">**requests**</a> de Python. Podes instalarala haciendo:


```bash
$ pip install requests

```

Luego desde el intérprete de python podremos hacer finalmente nuestro primer pedido:


```python
>>> import requests
>>> r = requests.get('https://macowins-server.herokuapp.com/prendas/1')
>>> r.json()
{
  "id": 1,
  "tipo": "pantalon",
  "talle": 35
}
```

Veremos que lo que nos devuelve no es HTML, sino un formato llamado JSON.

>
>📚 Para indagar: ¿Sabés qué es HTML? Si aún no conoces este tipo de lenguaje hacé Ctr+u y observalo _in situ_
>
> 🤔 Para pensar: ¿Qué características tiene este formato? ¿Qué tipo de datos puede soportar? ¿por qué devolver JSON? ¿Quién puede leerlo? ¿A quién le sirve?




>🏅 DESAFIO I: Ahora te toca a vos, hacé otro pedido para traer a la prenda `20`. Deberías obtener el siguiente resultado:

```bash
{
  "id": 20,
  "tipo": "saco",
  "talle": "XL"
}
```

## 2. Códigos de respuesta

 ¿Cuántas prendas existirán? ¿Existirá la prenda 400?

> 🏅 Desafío II: ¡averigualo! Hacé `requests.get('https://macowins-server.herokuapp.com/prendas/400')` y observá qué sucede.

<details>
  <summary>Respuesta</summary>

```python
  >>> import requests
  >>> r = requests.get('https://macowins-server.herokuapp.com/prendas/400')
  >>> r.json()
```
</details>

¡Momento! ¿Será un error? ¿Habrá forma de saberlo a ciencia cierta?

```python
>>> r.headers

{'Server': 'Cowboy',
'Connection': 'keep-alive',
'X-Powered-By': 'Express',
'Expires': '-1',
'Content-Type': 'text/html; charset=utf-8',
'Content-Length': '0',
'Etag': 'W/"0-2jmj7l5rSw0yVb/vlWAYkK/YBwk"',
'Vary': 'Accept-Encoding',
'Date': 'Sat, 27 Feb 2021 19:14:21 GMT',
'Via': '1.1 vegur'}
```

Como dijimos antes, una conversación no se trata de la simple enunciación de palabras al azar. Existe un intercambio regulado o normado, donde es de esperar una estructura simple de enunciaciones/preguntas y respuestas.

> En este caso ¿de qué tipo de respuesta se trata? Si tuvieras que expresarlo en emojis ¿Qué emoji es el 400?

> ✍️ Autoevaluación: ¿Para qué sirve el método `headers`? ¿Que nos permitió?

> 🏅 Desafío III: contrastá con lo que sucede al hacer get de `'https://macowins-server.herokuapp.com/prendas/1'` ¿Qué te devuelve el método headers?

<details>
  <summary>Respuesta</summary>

```python
  >>> import requests
  >>> r = requests.get('https://macowins-server.herokuapp.com/prendas/400')
  >>> r.headers

{'Server': 'Cowboy',
'Connection': 'keep-alive',
'X-Powered-By': 'Express',
'Expires': '-1',
'Content-Type': 'application/json; charset=utf-8',
'Content-Length': '50',
'Etag': 'W/"32-i8e+gZ5GUBVXp/2hTq5pj1i9+f8"',
'Vary': 'Accept-Encoding', 'Date': 'Sat, 27 Feb 2021 18:11:12 GMT',
'Via': '1.1 vegur'}
```
</details>

> 🤔 Para pensar: ¿Qué cambió? ¿Qué cambio o cambios te parecen relevates entre ambas respuestas? ¿Qué emoji le pondrías a esta respuesta?

> 🏅 Desafío IV: ¿y que sucederá si consultamos a una dirección que no existe, como por ejemplo `https://macowins-server.herokuapp.com/prindas/1`? ¡Averigualo!

<details>
  <summary>Respuesta</summary>

```bash
$ curl 'https://macowins-server.herokuapp.com/prindas/1' -i
HTTP/1.1 404 Not Found
....
```
</details>

`404` y `200` son códigos de estado (_status code_, también llamados a veces _códigos de respuesta_) y forman parte de toda respuesta HTTP.

> ✍️ Autoevaluación: ¿qué es un status code y para qué me sirve?

Veamos otro código de respuesta más, que nos permitirá usar una funcionalidad que es _muy muy nueva y que quizás aún no ande bien_:

```bash
$ curl 'https://macowins-server.herokuapp.com/nueva-funcionalidad-que-a-veces-no-anda-bien' -i
HTTP/1.1 500 Internal Server Error
X-Powered-By: Express
Vary: Origin, Accept-Encoding
Access-Control-Allow-Credentials: true
Cache-Control: no-cache
Pragma: no-cache
Expires: -1
Content-Security-Policy: default-src 'none'
X-Content-Type-Options: nosniff
Content-Type: text/html; charset=utf-8
Content-Length: 1594
Date: Tue, 21 Apr 2020 12:51:17 GMT
Connection: keep-alive

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Error</title>
</head>
<body>
<pre>TypeError: req.ups is not a function<br> &nbsp; &nbsp;at module.exports (/home/usuario/Documents/http-tutorial/server/internal-error.js:3:9)<br> &nbsp; &nbsp;at Layer.handle [as handle_request] (/home/usuario/.nvm/versions/node/v10.20.1/lib/node_modules/json-server/node_modules/express/lib/router/layer.js:95:5)<br> &nbsp; &nbsp;at trim_prefix (/home/usuario/.nvm/versions/node/v10.20.1/lib/node_modules/json-server/node_modules/express/lib/router/index.js:317:13)<br> &nbsp; &nbsp;at /home/usuario/.nvm/versions/node/v10.20.1/lib/node_modules/json-server/node_modules/express/lib/router/index.js:284:7<br> &nbsp; &nbsp;at Function.process_params (/home/usuario/.nvm/versions/node/v10.20.1/lib/node_modules/json-server/node_modules/express/lib/router/index.js:335:12)<br> &nbsp; &nbsp;at next (/home/usuario/.nvm/versions/node/v10.20.1/lib/node_modules/json-server/node_modules/express/lib/router/index.js:275:10)<br> &nbsp; &nbsp;at module.exports (/home/usuario/Documents/http-tutorial/server/not-found.js:12:3)<br> &nbsp; &nbsp;at Layer.handle [as handle_request] (/home/usuario/.nvm/versions/node/v10.20.1/lib/node_modules/json-server/node_modules/express/lib/router/layer.js:95:5)<br> &nbsp; &nbsp;at trim_prefix (/home/usuario/.nvm/versions/node/v10.20.1/lib/node_modules/json-server/node_modules/express/lib/router/index.js:317:13)<br> &nbsp; &nbsp;at /home/usuario/.nvm/versions/node/v10.20.1/lib/node_modules/json-server/node_modules/express/lib/router/index.js:284:7</pre>
</body>
</html>
```

¡Ups! 🙈

> ✍️ Autoevaluación: ¿qué representa el código `500`?


## 3. Parámetros

Hagamos un nuevo pedido, pero ahora a una _ruta_ ligeramente diferente:

```bash
$ curl 'https://macowins-server.herokuapp.com/prendas'
[
  {
    "id": 1,
    "tipo": "pantalon",
    "talle": 35
  },
  {
    "id": 2,
    "tipo": "pantalon",
    "talle": 36
  },
  {
    "id": 3,
    "tipo": "pantalon",
    "talle": 37
  },
  {
    "id": 4,
    "tipo": "pantalon",
    "talle": 38
  },
  ...
  {
    "id": 18,
    "tipo": "saco",
    "talle": "M"
  },
  {
    "id": 19,
    "tipo": "saco",
    "talle": "L"
  },
  {
    "id": 20,
    "tipo": "saco",
    "talle": "XL"
  }
]
```

> 🤔 Para pensar: ¿es lo mismo consultar `/prendas/` que `/prendas/1`? ¿En qué se diferencian?

> 🤔 Para pensar: ¿qué hará `/ventas/2`? ¿`/ventas/`?.

> 🏅 Desafío: hacé `curl 'https://macowins-server.herokuapp.com/ventas'` y `curl 'https://macowins-server.herokuapp.com/ventas/2'` y contrastá el resultado con tu respuesta anterior

Este listado es muy completo, pero por eso también puede ser engorroso para usar. Quizás podríamos traer sólo una parte así...

```bash
$ curl 'https://macowins-server.herokuapp.com/prendas?tipo=pantalon'
[
  {
    "id": 1,
    "tipo": "pantalon",
    "talle": 35
  },
  {
    "id": 2,
    "tipo": "pantalon",
    "talle": 36
  },
  ....
  {
    "id": 10,
    "tipo": "pantalon",
    "talle": 44
  }
]
```

...o así:

```bash
$ curl 'https://macowins-server.herokuapp.com/prendas?tipo=saco'
[
  {
    "id": 16,
    "tipo": "saco",
    "talle": "XS"
  },
  {
    "id": 17,
    "tipo": "saco",
    "talle": "S"
  },
  {
    "id": 18,
    "tipo": "saco",
    "talle": "M"
  },
  {
    "id": 19,
    "tipo": "saco",
    "talle": "L"
  },
  {
    "id": 20,
    "tipo": "saco",
    "talle": "XL"
  }
]
```

> ✍️ Autoevaluación: ¿qué acabamos de hacer? ¿para qué nos sirvió el `?...=...`?

> 🏅 Desafío: Obtené las remeras.

Es común que las APIs que admiten parámetros soporten más de uno, por ejemplo:

```bash
$ curl 'https://macowins-server.herokuapp.com/prendas?talle=40'
[
  {
    "id": 6,
    "tipo": "pantalon",
    "talle": 40
  }
]
```

Además, los parámetros además se pueden combinar, utilizando el signo `&` (se llama _et_, aunque en informática es más común escucharlo por su nombre en inglés _ampersand_)

```bash
$ curl 'https://macowins-server.herokuapp.com/prendas?talle=40&tipo=pantalon'
[
  {
    "id": 6,
    "tipo": "pantalon",
    "talle": 40
  }
]
```

> 🏅 Desafío: Obtené las remeras XS

> ✍️ Autoevaluación: ¿Para qué sirven los parámetros?

## 4. Paginación

Volvamos a `curl 'https://macowins-server.herokuapp.com/prendas'`. ¿Qué pasaría si este listado fuera muy grande? ## TODO simular que creamos muchos productos. O usar ventas

> 🤔 Para pensar: ¿Qué problemas tiene esto?

Ejecutemos nuevamente...

```bash
$ curl 'https://macowins-server.herokuapp.com/prendas' -i
HTTP/1.1 200 OK
X-Powered-By: Express
Expires: -1
Content-Type: application/json; charset=utf-8
Content-Length: 1237
Vary: Accept-Encoding
Date: Tue, 21 Apr 2020 13:05:09 GMT
Connection: keep-alive

[
  {
    "id": 1,
    "tipo": "pantalon",
    "talle": 35
  },
  {
    "id": 2,
    "tipo": "pantalon",
    "talle": 36
  },
...
```

...pero esta vez prestemos atención a esta parte de la respuesta...

```
Content-Length: 794
```

> 💡 Tip:  Probá hacer `curl 'https://macowins-server.herokuapp.com/prendas' -is | grep 'Content-Length'`

...y comparemos el resultado con el de:

```bash
$ curl 'https://macowins-server.herokuapp.com/ventas' -i
HTTP/1.1 200 OK
X-Powered-By: Express
Expires: -1
Content-Type: application/json; charset=utf-8
Content-Length: 73800
Vary: Accept-Encoding
Date: Tue, 21 Apr 2020 13:06:18 GMT
Connection: keep-alive

[
  {
    "id": 1,
    "producto": {
      "id": 19,
      "tipo": "saco",
      "talle": "L"
    },
    "fecha": "1970-02-06T12:00:00.000Z"
  },
...
```

> 🤔 Para pensar: ¿Cual es mayor? ¿Por qué? ¿Qué problema puede representar esto?

Como se observa, tienen tamaños diferentes: a mayor la cantidad de elementos, mayor es la respuesta, y "más pesada" es.

> 🤔 Para pensar: ¿Cuál será más rápido de descargar? ¿Por qué?

Ya sea porque la respuesta es demasiado "pesada", o porque simplemente sólo queremos una parte de la misma, en ocasiones querremos recorrer el resultado como
si fueran las páginas de un libro: de una a la vez. Por eso Macowins nos permite utilizar un parámetro llamado `_page`, con el que podemos decirle qué número de página queremos.

```bash
$ curl 'https://macowins-server.herokuapp.com/ventas/?_page=1' -i
HTTP/1.1 200 OK
X-Powered-By: Express
Expires: -1
X-Total-Count: 500
Access-Control-Expose-Headers: X-Total-Count, Link
Link: <https://macowins-server.herokuapp.com/ventas/?_page=1>; rel="first", <https://macowins-server.herokuapp.com/ventas/?_page=2>; rel="next", <https://macowins-server.herokuapp.com/ventas/?_page=50>; rel="last"
Content-Type: application/json; charset=utf-8
Content-Length: 1456
Vary: Accept-Encoding
Date: Tue, 21 Apr 2020 13:07:23 GMT
Connection: keep-alive

[
  {
    "id": 1,
    "producto": {
      "id": 19,
      "tipo": "saco",
      "talle": "L"
    },
    "fecha": "1970-02-06T12:00:00.000Z"
  },
  {
    "id": 2,
    "producto": {
      "id": 13,
      "tipo": "remera",
      "talle": "M"
    },
    "fecha": "1970-03-15T00:00:00.000Z"
  },
  ...
  {
    "id": 9,
    "producto": {
      "id": 4,
      "tipo": "pantalon",
      "talle": 38
    },
    "fecha": "1970-11-25T12:00:00.000Z"
  },
  {
    "id": 10,
    "producto": {
      "id": 7,
      "tipo": "pantalon",
      "talle": 41
    },
    "fecha": "1971-01-01T00:00:00.000Z"
  }
]
```

```bash
$ curl 'https://macowins-server.herokuapp.com/ventas/?_page=2' -i
HTTP/1.1 200 OK
X-Powered-By: Express
Expires: -1
X-Total-Count: 500
Access-Control-Expose-Headers: X-Total-Count, Link
Link: <https://macowins-server.herokuapp.com/ventas/?_page=1>; rel="first", <https://macowins-server.herokuapp.com/ventas/?_page=1>; rel="prev", <https://macowins-server.herokuapp.com/ventas/?_page=3>; rel="next", <https://macowins-server.herokuapp.com/ventas/?_page=50>; rel="last"
Content-Type: application/json; charset=utf-8
Content-Length: 1464
Vary: Accept-Encoding
Date: Tue, 21 Apr 2020 13:07:51 GMT
Connection: keep-alive

[
  {
    "id": 11,
    "producto": {
      "id": 8,
      "tipo": "pantalon",
      "talle": 42
    },
    "fecha": "1971-02-06T12:00:00.000Z"
  },
....
```

```bash
$ curl 'https://macowins-server.herokuapp.com/ventas/?_page=3' -i
HTTP/1.1 200 OK
X-Powered-By: Express
Expires: -1
X-Total-Count: 500
Access-Control-Expose-Headers: X-Total-Count, Link
Link: <https://macowins-server.herokuapp.com/ventas/?_page=1>; rel="first", <https://macowins-server.herokuapp.com/ventas/?_page=2>; rel="prev", <https://macowins-server.herokuapp.com/ventas/?_page=4>; rel="next", <https://macowins-server.herokuapp.com/ventas/?_page=50>; rel="last"
Content-Type: application/json; charset=utf-8
Content-Length: 1467
Vary: Accept-Encoding
Date: Tue, 21 Apr 2020 13:09:14 GMT
Connection: keep-alive

[
  {
    "id": 21,
    "producto": {
      "id": 6,
      "tipo": "pantalon",
      "talle": 40
    },
    "fecha": "1972-02-06T12:00:00.000Z"
  },
....
```

> 🤔 Para pensar: observá las fechas de venta. ¿Tendrá alguna relación el número de página con la fecha de venta en Macowins?

> 📝 Nota: de la misma forma que que no todos los sitios soportarán los parámetros `talle` o `tipo`, tampoco todos soportarán `_page`

> 🏅 Desafío: ¿cuando pesan las páginas ahora? ¿Más o menos que todas las ventas?


## 6. URLs y URIs

Pero ¿qué es `https://macowins-server.herokuapp.com/ventas/?_page=3`? Informalmente le diremos dirección, aunque su nombre técnico es URL.

¿Y qué es una URL? Es cualquier _string_ con un formato particular llamado _URI_ nos permita _localizar un recurso_, por ejemplo en internet.

Las URIs se componente de:

  * un protocolo
  * un dominio
  * opcionalmente, un puerto
  * una ruta
  * opcionalmente, parámetros
  * opcionalmente, un fragmento, que indica en que sección queremos obtener del recurso que estamos consultando.

Y se ven así: `protocolo://dominio:puerto/ruta#fragmento?parametro1=valor1&parametro2=valor2`. Las URIs son simplemente un formato estandarizado de strings,
que por sí mismo no significa nada. Por ejemplo `cerebro://recuerdos:3403/recientes#hoy?tema=http` es sólo un string que cumple la estructura de una URI, aunque probablemente
no sea muy util (o al menos no el año 2020 🧠)

> 🏅 Desafío: decí usando tus palabras qué significa la URI de este ejemplo _cerebral_ 😛.

> 🤔 Para pensar: ¿cuál es el protocolo que estamos estudiando? ¿Se observa en las URLs que venimos mencionando?

> ✍️ Autoevaluación: ¿es el string _tutoriales://http/introductorio#7_ una URI? ¿Y una URL?


## 7. Resolución de dominios

> 🤔 Para pensar: ¿Qué ocurrirá si hacemos un pedido a un dominio inexistente? ¿Qué código de estado HTTP obtendremos?

Observemos los siguientes pedidos:

```bash
$ curl 'http://localhost:300
curl: (7) Failed to connect to localhost port 300: Connection refused
```

```bash
$ curl 'http://unSitioQueProbablementeNoExistaEnInternet
curl: (6) Could not resolve host: unSitioQueProbablementeNoExistaEnInternet
```

```bash
$ curl 'http://google.com:8902' -i --connect-timeout 5
curl: (28) Connection timed out after 5000 milliseconds
```

¡Ups! En un caso no pudo resolver el dominio, y en el otro, no había nada escuchando en el puerto.

> ✍️ Autoevaluación: ¿Por qué ante problemas de conexión obtenemos errores que no son de HTTP, sino de más bajo nivel?

> ✍️ Autoevaluación: ¿Para qué sirve el flag `--connect-timeout`? Contratá tu respuesta con el lo que dice `curl --help`


Como vemos esto nos abre una serie de nuevos errores: los errores de conexión, que como vemos pueden deberse por ejemplo a:

 * el puerto al que estamos intentando conectarnos no es el adecuado
 * el el dominio no existe en internet

> 💬 Para discutir: Pero, ¿qué es un dominio? ¿Qué otra forma tenemos de llegar a una máquina que sea a través de su dominio?

```bash
$ ping google.com
PING google.com (172.217.172.110) 56(84) bytes of data.
64 bytes from eze06s02-in-f14.1e100.net (172.217.172.110): icmp_seq=1 ttl=54 time=15.8 ms
64 bytes from eze06s02-in-f14.1e100.net (172.217.172.110): icmp_seq=2 ttl=54 time=24.5 ms
64 bytes from eze06s02-in-f14.1e100.net (172.217.172.110): icmp_seq=3 ttl=54 time=24.5 ms
64 bytes from eze06s02-in-f14.1e100.net (172.217.172.110): icmp_seq=4 ttl=54 time=25.2 ms
^C
--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3005ms
rtt min/avg/max/mdev = 15.844/22.553/25.276/3.888 ms
```

```bash
$ ping google.com
PING google.com (172.217.162.14) 56(84) bytes of data.
64 bytes from eze04s07-in-f14.1e100.net (172.217.162.14): icmp_seq=1 ttl=54 time=12.9 ms
64 bytes from eze04s07-in-f14.1e100.net (172.217.162.14): icmp_seq=2 ttl=54 time=27.8 ms
64 bytes from eze04s07-in-f14.1e100.net (172.217.162.14): icmp_seq=3 ttl=54 time=26.3 ms
64 bytes from eze04s07-in-f14.1e100.net (172.217.162.14): icmp_seq=4 ttl=54 time=29.8 ms
^C
--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3005ms
rtt min/avg/max/mdev = 12.928/24.245/29.843/6.650 ms

```

> 🤔 Para pensar: ¿por qué Google tiene múltiples IPs? ¿Que ventaja representa para esta empresa y para quienes lo usamos?

> 🏅 Desafío: ¿a través de qué IP accedés a google desde tu computadora?

## 8. Cabeceras

Antes ya aparecieron. Formalicemos

```
HTTP/1.1 200 OK
X-Powered-By: Express
Vary: Origin, Accept-Encoding
Access-Control-Allow-Credentials: true
Cache-Control: no-cache
Pragma: no-cache
Expires: -1
X-Total-Count: 100
Access-Control-Expose-Headers: X-Total-Count, Link
Link: <https://macowins-server.herokuapp.com/posts/?_page=1>; rel="first", <https://macowins-server.herokuapp.com/posts/?_page=2>; rel="next", <https://macowins-server.herokuapp.com/posts/?_page=10>; rel="last"
X-Content-Type-Options: nosniff
Content-Type: application/json; charset=utf-8
Content-Length: 794
ETag: W/"31a-kfX25hKekB1DHqT0GE68BdzBP1Q"
Date: Sun, 19 Apr 2020 20:18:21 GMT
Connection: keep-alive
```

> 📝 Nota: si bien en CURL 'se muestra de esta mantera (que a su vez tiene que ver con cómo funciona HTTP internamente), la primera línea NO se corresponde con una cabecera, sino que es el código de estado del que ya hemos hablado anteriormente.

Algunas de estas no las entenderemos. Pero las que sí nos dan información relevante:

* `X-Powered-By: QUIEN`: nos dice que software es el que está corriendo en el servidor. No siempre es muy confiable
* `Content-Length: TAMAÑO`: nos dice el tamaño de la respuesta
* `Date: FECHA`: nos dice la fecha en que se generó la respuesta
* `Content-Type: TIPO`: nos dice el tipo de contenido que estamos recibiendo, el cual podría ser, por ejemplo:
  * sonido, como `audio/wav`o `audio/ogg`
  * video, como `video/ogg`
  * una imagen, como `image/jpeg` o `image/gif`
  * un XML `application/xml`
  * un archivo css `text/css`

> 🤔 Para pensar: ¿Cuál fue el `Content-Type` de las respuesta del ejemplo? ¿Por qué devolvió eso?

> 🏅 Desafío: ¿Qué devolverá la página principal (_home_) de nuestro sitio? Averiguá el `Content-Type` de /home

> ✍️ Autoevaluación: ¿Para qué sirven las cabeceras? Mencioná al menos dos.

## 9. Compresión

```bash
$ curl 'https://macowins-server.herokuapp.com/ventas' -i
```

```bash
$ curl 'https://macowins-server.herokuapp.com/ventas' -i -H "Accept-Encoding: gzip"
X-Powered-By: Express
Expires: -1
Content-Type: application/json; charset=utf-8
Vary: Accept-Encoding
Content-Encoding: gzip
Date: Tue, 21 Apr 2020 13:10:58 GMT
Connection: keep-alive
Transfer-Encoding: chunked

^_<8B>^H^@^@^@^@^@^@^C<BD><9D>ˊ&<C7>^QF<F7>z<8A>a<D6>jS<91><F7><D4>3<D8>+kal<BC>^X<A4>1^VH<9A>a,<AF><8C><DF><DD>^?U<FA>^F<BF><BB><BE><D3><F8>#a<B4>Pk^PAT<D6><C9>Ȍ:^]^?<F8><EA>ݻ<BF>=<FE>y<F7><EE><FD>^O߿<FF><E6>]|<BD><FE><E5><F3><97>O<DF><FF><F5><BB>_>=~<B4><FE><F3><BF><FF><C2><FC><FA>_<FF><FE><CB>^O<9F><CF><FF><FE><FE>/^_<BE><FB><F4><FE>??<FD><F0><E3><8F>^_<CF>^_<FF><FA><FD><F5><A3><BF><FF><F3><FF><F8><A7><8F><DF><FD>
<F9><C3><F9><F3><98><FD>x9<D2><CB>Ѿ<8D><F4><CD>q<<FE><FC><EA>8<8E>ߟ^?<FD><FA><CB><FF>^]O<92><F1><E4><A7>x<BE>|<FC><E9><E3><97>^O<FF>#<A2><DF><DC>F<94>_<A2>~{<85>sESCQ<96>^Q%^^<D1>oo#*/<E9>^@9**<A2><E7>^T}<FE>
<F0><F3>#<86>O??<87><94><FB>]D<F5>%u<90><A3>*s4<E8>*<BA>^?f<FD><B1><90>@<86><9A><8C><A7><D3>x<EE><9F><D8>x<FC>^A<F9><E9>2<9E>F<E3><F9><DD>}@<F3>%2H<D0>ض<A8><E3>8^W<B5>N<D1>T^Q<95><B7>,<EA>q^WQ<BC><A4>
r^T<87>
...
```

> 💡 Tip: Probá hacer `curl 'https://macowins-server.herokuapp.com/ventas' -i -H "Accept-Encoding: gzip" | less` para ver mejor el resultado

```bash
$ curl 'https://macowins-server.herokuapp.com/ventas' -i -H "Accept-Encoding: gzip" --compressed
HTTP/1.1 200 OK
X-Powered-By: Express
Expires: -1
Content-Type: application/json; charset=utf-8
Vary: Accept-Encoding
Content-Encoding: gzip
Date: Tue, 21 Apr 2020 13:13:22 GMT
Connection: keep-alive
Transfer-Encoding: chunked

[
  {
    "id": 1,
    "producto": {
      "id": 19,
      "tipo": "saco",
      "talle": "L"
    },
    "fecha": "1970-02-06T12:00:00.000Z"
  },
...
```

> ✍️ Autoevaluación: ¿Qué hizo el _flag_ `--compressed`?


```bash
$ curl 'https://macowins-server.herokuapp.com/prendas/1' -i -H "Accept-Encoding: gzip"
HTTP/1.1 200 OK
X-Powered-By: Express
Expires: -1
Content-Type: application/json; charset=utf-8
Content-Length: 50
Vary: Accept-Encoding
Date: Tue, 21 Apr 2020 13:15:39 GMT
Connection: keep-alive

{
  "id": 1,
  "tipo": "pantalon",
  "talle": 35
}
...
```

> 🤔 Para pensar: ¿Sucedió lo que esperábamos? ¿Por qué puede ser?

## 10. Desde el navegador

¡Probemos estas mismas ideas desde el navegador!

> 🏅 Desafío: consultá 4 sitios diferentes y averiguá para todos ellos qué servidor utilizan,
> si el contenido se transfiere encriptado, y la fecha de expieración del contenido.

## 11. Borrando contenido

> ✍️ Autoevaluación: ¿qué es un método HTTP?

> 🤔 Para pensar: ¿es correcto que permitamos que cualquiera borre contenido?

> 🤔 Para pensar: ¿Habrá algo que impida que no borre nada con un DELETE, o que borre algo con un GET?


## 12. Creando y actualizando contenido

Probemos ahora crear una prenda:

```bash
$ curl -XPOST 'https://macowins-server.herokuapp.com/prendas/'
{
  "id": 21
}
```

Como vemos, se creó una prenda con el id `21`, y lo que obtenemos como respuesta es el _recurso_ creado.

> 🏅 Desafío: ¿qué código de estado devuelve cuando un _recurso_ es creado? Averigualo

> 🤔 Para pensar: ¿Nos es realmente útil crear una prenda sin especificar más nada?

> 🤔 Para pensar: ¿Por qué se creó con el id `21`?

Pero para que las cosas sean más interesantes, vamos a especificar _el cuerpo_ del pedido HTTP, con el contenido de la prenda que queremos crear.

```bash
curl -XPOST 'https://macowins-server.herokuapp.com/prendas/' -i --data '{ "tipo": "chomba", "talle": "XS" }'
{
  "{ \"tipo\": \"chomba\", \"talle\": \"XS\" }": "",
  "id": 22
}
```

> ✍️ Autoevaluación: ¿para qué sirve la opción `--data`?

> 🤔 Para pensar: Hmm, funcionó, pero ¿creó el contenido que queríamos? ¿Por qué?


El servidor de QMP necesita que le especifiquemos el tipo de contenido, para que cuando creemos algo sepa de qué tipo de cosa estamos hablando. Usemos para eso la
cabecera que vimos anteriormente: `Content-Type`


```bash
curl -XPOST 'https://macowins-server.herokuapp.com/prendas/' --data '{ "tipo": "chomba", "talle": "XS" }' -H 'Content-Type: application/json'
{
  "tipo": "chomba",
  "talle": "XS",
  "id": 25
}
```

> 🤔 Para pensar: ¿por qué no especificamos el ID en el cuerpo?

> 🏅 Desafío: Nos quedaron prendas con ids `21` y `22` que no nos sirve; ¡borralas!

> 📝 Nota: el servidor de QMP aceptó la prenda aún sin especificar el tipo de contenido, pero la guardó de una forma incorrecta. Otros servidores podrían haber hecho un intento por descubrir el tipo de
> todas maneras, o haber rechazado el pedido completamente, con un error de la familia `400`.

Como vemos, haciendo POST sobre la ruta de `/prendas` creamos una prenda, sin especificar un id, dado que se generará solo. De todas formas, si quisieramos podríamos haberlo especificado
agregándolo en el cuerpo.

> 🏅 Desafío: Creá una venta.

> 🏅 Desafío: Intentá hacer POST sobre una venta concreta, como por ejemplo `https://macowins-server.herokuapp.com/prendas/1`. ¿Qué sucede?

## 13. Sobre la semántica de los verbos

> 🤔 Para pensar: A los métodos HTTP también se les dice verbos. ¿Por qué?

Como vemos, hay varios verbos (métodos) HTTP:

* `OPTIONS`
* `GET`
* `POST`
* `PUT`
* `PATCH`
* `DELETE`

Nada nos impide borrar con GET, eliminar con POST o consultar con PUT. ¡Son todas convenciones!
Estas convenciones nos hablan de una semántica para cada uno de los verbos, y es importante respetarlas:

* `OPTIONS`: consultar meta-datos o configuraciones de HTTP
* `GET`: consultar un contenido sin efecto
* `POST`: crear un contenido
* `PUT`: actualizar de forma total un contenido
* `PATCH`: actualizar de forma parcial un contenido
* `DELETE`: eliminar un contenido

> 🤔 Para pensar: ¿por qué es importante respetar estas convenciones?


> 🤔 Para pensar: `POST` es uno de los métodos con efecto más antiguos de HTTP, y por eso es común que a veces se lo use
> para resolver operaciones que no encajan en otras semánticas. ¿Se te ocurre algún otro ejemplo fuera de HTTP en que pase algo así?


## 14. Recursos

Formalización de REST: organizaremos nuestras rutas, tanto de una API como de **un sitio común y corriente**, en forma de recursos y _colecciones_.

* `GET /ventas/`: consultar todos (listar)
* `DELETE /ventas/`: borrar todos
* `POST /ventas/`: crear uno
* `POST /ventas/1` crear uno con ID (QMP no lo soporta)
* `GET /ventas/1`: consultar uno
* `PUT /ventas/1`: modificar uno
* `DELETE /ventas/1`: eliminar uno

> 🤔 Para pensar: nuevamente, ¿por qué es importante respetar estas convenciones?

> 🏅 Desafío: ¿cuales de los siguientes sitios tiene (o parecen tener, al menos) rutas REST?
>
>   * Github
>   * Youtube
>   * Facebook
>   * Infobae, Pagina12, La Nacion
>
> 🏅 Desafío: si no se organizan de forma REST, ¿cómo se organizan sus rutas?

> 💬 Para discutir: recursos anidados

> 🏋️ Ejercicio: Pongamos a prueba nuestros conocimientos de REST [con este problema](https://docs.google.com/document/d/1lNQERQZuWsve0k7VUVVPtliX9aR6JE0NC8tamYON_9A/edit)

## 15. Paréntesis: servidores y despliegue

> 🤔 Para pensar: ¿Dónde está desplegado QMP? ¿En la máquina de uno de los docentes? ¿En su máquina? ¿Qué problemas tendría ésto?

> 🏅 Desafío: ¿En dónde está desplegado QMP? ¿Podés averiguarlo las cabeceras HTTP y/o la URL?

> 💬 Para discutir: qué es Heroku y cómo se despliega allí

> 💬 Para discutir: ¿Qué significa _bare metal_? ¿Y qué es la _nube_? ¿Qué ventajas tiene desplegar en uno u otro?

```bash
$ heroku login -i
heroku: Enter your login credentials
Email: me@example.com
Password: ***************
Two-factor code: ********
Logged in as me@heroku.com
```

```bash
$ git push heroku master
Total 0 (delta 0), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote:
remote: -----> Node.js app detected
remote:
remote: -----> Creating runtime environment
remote:
remote:        NPM_CONFIG_LOGLEVEL=error
remote:        NODE_ENV=production
remote:        NODE_MODULES_CACHE=true
remote:        NODE_VERBOSE=false
remote:
remote: -----> Installing binaries
remote:        engines.node (package.json):  unspecified
remote:        engines.npm (package.json):   unspecified (use default)
remote:
remote:        Resolving node version 12.x...
remote:        Downloading and installing node 12.16.3...
remote:        Using default npm version: 6.14.4
remote:
remote: -----> Restoring cache
remote:        Cached directories were not restored due to a change in version of node, npm, yarn or stack
remote:        Module installation may take longer for this build
remote:
remote: -----> Installing dependencies
remote:        Installing node modules (package.json + package-lock)
remote:        added 229 packages from 124 contributors and audited 449 packages in 6.012s
remote:
remote:        7 packages are looking for funding
remote:          run `npm fund` for details
remote:
remote:        found 0 vulnerabilities
remote:
remote:
remote: -----> Build
remote:
remote: -----> Caching build
remote:        - node_modules
remote:
remote: -----> Pruning devDependencies
remote:        audited 449 packages in 1.845s
remote:
remote:        7 packages are looking for funding
remote:          run `npm fund` for details
remote:
remote:        found 0 vulnerabilities
remote:
remote:
remote: -----> Build succeeded!
remote: -----> Discovering process types
remote:        Default types for buildpack -> web
remote:
remote: -----> Compressing...
remote:        Done: 24.6M
remote: -----> Launching...
remote:        Released v10
remote:        https://macowins-server.herokuapp.com/ deployed to Heroku
remote:
remote: Verifying deploy... done.
To https://git.heroku.com/macowins-server.git
   07f9006..aa4b7bd  master -> master
```

## 16. Redirecciones

Consultemos al muy conocido busacador `google.com`:


```bash
$ curl 'http://google.com/' -i
HTTP/1.1 301 Moved Permanently
Location: http://www.google.com/
Content-Type: text/html; charset=UTF-8
Date: Fri, 01 May 2020 21:39:14 GMT
Expires: Sun, 31 May 2020 21:39:14 GMT
Cache-Control: public, max-age=2592000
Server: gws
Content-Length: 219
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN

<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://www.google.com/">here</A>.
</BODY></HTML>
```

¿Qué quiere decir ésto? El servidor de Google nos dijo que en esa ubicación no está lo que andamos buscando, sino en otra. ¿A cuál?

> 🏅 Desafío: mirá las cabeceras y averiguá a dónde tenemos que ir.

<details>
  <summary>Respuesta</summary>

  La cabecera `Location` nos dice a dónde dirigirnos: `http://www.google.com/`
</details>

> 🏅 Desafío: ¿cuál es el nuevo código de estado utilizado?

<details>
  <summary>Respuesta</summary>

  Es `301`: `Moved Permanently`
</details>


`Location` nos dice a dónde (re)dirigirnos. No es de sorprender que ahora el siguiente pedido funcione como esperamos:

```bash
$ curl 'http://www.google.com/' -i
HTTP/1.1 200 OK
Date: Fri, 01 May 2020 21:43:52 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."
Server: gws
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN
Set-Cookie: 1P_JAR=2020-05-01-21; expires=Sun, 31-May-2020 21:43:52 GMT; path=/; domain=.google.com; Secure
Set-Cookie: NID=203=kTYpSPLU8DGcNo-DaJiKWCn3ei0Yo9ASkCoh8-QDQ9KbtxCrnIwxckj3atgK5wB8Ahkk9vPZZFlQfQJgbs80sMvk2CcrvwXLjs-Uaz0wM7cqi9dEx7nrGi1OpL9JELLDwkfahnLGr85bAiFzaHg7a9d-aCAaPcsguQ3MJcQQmE8; expires=Sat, 31-Oct-2020 21:43:52 GMT; path=/; domain=.google.com; HttpOnly
Accept-Ranges: none
Vary: Accept-Encoding
Transfer-Encoding: chunked

<!doctype html>.....
```

Al igual que los navegadores, que automáticamente reconocen este código de estado `301` y nos redirigen automáticamente, `curl` cuenta con la opción `-L`

```bash
curl 'http://google.com/' -iL
HTTP/1.1 301 Moved Permanently
Location: http://www.google.com/
Content-Type: text/html; charset=UTF-8
Date: Fri, 01 May 2020 21:46:14 GMT
Expires: Sun, 31 May 2020 21:46:14 GMT
Cache-Control: public, max-age=2592000
Server: gws
Content-Length: 219
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN

HTTP/1.1 200 OK
Date: Fri, 01 May 2020 21:46:14 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."
Server: gws
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN
Set-Cookie: 1P_JAR=2020-05-01-21; expires=Sun, 31-May-2020 21:46:14 GMT; path=/; domain=.google.com; Secure
Set-Cookie: NID=203=rWirgAnHsiCpyvJffO9W-KmyuhZRK89E8epLs86Fe5jhT9XhAz8aPTFLRzFrUSnxrt_Sbl99LseCkw9wsxkA7vRAC7iw8NfCrZ2HX-r5j4f-NnOjT2ElEsppEQGLFDTO1VDdaG34gZJflszZNV4di-q7-y37cswfG2UIQmg1hNs; expires=Sat, 31-Oct-2020 21:46:14 GMT; path=/; domain=.google.com; HttpOnly
Accept-Ranges: none
Vary: Accept-Encoding
Transfer-Encoding: chunked

<!doctype html>....
```

> ✍️ Autoevaluación: ¿por qué ahora en la salida de `curl` vemos dos grupos de cabeceras?

¡Veamos otro ejemplo! En la primera iteración de QMP originalmente teníamos una ruta `/negocios` que nos respondía...

> 🏅 Desafío: ... ¡averigualo vos! Si produce redirecciones, ya sabés que hacer 😉

<details>
  <summary>Respuesta</summary>

```bash
$ curl 'https://macowins-server.herokuapp.com/negocios' -iL
HTTP/1.1 301 Moved Permanently
X-Powered-By: Express
Location: /sucursales
Vary: Accept
Content-Type: text/plain; charset=utf-8
Content-Length: 45
Date: Wed, 06 May 2020 12:11:15 GMT
Connection: keep-alive

HTTP/1.1 200 OK
X-Powered-By: Express
Expires: -1
Content-Type: application/json; charset=utf-8
Content-Length: 376
ETag: W/"178-uvXmPkvp2cYryJGsbplIHwyzSPA"
Vary: Accept-Encoding
Date: Wed, 06 May 2020 12:11:15 GMT
Connection: keep-alive

[
  {
    "id": 1,
    "direccion": "Avenida Rivadavia 6200"
  },
  {
    "id": 2,
    "direccion": "Avenida Monroe 5100"
  },
  {
    "id": 3,
    "direccion": "Avenida Cabildo 2800"
  },
  {
    "id": 4,
    "direccion": "Avenida Santa Fe 2300"
  },
  {
    "id": 5,
    "direccion": "Avenida Nazca 1900"
  },
  {
    "id": 6,
    "direccion": "Avenida Corrientes 500"
  }
]
```
</details>


¡`/negocios` nos redirije a las `sucursales`!

Probablemente el equipo en algún momento decidió que el nombre "negocios" no era el mejor, pero ya era tarde para renombrar la ruta. Entonces crearon una redirección _permamente_: aunque a partir de ahora **siempre deberemos apuntar nuestro cliente (por ejemplo nuestro navegador) a `/sucursales`**, se mantiene `/negocios`
como un resto evolutivo y por _retrocompatibilidad_. Es decir, la ruta de `/negocios` sólo sigue existiendo para que si alguien sigue consultándola no tenga errores. Como es de esperar, esta ruta nos devuelve un `301`.

Por otro lado, QMP está estudiando agregar una ruta de `/catalogo`, que tenga un listado de todos los productos que están en stock, con sus precios, sucursal dónde conseguirlo, etc. Como construir esa funcionalidad les tomará tiempo, por ahora fueron por una decisión más conservadora.

> 🏅 Desafío: Averiguá que sucede cuando consultás `/catalogo`. Nuevamente prestá atención a las redirecciones.

<details>
  <summary>Respuesta</summary>

```bash
$ curl 'https://macowins-server.herokuapp.com/catalogo' -iL
HTTP/1.1 302 Found
X-Powered-By: Express
Location: /prendas
Vary: Accept
Content-Type: text/plain; charset=utf-8
Content-Length: 30
Date: Wed, 06 May 2020 12:20:19 GMT
Connection: keep-alive

HTTP/1.1 200 OK
X-Powered-By: Express
Expires: -1
Content-Type: application/json; charset=utf-8
Content-Length: 1237
ETag: W/"4d5-FRYAq3czqjuFkgsBzjVbUxGfr2k"
Vary: Accept-Encoding
Date: Wed, 06 May 2020 12:20:19 GMT
Connection: keep-alive

[
  {
    "id": 1,
    "tipo": "pantalon",
    "talle": 35
  },
  {
    "id": 2,
    "tipo": "pantalon",
    "talle": 36
  },
  {
    "id": 3,
    "tipo": "pantalon",
    "talle": 37
  },
  {
    "id": 4,
    "tipo": "pantalon",
    "talle": 38
  },
  {
    "id": 5,
    "tipo": "pantalon",
    "talle": 39
  },
  {
    "id": 6,
    "tipo": "pantalon",
    "talle": 40
  },
  {
    "id": 7,
    "tipo": "pantalon",
    "talle": 41
  },
  {
    "id": 8,
    "tipo": "pantalon",
    "talle": 42
  },
  {
    "id": 9,
    "tipo": "pantalon",
    "talle": 43
  },
  {
    "id": 10,
    "tipo": "pantalon",
    "talle": 44
  },
  {
    "id": 11,
    "tipo": "remera",
    "talle": "XS"
  },
  {
    "id": 12,
    "tipo": "remera",
    "talle": "S"
  },
  {
    "id": 13,
    "tipo": "remera",
    "talle": "M"
  },
  {
    "id": 14,
    "tipo": "remera",
    "talle": "L"
  },
  {
    "id": 15,
    "tipo": "remera",
    "talle": "XL"
  },
  {
    "id": 16,
    "tipo": "saco",
    "talle": "XS"
  },
  {
    "id": 17,
    "tipo": "saco",
    "talle": "S"
  },
  {
    "id": 18,
    "tipo": "saco",
    "talle": "M"
  },
  {
    "id": 19,
    "tipo": "saco",
    "talle": "L"
  },
  {
    "id": 20,
    "tipo": "saco",
    "talle": "XL"
  }
]
```
</details>


Cuando consultamos `/catalogo` nuevamente nos redirige, pero usando un código  `302` quue designa un redirección _temporal_. En otras palabras, el API de QMP nos está diciendo que _por ahora_ si querés consultar el `catalogo` mires las `prendas`. ¡Pero quizás en el futuro esto cambie, así **seguí consultando a `/catalogo`**!

> 📝 Nota: la redirecciones "clásicas" 301 y 302 sólo funcionan (de forma consistente) con GET. Si nos interesa hacer redirects con otros métodos, existen otros códigos de estado: `307` y `308`.

> ✍️ Autoevaluación: explicá con tus palabras la diferencia entre `301` y `302`.



## 17. Seguridad

Miremos más en detalle la ruta que acabamos de descubrir:


```bash
curl https://macowins-server.herokuapp.com/sucursales/
[
  {
    "id": 1,
    "direccion": "Avenida Rivadavia 6200"
  },
  {
    "id": 2,
    "direccion": "Avenida Monroe 5100"
  },
  {
    "id": 3,
    "direccion": "Avenida Cabildo 2800"
  },
  {
    "id": 4,
    "direccion": "Avenida Santa Fe 2300"
  },
  {
    "id": 5,
    "direccion": "Avenida Nazca 1900"
  },
  {
    "id": 6,
    "direccion": "Avenida Corrientes 500"
  }
]
```

Y volvamos también a una pregunta que surgió anteriormente: ¿qué pasaría si intentamos crear una nueva sucursal, o modificar o eliminar una existente? ¿Cualquier debería poder hacerlo?

> 🏅 Desafío: Intentá crear una nueva sucursal que quede cerca de tu casa 🏠. Recordá que tenés que usar el método `POST` y usar `application/json` como `Content-Type`. ¿Te deja hacerlo? ¿Qué código HTTP responde?

<details>
  <summary>Respuesta</summary>

```bash
curl -XPOST https://macowins-server.herokuapp.com/sucursales/ -H 'Content-Type: application/json' --data '{ "direccion": "Calle Falsa 1234" }' -i
HTTP/1.1 401 Unauthorized
X-Powered-By: Express
WWW-Authenticate: Basic
Content-Type: text/html; charset=utf-8
Content-Length: 0
ETag: W/"0-2jmj7l5rSw0yVb/vlWAYkK/YBwk"
Date: Wed, 06 May 2020 14:09:06 GMT
Connection: keep-alive
```
</details>

Se ve que el equipo de QMP aprendió de las lecciones pasadas y ahora no deja que cualquiera modifique sus recursos 😎.

Cuando intentamos modificar las `sucursales` nos dice que el pedido no está autorizado (`401`), y nos propone que nos autentiquemos utilizando el método HTTP _basic_ (`WWW-Authenticate: Basic`), que no es más que el clásico (y no tan seguro 🕵️) _usuario y contraseña_. Para ingresarlo usemos la opción `--user`, con usuario `punpun` y contraseña.... ehmmm.... `punpun` 😛:

```bash
$ curl -XPOST https://macowins-server.herokuapp.com/sucursales/ -H 'Content-Type: application/json' --data '{ "direccion": "Calle Falsa 1234" }' --user 'punpun' -i
Enter host password for user 'punpun':
HTTP/1.1 201 Created
X-Powered-By: Express
Expires: -1
Access-Control-Expose-Headers: Location
Location: https://macowins-server.herokuapp.com/sucursales//7
Content-Type: application/json; charset=utf-8
Content-Length: 48
ETag: W/"30-mf6CooPA8EhdV1CF/A0ifg/X95A"
Vary: Accept-Encoding
Date: Wed, 06 May 2020 14:14:18 GMT
Connection: keep-alive

{
  "direccion": "Calle Falsa 1234",
  "id": 7
}
```

> 🏅 Desafío: ¿Qué sucede si ingresamos una contraseña inválida o un usuario inexistente? ¡Descubrilo!

<details>
  <summary>Respuesta</summary>

```bash
# ingresemos de contraseña asdfdsfdfs
$ curl -XPOST https://macowins-server.herokuapp.com/sucursales/ -H 'Content-Type: application/json' --data '{ "direccion": "Calle Falsa 1234" }' --user 'punpun' -i
Enter host password for user 'punpun':
HTTP/1.1 401 Unauthorized
X-Powered-By: Express
WWW-Authenticate: Basic
Content-Type: text/html; charset=utf-8
Content-Length: 0
ETag: W/"0-2jmj7l5rSw0yVb/vlWAYkK/YBwk"
Date: Wed, 06 May 2020 14:18:16 GMT
Connection: keep-alive
```
</details>


> 💬 Para discutir: `Basic` vs `Bearer`

> 🏅 Desafío: Ahora intentá eliminar la priemera sucursal.

<details>
  <summary>Respuesta</summary>

```bash
$ curl -XDELETE https://macowins-server.herokuapp.com/sucursales/1 --user 'punpun' -i
Enter host password for user 'punpun':
HTTP/1.1 200 OK
X-Powered-By: Express
Expires: -1
Content-Type: application/json; charset=utf-8
Content-Length: 2
ETag: W/"2-vyGp6PvFo4RvsFtPoIWeCReyIC8"
Vary: Accept-Encoding
Date: Wed, 06 May 2020 14:21:47 GMT
Connection: keep-alive

{}
```
</details>

> 🤔 Para pensar: ¿Fue necesario volver a ingresar las credenciales? ¿Por qué?


## 18. HTTP es stateless

Como acabamos de ver, HTTP es olvidadizo 🐠, ¡y no recuerda que yo nos autenticamos!

> 💬 Para discutir:
> - Concepto de sesión
> - Tipos de sesión:
>   - server side vs client side
>   - en memoria vs en cookie
> - `Cookie` y `Set-Cookie`


## 19. Negociación de contenido

> 💬 Para discutir:
> - Accept
> - Content Type



## 20. Requests condicionales

Pidamos la prenda número 20:

```bash
$ curl 'https://macowins-server.herokuapp.com/prendas/20' -i
HTTP/1.1 200 OK
X-Powered-By: Express
Expires: -1
Content-Type: application/json; charset=utf-8
Content-Length: 49
ETag: W/"31-OlDFK7SS8oUCKcn/LZE2poJFDDo"
Vary: Accept-Encoding
Date: Thu, 30 Apr 2020 01:40:19 GMT
Connection: keep-alive

{
  "id": 20,
  "tipo": "saco",
  "talle": "XL"
}
```

Pero esta vez observemos la cabecera `ETag` (por _entity-tag_):

```bash
$ curl 'https://macowins-server.herokuapp.com/prendas/4' -is | grep 'ETag'
ETag: W/"31-OlDFK7SS8oUCKcn/LZE2poJFDDo"
```

¿Qué es ésto? Es un código que identifica unívocamente al estado del recurso. Es decir, el valor `"31-OlDFK7SS8oUCKcn/LZE2poJFDDo"` representa exactamente a una
prenda que tiene `id` `20`, `tipo` `"saco"` y `talle` `"XL"`, ni más ni menos.


Saber esto nos permite hacer uso de una nueva cabecera: `If-None-Match`, que nos permite hacer pedidos especificar uno o más `ETags`, de forma que cuando el `ETag` dado **NO coincida**
con el que tiene el servidor, responda normalmente:

```bash
$ curl 'https://macowins-server.herokuapp.com/prendas/20' -i -H 'If-None-Match: "otracosa"'
HTTP/1.1 200 OK
X-Powered-By: Express
Expires: -1
Content-Type: application/json; charset=utf-8
Content-Length: 49
ETag: W/"31-OlDFK7SS8oUCKcn/LZE2poJFDDo"
Vary: Accept-Encoding
Date: Thu, 30 Apr 2020 01:40:19 GMT
Connection: keep-alive

{
  "id": 20,
  "tipo": "saco",
  "talle": "XL"
}
```

> 🏅 Desafío: ¿Qué sucede cuando coincide? Probá consultar con el valor `"31-OlDFK7SS8oUCKcn/LZE2poJFDDo"` (comillas incluidas)

<details>
  <summary>Respuesta</summary>

```bash
curl 'https://macowins-server.herokuapp.com/prendas/20' -i -H 'If-None-Match: "31-OlDFK7SS8oUCKcn/LZE2poJFDDo"'
HTTP/1.1 304 Not Modified
X-Powered-By: Express
Expires: -1
ETag: W/"31-OlDFK7SS8oUCKcn/LZE2poJFDDo"
Date: Thu, 30 Apr 2020 01:40:04 GMT
Connection: keep-alive
```

</details>

Cuando **coincide**, nos dice que el el recurso _sigue siendo el mismo_, mediante un código `304`.


> 🤔 Para pensar: ¿Y para qué nos podría servir ésto? ¿Por qué creés que no responde un cuerpo en este caso?

Supongamos que ahora modificamos el contenido de la prenda 20, indicando que no tiene stock:

```bash
$ curl -XPATCH 'https://macowins-server.herokuapp.com/prendas/20' --data '{ "enStock": false }' -H 'Content-Type: application/json' -i
HTTP/1.1 200 OK
X-Powered-By: Express
Expires: -1
Content-Type: application/json; charset=utf-8
Content-Length: 69
ETag: W/"45-38RNDuIjR/nqwDhm73CxIQFBqWc"
Vary: Accept-Encoding
Date: Thu, 30 Apr 2020 02:04:18 GMT
Connection: keep-alive

{
  "id": 20,
  "tipo": "saco",
  "talle": "XL",
  "enStock": false
}
```

> ⚠️ ¡Cuidado! Notá que esta vez usamos (por primera vez) `PATCH`, no `PUT`. ¿Por qué pensás que lo hicimos?

Ahora vevmos que el `ETag` es diferente: `"45-38RNDuIjR/nqwDhm73CxIQFBqWc"`. Porque claro, ¡la prenda cambió!

> 🏅 Desafío: si ahora consultamos por la prenda 20, ¿el `ETag` seguirá siendo el mismo? ¿Será `"45-38RNDuIjR/nqwDhm73CxIQFBqWc"` (el nuevo), `"31-OlDFK7SS8oUCKcn/LZE2poJFDDo"` (el viejo) u otro?
> Averigualo obteniendo con `curl` y `grep` el `ETag` de la prenda 20.

Si ahora hacemos un _pedido condicional_ con el viejo `ETag`, la respusta cambiará:

```bash
$ curl 'https://macowins-server.herokuapp.com/prendas/20' -i -H 'If-None-Match: "31-OlDFK7SS8oUCKcn/LZE2poJFDDo"'
HTTP/1.1 200 OK
X-Powered-By: Express
Expires: -1
Content-Type: application/json; charset=utf-8
Content-Length: 69
ETag: W/"45-38RNDuIjR/nqwDhm73CxIQFBqWc"
Vary: Accept-Encoding
Date: Thu, 30 Apr 2020 02:15:18 GMT
Connection: keep-alive

{
  "id": 20,
  "tipo": "saco",
  "talle": "XL",
  "enStock": false
}
```

> 🏅 Desafío: ¿Y si lo hacemos con el nuevo? ¿Qué debería suceder? ¡Averigualo!

> 👀 Para más detalles, ver: https://developer.mozilla.org/en-US/docs/Web/HTTP/Conditional_requests

> 🔎 Para investigar: ¿Qué significa la `W/` en los `ETags`?

## 21. Contenido estático y dinámico

Consultar: `https://macowins-server.herokuapp.com/`.
Observar el pie de página

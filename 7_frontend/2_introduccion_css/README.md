# Introducción a CSS

## Repaso

Repasemos lo visto:

* 🥅️ Red de computadoras: ¿viste que un hilo por sí solo no sirve para mucho, pero si unís muchos formando una red podés sostener papas, evitar que una pelota salga volando de la cancha o pescar decenas de peces? ¿O que si muchas personas se conectan a través de una red social pueden lograr cosas que quizás ninguna hubiera podido hacer sola?  Bueno, las redes de computadoras son parecidas: cuando unís muchas computadoras (a través de cables, ondas de WiFi, 3G o incluso satélites), estas van a poder "hablar" entre sí y compartir información. De esa forma, todas juntas, pueden hacer mucho más que una sola. ¡Y vos también!

* 🌎️Internet: es la "red de redes", ese conjunto de computadoras globales que nos permiten acceder a un montón de información y servicios públicos de estados y empresas a lo largo de tooooodo el mundo. Con una conexión a internet podés consultar la información que está en Wikipedia, enviar mensajes  a través de whatsapp, y usar las aplicaciones de Google Drive, Instagram o TicToc.

* 🕸️La Web: es una de las "cosas" (o, más técnicamente, uno de los servicios) más obvias que podés encontrar en Internet. Se trata de un montón de información organizada en páginas (sí, las famosas páginas Web) que podés encontrar y navegar usando un navegador.

* 🚢️ Navegadores: Son aplicaciones, como Firefox, Chrome o Edge, que nos permiten  navegar la Web y también cuentan con algunas herramientas para ayudarnos a crear nuestras propias páginas. Ojo, no confundirlos con los _buscadores_, que son páginas concretas, como google.com o bing.com, que sirven para buscar otras páginas en toda la Web.

* 🤔️ Google: sí, todo el tiempo escuchamos de este gigante de la tecnología. Pero aunque es una empresa enorme y omnipresente, para nada es la única ni es todopoderosa. Y aunque muchas veces usamos sus productos y servicios, ¡no todos son lo mismo ni son la única opción! Como vimos recién: Chrome es un navegador, pero google.com es un buscador. Y Google Drive son un conjunto de aplicaciones online para crear documentos.

* 🎉️HTML: es el lenguaje con el que construimos el esqueleto de nuestras páginas Web y con el que empezaremos hacer las nuestras. En HTML todo es una etiqueta (tag), que sirve para encerrar a nuestro texto y darle significado. Vimos 3 tags (¡de entre muchísimos!):

* 🗃️ Los archivos HTML deben tener extensión (es decir, terminar en) .html. Los podemos editar con Visual Code y abrirlos con cualquier navegador.


## Dando formato

1. Terminar de armar el HTML. Comentar los tags semánticos:
   1. `html`
   2. `head`, (donde pondremos `title`) `body`
   3. `header`, `section`
2. Cargar el css en un tag `style`. Hay mejores formas de hacerlo, pero las veremos luego porque esta es la más sencilla y rápida.
3. Arrancar por un "truco" que nos va a servir muchísimo: tomar "el control" de los tamaños:

```css
* {
  margin: 0;
  padding: 0;
}
```

4. Vamos darle _estilo_ (es decir, formato) a nuestra cabezera. Dado que esta parte contendrá nuestro título y actividad, tiene que resaltar, así que empezaremos por darle color de fondo (`background-color`) y color de fuente (`color`):

```css
header {
  background-color: #164e98;
  color: white;
}
```

5. ¿Qué otras cosas pueden ayudarnos a resaltar algo? ¡El espacio! Sí, por más antiintuitivo que parezca, si querés que algo resalte, ponele mucho espacio a su alrededor, y para eso vamos a usar `padding`, que nos agrega espacio **dentro** de _la caja_ de un componente html:

```css
header {
  background-color: #164e98;
  color: white;
  padding: 70px 0 45px 0;
}
```


el padding funciona como las agujas del reloj: primero te dice el espacio que va arriba, luego el de la derecha, luego el de abajo y luego el de la izquierda. Otro elemento que nos va a servir para dar espacio es el `margin` que indica cuánto hay espacio **fuera** de la caja:

```css
h1 {
  margin: 0 0 5px;
}
```

6. El centrado es otra propiedad que nos ayuda a concentrar la atención, y la podemos lograr con `text-align`.

```css
header {
  background-color: #164e98;
  color: white;
  padding: 70px 0 45px 0;
  text-align: center;
}
```

7. Ya empieza a tomar otra forma, ¿no? ¡Pero aún podemos hacerlo mejor! Podemos aumentar los tamaños de la fuente (con `font-size`) y hacerla mayúsculas (con `text-transform`)

```css
header {
  background-color: #164e98;
  color: white;
  padding: 70px 0 45px 0;
  text-align: center;
  text-transform: uppercase;
  font-size: 20px;
}
```

Alternativa: cambiar el texto al h1 y h2 individualmente. (40px y 30px). ¿Qué cambia?

8. Hmm, se nos fue un poco la mano, porque ahora todo quedó muy grande. Y otra técnica para que algo resalto es hacer que haya algo que resalte menos cerca. Al fin y al cabo lo primero que queremos que se vea es nuestro nombre, ¿no? Saquémosle entonces _grosor_ a la fuente del h2:

```css
h2 {
  font-weight: lighter;
}
```

9. Y para que ocupe más espacio (¿te acordás que el espacio es importante?)

```css
header {
  background-color: #164e98;
  color: white;
  padding: 70px 0 45px 0;
  text-align: center;
  text-transform: uppercase;
  font-size: 20px;
  letter-spacing: 5px;
}
```

10. Y para cerrar, usemos `sans-serif` como `font-family`.

## Desafío

¡Ahora te toca a vos! Usando las herramientas que vimos, completá tu CV y dale formato. Podés usar todos los elementos HTML y estilos CSS que vimos hasta ahora, pero quizás quieras explorar un poco más sobre las siguiente etiquetas:

1. `ul`, `ol`, `li`
3. `hr`
2. `img`

Para que te sirva de inspiración, te dejamos un `cv_ejemplo.pdf` provisto por canva.com, pero sentite libre de cambiar su estilo tanto como quieras 😁️.

¡El próximo encuentro aprenderemos a ponerlo en línea!

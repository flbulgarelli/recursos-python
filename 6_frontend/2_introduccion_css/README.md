## Introducción a CSS


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

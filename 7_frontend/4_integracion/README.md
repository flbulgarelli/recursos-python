# MacoWins - Entrega 5

🌐 ¡Llegó la hora de permitir que todas las personas ingresen al sitio de MacoWins! Por ello vamos a incluir Flask a nuestro proyecto y convertir nuestro código en una aplicación web.

Esta aplicación debe contar con las siguientes pantallas:

  1. Listado de productos: desde esta página se deben poder ver todos los productos, con su nombre, **primera** categoría y precio. Los productos que no tienen stock deben tener un estilo diferente, fácilmente reconocible. Desde el listado de productos se debe poner navegar a la pantalla de detalle del producto (punto 2).

  2. 🔍 Detalle de producto: debe contener la misma información que la que se encuentra en el listado de productos (nombre, precio, y cantidad en stock), pero además se deben ver **todas** sus categorias y código de producto. También debe ser posible ver en qué sucursal se encuentra y desde allí navegar a la página de detalle de sucursal (punto 3).

  3. Detalle de sucursal: debe mostrar la cantidad de productos en stock, su nombre y dirección (sólo para las físicas). Estos últimos dos datos deben ser incorporados al modelo de objetos. Además, las sucursales que son virtuales deben tener un estilo diferente, fácilmente identificable. En todos los casos, también se deben mostrar los tres productos más vendidos, mostrando por cada uno de ellos los mismos datos que el listado del punto 1, y permitiendo navegar hacia el detalle del producto (punto 2)

  4. Buscador de productos: la home de MacoWins. Desde aquí debe ser posible ingresar un nombre de prenda, una categoría y/o un precio máximo y al presionar enviar obtener todos los productos que encajen con ese criterio. Opcionalmente, debe ser posible navegar hacia el listado completo de productos (punto 1). Cuando se muestra el resultado de la búsqueda, se debe ver claramente cuál fue la búsqueda realizada y permitir realizar una nueva.

  5. Listado de ventas: esta página estará destinada sólamente al equipo que trabaja de MacoWins. Desde allí se deberán poder ver todas las ventas realizadas, de cualquier producto. Se debe poder ver el precio de venta, nombre del producto vendido, fecha y cantidad. Además, debe ser posible ver la sucursal donde se realizó la venta. Por defecto, debe mostrar todas las ventas de MacoWins, debe contar con un filtro que permita mostrar ventas sólo entre dos fechas.

  6. Listado de sucursales: desde esta página se debe poder ver todas las sucursales. Aquellas que son virtuales deben ser claramente distinguibles con un estilo diferente. Se debe mostrar el nombre de la sucursal (ver punto 3) y si es virtual o física, usando un estilo diferente, fácilmente diferenciable. La página debe tener un filtro que permita mostrar todas las sucursales, sólo las físicas o sólo las virtuales.

Consideraciones:

 0. Todas las pantallas deben presentar la misma estructura: pie de página con información del sitio, cabecera con nombre del sitio y enlaces de navegación, cuerpo con los contenidos de la página. Además, debe utilizar la misma tipografía y colores.
 1. La entrega debe ser completamente funcional y debe permitir navegar entre las pantallas.
 2. La aplicación debe ser integrada con [el módulo de `persistencia`](https://gist.github.com/flbulgarelli/3b34f870783cba3d88c996da6acf773c), si no lo fue hecho aún.
 3. Cada uno de los requerimientos debe ser integrado al proyecto usando Git, en múltiples commits con nombres representativos.
 4. Antes de la entrega, los equipos deben entregar bosquejos (a mano alzada o usando una herramienta online como [moqups.com](https://moqups.com/) de cómo se verán las pantallas que implementarán.

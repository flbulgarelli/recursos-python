# MacoWins - Entrega 3

¡MacoWins sigue creciendo! Tenemos nuevos requerimientos y todo parece indicar que seguiremos desarrollando su sistema por varias iteraciones más.

Por eso, antes de empezar:

  1. 🧪 Asegurate de que tu código y sus pruebas automatizadas con pytest estén en un mismo directorio y que las pruebas se puedan ejecutar correctamente y sin errores.
  2. Creá un repositorio en Github y subí tu código al control de versiones. El mismo debe ser público.


## Requerimientos

Y ahora sí, los requerimientos:

  1. ✨ Modelar los _estados_ de prenda, que son modificadores del precio. Hay tres estados diferentes:
      1. `Nueva`: no se modifica el precio de la prenda.
      2. `Promoción`: se le resta un valor fijo, propio de cada promoción.
      3. `Liquidación`: la prenda queda al 50% de su valor original.
  2. 🏗 Modificar el código de las entregas pasadas para que ahora las prendas puedan estar en los estados descriptos arriba. En particular:
      1. Inicialmente una prenda debe ser nueva
      2. En cualquier momento debe ser posible poner a la prenda en liquidación o promoción, o incluso volverla a marcar como nueva.
      3. El precio debe siempre reflejar el estado actual de la prenda. Si el estado cambia, el precio de la misma debe verse afectado instantáneamente y tener impacto en todos los puntos en donde se use: `realizar_compra`, `calcular_precio_final_producto`, etc.
      4. Responder: ¿puede la programación orientada a objetos ayudarnos en este punto? ¿Por qué?
  3. 🆕 A partir de ahora, las prendas pueden tener múltiples categorías (pero siempre al menos una). Realizar los agregados y modificaciones necesarias para que:
      1. Las prendas puedan respondernos si son de una categoría dada, teniendo en cuenta todas las que tiene y aplicando las mismas reglas de búsqueda inexacta explicada en la primera entrega.
      2. Podamos agregarle en cualquier momento nuevas categorías a una prenda existente.
      3. `actualizar_precios_por_categoria` siga funcionando adecuadamente.
  4. 🛍 Dado el éxito de nuestro sistema, múltiples sucursales de MacoWins solicitaron poder gestionar sus propios productos y stock. Modificar el código existente para que sea posible crear múltiples sucursales, y cada una pueda resolver los problemas originalmente planteados. Ejemplo:

  ```python
  sucursal_cabildo.registrar_producto(remera_talle_m)
  sucursal_cabildo.recargar_stock(100, 10)
  sucursal_cabildo.hay_stock(100) # True
  
  sucursal_avellaneda.hay_stock(100) # False
  ```

  5. 🤔 Luego de realizar el cambio anterior, responder: ¿qué objeto debería tener ahora la responsabilidad de resolver el problema de calcular el _precio final_ de un producto?
  6. 🌐 A la franquicia MacoWins se desea incorporar también una sucursal virtual, que es muy similar a las sucursales de siempre, pero tienen formas diferentes de calcular los _gastos del día_:
      1. Las sucursales comunes gastan diariamente un valor fijo, que cada una conoce.
      2. La sucursal virtual se comporta de igual forma forma, pero si supera las 100 ventas diarias, su gasto pasa a computarse como `cantidad de ventas del día × gasto variable`. Dicho gasto variable también es configurable.
  7. 🤑 Se desea poder saber la ganancia diaria de una sucursal, es decir, la diferencia entre las ventas del día y su gasto del día. Este comportamiento debe funcionar para los dos tipos de sucursales.
  8. 📛 Además de poder actualizar precios según (alguna de las) categorías del producto, se desea contar con una funcionalidad similar, pero que aplique los cambios a los productos cuyo nombre coincide con una [expresión regular](https://flbulgarelli.github.io/recursos-python/1_introduccion_a_la_programacion/16_expresiones_regulares/).
      1. Incorporar los métodos y/o clases necesarios para soportar este requerimiento.
      2. Responder: ¿puede este requerimiento ser resuelto sin repetir lógica y posibilitando agregar más formas de búsqueda en el futuro? ¿Cómo?
  9. 💡 Una vez resueltos los puntos anteriores, responder: ¿hay otros cambios que podríamos realizar a nuestra solución original desde los puntos de vista del encapsulamiento y la delegación?

Al terminar, asegurate de que todo el código esté adecuadamente subido a Github y realizá un tag.

Tené en cuenta que:

  1. Las nuevas funcionalidades deben ser realizadas bajo el paradigma de objetos.
  2. No es necesario convertir todo el código existente al paradigma de objetos, aunque probablemente te convenga hacerlo al menos de forma parcial, para hacer más fácil el desarrollo de los nuevos requerimientos de esta entrega. Este cambio del diseño de la solución para favorecer la _extensibilidad_, pero preservando su _funcionalidad_ es lo que se conoce como _refactor_.
  3. Todos los tests existentes tienen que seguir andando, aunque puede que sea necesario modificarlos ligeramente para adaptarse a los _refactors_
  4. Para probar las nuevas funcionalidades será necesario incorporar nuevas pruebas automatizadas con `pytest`.

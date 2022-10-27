# MacoWins - Entrega 4

¡Se agregan nuevos requerimientos!

1. Se agregan tres nuevos criterio de actualización de precios:
  1. 💰 Por precio: queremos poder actualizar a cualquier prenda que tenga un valor menor a una cierta cantidad de dinero
  2. #️⃣ Por stock: queremos poder actualizar a cualquier prenda para la que haya stock
  3. 🙅‍♀️ Por oposición: queremos poder actualizar a cualquier prenda que NO cumpla alguno de los criterios anteriores. Por ejemplo, nos gustaría poder actualizar las prendas para las que no haya stock o que no tengan un cierto nombre. ¿Podemos resolverlo sin repetir lógica?

2. 🔍 Queremos poder _listar_ (es decir, obtener una lista con) todos los productos que cumplan cualquiera de los criterios anteriores (por nombre, por categoría, por precio, etc)

3. 👋 Queremos poder `discontinuar` los productos que correspondan de forma automática una vez por semana.

4. 📈 Bonus: queremos **una vez por día** escribir en un archivo `reporte.csv` una línea con la fecha de hoy, la cantidad de ventas del día y el monto total de dichas ventas, separado por comas. Para esto punto, recomendamos leer [una introducción al manejo de archivos](https://github.com/AJVelezRueda/Fundamentos_de_informatica/blob/master/Python_intro/Manipulaci%C3%B3n_de_archivos.md)

🧪 Nota: todos los requerimientos del punto 1 y 2 tienen que estar adecuadamente probados con `pytest`.

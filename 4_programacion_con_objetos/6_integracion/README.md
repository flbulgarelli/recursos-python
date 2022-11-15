# MacoWins - Entrega 4B

¡MacoWins se sumó a la fiebre por las tarjetas 💳! Desde ahora, cuando se compre un producto, MacoWins ofrecerá 3 medios de pago diferentes:

  1. Efectivo: al usar este medio, el precio de la venta es de lista
  2. Tarjeta de crédito: aplica un 10% de recargo al precio de la prenda
  3. Tarjeta MacoWins: aplica un 10% de descuento sobre los productos de la marca Macowins.

Además, la tarjeta MacoWins tiene un sistema de puntos y medallas: cada vez que alguien compra con una tarjeta MacoWins, la misma incrementa 1 punto. A medida que se van sumando puntos pasan cosas:

  * 🥉 Cuando **suma** 5 puntos pasa a nivel bronce (que da descuentos del 15%)
  * 🥈 Cuando luego suma otros 10 pasa a nivel plata (que da descuentos del 20%)
  * 🥇 Cuando luego suma otros 30 puntos pasa a nivel oro (que da 25%, pero hasta 3 mil pesos de descuento máximo).

📆 Cada primero de mes todas las tarjetas son bajadas de medalla: si tu tarjeta estaba en oro pasa a plata, si estaba en plata pasa a bronce y si estaba en bronce vuelve a no tener medalla (de 10% de descuento). Aunque aún no se usarán para generar descuentos, **los puntos de la tarjeta deben quedar intactos**. Este es un ejemplo de situación:

 1. Tu tarjeta está inicialmente en cero y sin medallas
 2. Realizás 5 compras y pasás a bronce. Tenés 5 puntos totales
 3. Realizás 10 compras más y pasas a plata. Tenés 15 puntos totales
 4. Realizás 2 compras más y seguís en plata. Tenés 17 puntos totales
 5. Inicia el nuevo mes: pasás a bronce nuevamente pero tus puntos totales siguen siendo 17.
 6. Realizás 10 comprás mas y volvés a plata. Tenés 27 puntos totales

Se pide:

1. Agregar a los productos la información de si son de la marca MacoWins.
2. Incorporar los tres medios de pago antes mencionados.
3. Hacer que las tarjetas ganen puntos, ganen medallas y cambien su cálculo de descuento.
4. Poder saber con qué medio de pago se realizó una venta.
5. Hacer que automáticamente cada mes las tarjetas sean bajadas de medalla.

🧪 Notas:

 1. Todos los requerimientos 1, 2, 3 y 4 tienen que estar adecuadamente probados con `pytest`. Todos los mismos deben estar en verde ✅.
 2. Para el punto 3 se requiere integración con el módulo de [`persistencia`](https://gist.github.com/flbulgarelli/3b34f870783cba3d88c996da6acf773c).
 3. Cada uno de los requerimientos debe ser integrado al proyecto usando Git, en múltiples commits con nombres representativos.

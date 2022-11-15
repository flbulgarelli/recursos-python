# MacoWins - Entrega 4B

¡MacoWins se sumó a la fiebre por las tarjetas 💳! Desde ahora, cuando se compre un producto, MacoWins ofrecerá 3 medios de pago diferentes:

  1. Efectivo: al usar este medio, el precio de la venta es de lista
  2. Tarjeta de crédito: aplica un 10% de recargo al precio de la prenda
  3. Tarjeta MacoWins: aplica un 10% de descuento sobre los productos de la marca Macowins.

Además, la tarjeta MacoWins tiene un sistema de puntos y medallas: cada vez que alguien compra con una tarjeta MacoWins, la misma incrementa 1 punto. A medida que se van sumando puntos pasan cosas:

  * 🥉 Cuando suma 5 puntos pasa a nivel bronce (que da descuentos del 15%)
  * 🥈 Cuando luego suma otros 10 pasa a nivel plata (que da descuentos del 20%)
  * 🥇 Cuando luego suma otros 30 puntos pasa a nivel oro (que da 25%, pero hasta 3 mil pesos de descuento máximo).

📆 Cada primero de mes todas las tarjetas son bajadas de medalla: si tu tarjeta estaba en oro pasa a plata, si estaba en plata pasa a bronce y si estaba en bronce vuelve a no tener medalla (de 10% de descuento). **Tus puntos quedan intactos**.

Se pide:

1. Agregar a los productos la información de si son de la marca MacoWins.
2. Incorporar los tres medios de pago antes mencionados.
3. Hacer que las tarjetas ganen puntos, ganen medallas y cambien su cálculo de descuento.
4. Poder saber con qué medio de pago se realizó una venta.
5. Hacer que automáticamente cada mes las tarjetas sean bajadas de medalla.

🧪 Notas:

 1. Todos los requerimientos 1, 2, 3 y 4 tienen que estar adecuadamente probados con `pytest`. Todos los mismos deben estar en verde ✅.
 2. Para el punto 3 se requiere integración con el módulo de `persistencia`.
 3. Cada uno de los requerimientos debe ser integrado al proyecto usando Git, en múltiples commits con nombres representativos.

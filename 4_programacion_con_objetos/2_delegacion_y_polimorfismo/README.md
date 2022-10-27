Delegación y Polimorfismo
=========================


## Sueldo de Pepe


> Ejercicio basado en [El sueldo de Pepe](https://docs.google.com/document/d/1DQNuJwO3m6o_0-31tld94eJKJSQQ2TsjqBBY_rOVho4/edit)

Desarrollar los objetos necesarios para calcular el sueldo de Pepe. El sueldo de pepe se calcula así:

```
sueldo = sueldo base + bono x presentismo + bono x resultados.
```

El sueldo base es el de la categoría, hay dos categorías:
  * gerentes que ganan $1000 de sueldo base,
  * cadetes que ganan $1500.

Hay dos bonos por presentismo:
  * Es $100 si la persona a quien se aplica no faltó nunca, $50 si faltó un día, $0 en cualquier otro caso;
  * En el otro, nada.

Hay tres posibilidades para el bono por resultados:
  * Un porcentaje sobre el sueldo base
  * Un valor fijo
  * O nada

Probar cambiándole a pepe la categoría, la cantidad de días que falta y haciendo que cumpla sus objetivos. Probar también cambiar sus bonos por presentismo y por resultados, o con nosotros empelados con diferente categoría y bonos. En cada caso preguntarle su sueldo.


```python
>>>
>>> dani.faltar()
>>> dani.faltas
1
>>> dani.sueldo_total()
1050
>>> dani.faltar()
>>> dani.faltar()
>>> dani.faltar()
>>> dani.sueldo_total()
1000
>>>
>>> umi.sueldo_total()
1500
>>> umi.cumplir_objetivos()
>>> umi.sueldo_total()
1725.0
>>> umi.bono_resultados = BonoFijoPorResultados(80)
>>> umi.sueldo_total()
1580
>>>
```


## Trenes y depósitos


Una administradora ferroviaria necesita una aplicación que le ayude a manejar las formaciones que tiene disponibles en distintos depósitos.
Una formación es lo que habitualmente llamamos “un tren”, tiene una o varias locomotoras, y uno o varios vagones. Hay vagones de pasajeros y vagones de carga.
En cada depósito hay: formaciones ya armadas, y locomotoras sueltas que pueden ser agregadas a una formación.

De cada vagón de pasajeros se conoce el largo en metros, y el ancho útil también en metros. La cantidad de pasajeros que puede transportar un vagón de pasajeros es:
Si el ancho útil es de hasta 2.5 metros: metros de largo * 8.
Si el ancho útil es de más de 2.5 metros: metros de largo * 10.
P.ej., si tenemos dos vagones de pasajeros, los dos de 10 metros de largo, uno de 2 metros de ancho útil, y otro de 3 metros de ancho útil, entonces el primero puede llevar 80 pasajeros, y el segundo puede llevar 100.
Un vagón de pasajeros no puede llevar carga.

De cada vagón de carga se conoce la carga máxima que puede llevar, en kilos. Un vagón de carga no puede llevar ningún pasajero.
No hay vagones mixtos.

El peso máximo de un vagón, medido en kilos, se calcula así:
Para un vagón de pasajeros: cantidad de pasajeros que puede llevar * 80.
Para un vagón de carga: la carga máxima que puede llevar + 160 (en cada vagón de carga van dos guardas).

De cada locomotora se sabe: su peso, el peso máximo que puede arrastrar, y su velocidad máxima. P.ej. puedo tener una locomotora que pesa 1000 kg, puede arrastrar hasta 12000 kg, y su velocidad máxima es de 80 km/h. Obviamente se tiene que arrastrar a ella misma, entonces no le puedo cargar 12000 kg de vagones, solamente 11000; diremos que este es su “arrastre útil”.

Modelar la situación descripta de acuerdo al paradigma de objetos, escribiendo el código en lenguaje Wollok, de manera de poder saber:
El total de pasajeros que puede transportar una formación.
Cuántos vagones livianos tiene una formación; un vagón es liviano si su peso máximo es menor a 2500 kg.
La velocidad máxima de una formación, que es el mínimo entre las velocidades máximas de las locomotoras.
Si una formación es eficiente; es eficiente si cada una de sus locomotoras arrastra, al menos, 5 veces su peso (el de la locomotora misma).
Si una formación puede moverse. Una formación puede moverse si el arrastre útil total de las locomotoras es mayor o igual al peso máximo total de los vagones.
Cuántos kilos de empuje le faltan a una formación para poder moverse, que es: 0 si ya se puede mover, y (peso máximo total de los vagones – arrastre útil total de las locomotoras) en caso contrario.
Dado un depósito, el conjunto formado por el vagón más pesado de cada formación; se espera un conjunto de vagones.
Si un depósito necesita un conductor experimentado.
Un depósito necesita un conductor experimentado si alguna de sus formaciones es compleja. Una formación es compleja si: tiene más de 20 unidades (sumando locomotoras y vagones), o el peso total (sumando locomotoras y vagones) es de más de 10000 kg.
Agregar, dentro de un depósito, una locomotora a una formación determinada, de forma tal que la formación pueda moverse.
Si la formación ya puede moverse, entonces no se hace nada.
Si no, se le agrega una locomotora suelta del depósito cuyo arrastre útil sea mayor o igual a los kilos de empuje que le faltan a la formación. Si no hay ninguna locomotora suelta que cumpla esta condición, no se hace nada.

O sea: indicar qué clases se necesitan, qué variables de instancia se necesitan en cada clase, qué mensajes van a entender las instancias de cada clase, y escribir los métodos correspondientes.
Para cada punto, indicar a qué objeto se le pide lo que se indica, con qué mensaje, qué parámetros, y qué devuelve.
Para el punto 8, indicar en qué otros objetos delega el responsable de hacer lo que se pide, y qué delega (indicar lo que se delega en castellano). Si hay una cadena de delegaciones (al objeto 1 le piden algo, entonces delega algo en el objeto 2, y el objeto 2 para hacer lo que le pidió el 1 tiene que delegar otra cosa en otro objeto 3) indicarla.

Ejercicio 2 – Mascota Virtual
Modelar una mascota virtual, onda Tamagotchi, incluyendo los mensajes correspondientes a las acciones de comer y jugar, y la pregunta acerca de si puede jugar o no.

También hay que poder conocer el nivel de contenta de una mascota, que es un número entero mayor o igual que 0, donde a mayor nivel, más contenta está la mascota.

Una mascota puede estar aburrida, hambrienta o contenta; y su comportamiento depende de en qué estado esté. Veamos:

Cuando una mascota come, pasa lo siguiente:
Si está hambrienta, se pone contenta.
Si está contenta, su nivel se incrementa en una unidad.
Si está aburrida, y hace más de 80 minutos que está aburrida, entonces se pone contenta.
Si está aburrida desde hace 80 minutos o menos, entonces no le pasa nada, no cambia nada.

Cuando una mascota juega, pasa lo siguiente:
Si está contenta, su nivel se incrementa en dos unidades.
Si está aburrida, se pone contenta.
No produce ningún efecto jugar con la mascota si está hambrienta.

Una mascota puede jugar si está contenta o aburrida, si está hambrienta no.

NO SE PUEDE CONSULTAR DE NINGUNA MANERA EL ESTADO ACTUAL DE LA MASCOTA.
Esto quiere decir que está prohibido hacer comparaciones del tipo estado == “contento” o cualquiera similar utilizando mensajes especiales.

Responder las siguientes preguntas:
Indique en palabras los pasos necesarios para incorporar un nuevo estado “Triste” en la mascota, de manera que quede listo para funcionar.
Indique cuál sería la prueba en un test similar para darles de comer a todas las mascotas que están dentro de una colección “mascotas”.
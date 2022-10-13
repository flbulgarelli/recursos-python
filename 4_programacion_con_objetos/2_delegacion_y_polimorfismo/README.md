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

> Este material se basa en [Clustering con Python by Joaquín Amat Rodrigo](https://www.cienciadedatos.net/documentos/py20-clustering-con-python.html) 

En este recorrido utilizaremos el set de datos [Iris](https://en.wikipedia.org/wiki/Iris_flower_data_set) que consiste en un conjunto de datos u observaciones realizadas por el biólogo Ronald Fisher, sobre las característica de distintas especies de plantas plantas.

# Guias de Trabajo
 * [1.Clustering ¿Qué es?](#1-Intro)
 * [2.Calculo de distancias](#2-distancia)
 * [3.K-means](#3-kmeans)
 * [4.Agrupamiento jerárquico](#4-agrupamiento)

[1.Clustering ¿Qué es?](#1-Intro)
Hemos estado trabajando hasta aquí en la carga y limpieza da datos con Pandas. Es momento de comenzar a trabajar con los datos, analizarlos y poder encontrar patrones que nos permitan derivar información. El aprendizaje automático consiste en identificar de patrones o tendencias que de los datos de forma automática.

> Para pensar 🤔: ¿Qué utilidad le encontrás al aprendizaje automatizado? ¿Qué aplicaciones se te ocurren o conoces?


<details>
  <summary>Recurso audiovisuales complementarios</summary>

[Inteligencia Artificial: ¿Amiga o Enemiga? | Diego Fernández Slezak](https://www.youtube.com/watch?v=znq3ql6wqnE)

[¿De qué es capaz la inteligencia artificial? | DW Documental](https://www.youtube.com/watch?v=34Kz-PP_X7c&t=146s)
</details>

En este recorrido nos centraremos particularmente en métodos que nos permitan describir la estructura u organización de nuestros datos. Los métodos de clustering(agrupamientos) nos permiten buscar patrones "ocultos" en los datos sin la necesidad de contar con la información sobre la verdadera clasificación (etiquetas) de los datos. Son métodos exploratorios que agrupan los datos según similitud para simplificar su análisis.

> Para pensar 🤔: ¿Qué tipo de simplificaciones permite el agrupamiento de datos?

Existen una amplia cantidad de técnicas que nos permiten encontrar patrones en los datos y agruparlas de algún modo, pero en todos los casos estos agrupamientos se establecen de forma que, las observaciones que están dentro de un mismo grupo, son similares entre ellas y distintas a las de otros grupos. Todos los métodos de clustering requieren de la definición y cuantificación de la similitud entre las observaciones. Es por ello que resulta necesario revisar el concepto de distancia, ya que es lo que se usa como medida de similitud o diferencia entre grupos.


[2.Calculo de distancias](#2-distancia)
Como hemos dicho, los métodos de clustering permiten la identificación de grupos en los que se pueden agrupar las observaciones de un conjunto de datos. Esto se hace de forma tal que las observaciones o registros asignados a un mismo grupo, muestren una mayor similitud entre sí que con los miembros de otros grupos.

Pero, ¿Cómo medimos similitud entre miembros de un grupo dado? 🤔

Una forma de obtener la similitud es asumir que los datos son puntos en el espacio, por lo que si se define la distancia ente los puntos y se mide la separación entre dos registros, podrá obtenerse la similitud entre estos. 

Una de las formas más básicas para calcular la distancia  entre dos puntos es la Euclídea, basada en el famoso [Teorema de Pitágoras](https://es.wikipedia.org/wiki/Teorema_de_Pit%C3%A1goras).. ¡Si, era importante Pitágoras!

![Distancia Euclidea](./dist_euclídea.gif)


¿Pero no todas las definiciones de distancia son aplicables a todos los tipos de datos no? ¡Claro que no!


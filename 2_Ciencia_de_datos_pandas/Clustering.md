> Este material se basa en [Clustering con Python by Joaquín Amat Rodrigo](https://www.cienciadedatos.net/documentos/py20-clustering-con-python.html) 

En este recorrido utilizaremos el set de datos [Iris](https://en.wikipedia.org/wiki/Iris_flower_data_set) que consiste en un conjunto de datos u observaciones realizadas por el biólogo Ronald Fisher, sobre las característica de distintas especies de plantas plantas.

# Guias de Trabajo
 * [1.Clustering ¿Qué es?](#1-Intro)
 * [2.Calculo de distancias](#2-distancia)
 * [3.K-means](#3-kmeans)
 * [4.Agrupamiento jerárquico](#4-agrupamiento)

[1.Clustering ¿Qué es?](#1-Intro)
Hemos estado trabajando hasta aquí en la carga y limpieza da datos con Pandas. Es momento de comenzar a trabajar con los datos, analizarlos y poder encontrar patrones que nos permitan derivar información. El aprendizaje automático consiste en identificar de patrones o tendencias que de los datos de forma automática.

En este recorrido nos centraremos particularmente en métodos que nos permitan describir la estructura u organización de nuestros datos. Los métodos de clustering(agrupamientos) nos permiten buscar patrones "ocultos" en los datos sin la necesidad de contar con la información sobre la verdadera clasificación (etiquetas) de los datos.  Son métodos exploratorios que simplifican el análisis de los datos.

Existen una amplia cantidad de técnicas que nos permiten encontrar patrones en los datos y agruparlas de algún modo, pero en todos los casos estos agrupamientos se establecen de forma que, las observaciones que están dentro de un mismo grupo, son similares entre ellas y distintas a las de otros grupos. Todos los métodos de clustering requieren de la definición y cuantificación de la similitud entre las observaciones. Es por ello que resulta necesario revisar el concepto de distancia, ya que es lo que se usa como medida de similitud o diferencia entre grupos.

[2.Calculo de distancias](#2-distancia)

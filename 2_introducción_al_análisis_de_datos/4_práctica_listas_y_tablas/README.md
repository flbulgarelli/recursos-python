## Ejercitacion de Complementarios

**Ejercicio 1**

Escribí una procedimiento de nombre _cursada_ que tome como parámetro el nombre de un una materia (por ejemplo:pensamiento computacional), un día de la semana y un horario los almacene en las correspondientes variables globales tipo listas _materias_, _dias_de_cursada_ y _horarios_de_cursada_


**Ejercicio 2**

Reescribí el procedimiento anterios para que almacene los datos de la cursada en una tabla cuyas columnas sean _materias_, _dias_de_cursada_ y _horarios_de_cursada_

<details>
  <summary>**Pistas**</summary>

```python
df = pd.DataFrame(columns=['materias', 'dias','horario'])
```

Nuestro procedimiento debría:

- paso 1: generar el df con las materias, dias, etc que vienen de parámetro 

- paso 2: es appendear al df global 
</details>


**Ejercicio 3**

Definí una función que almacene en una lista los números que se pasen por parámetro y retorne la lista en orden inverso

**Ejercicio 4**

1. Busquen en la página de [data.buenosaires.gob.ar](https://data.buenosaires.gob.ar) el dataset de puestos de bicicletas de CABA
2. Carguen en un dataframe dicho dataset
3. Averiguen cuántas bicicletas hay
4. Averiguen en cuántos barrios **diferentes** están estas bicicletas
5. Averiguen los nombres de estas bicicletas
6. Averiguen cuántas bibliotecas hay por barrio
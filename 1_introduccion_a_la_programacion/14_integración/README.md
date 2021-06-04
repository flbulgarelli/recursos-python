# Integración

## `anio`

Definí la función `anio` que dado un string con una fecha (como por ejemplo `"30/11/2014"`) devuelva el año, como **un número**. La función tiene que andar tanto con si el string original completa los dígitos con cero como si no lo hace.

Por ejemplo:

```python
>>> anio("30/11/2014")
2014
>>> anio("05/01/0152")
152
>>> anio("5/1/152")
152
```

## Estadísticas del curso

Tenemos datos de un curso como el siguiente:

```python
curso_ejemplo = [
  {
    'legajo': '123446',
    'nombre': 'María',
    'apellido': '(...)',
    'notas' : [10, 2, 3],
    'zona': 'Quilmes'
  },
  {
    'legajo': '123450',
    'nombre': 'Carlos',
    'apellido': '(...)',
    'notas' : [5, 8, 8],
    'zona': 'CABA'
  },
  {
    'legajo': '123430',
    'nombre': 'Liz',
    'apellido': '(...)',
    'notas' : [4, 8, 2],
    'zona': 'CABA'
  },
  {
    'legajo': '123453',
    'nombre': 'Hector',
    'apellido': '(...)',
    'notas' : [9, 9, 1],
    'zona': 'Temperley'
  },
  {
    'legajo': '123110',
    'nombre': 'Ana',
    'apellido': '(...)',
    'notas' : [6, 7, 8],
    'zona': 'Quilmes'
  },
  {
    'legajo': '123371',
    'nombre': 'Ivana',
    'apellido': '(...)',
    'notas' : [7, 7, 9],
    'zona': 'Avellaneda'
  }
]
```

Con esta información, definí funciones que calculen las siguientes estadísticas:

  * `nota_final(un_estudiante)`: devuelve la nota final de un estudiante, que se calcula como el promedio de sus notas
  * `promedio_de_notas_del_curso(un_curso)`: devuelve el promedio general de las notas finales del curso
  * `estudiantes_aprobados(un_curso)`: devuelve aquellos estudiantes cuyas notas individuales (sin importar la nota final) son todas mayores o iguales a 4.
  * `cantidad_de_estudiantes_por_zona(un_curso)`: devuelve un diccionario con la cantidad de estudiante que hay en cada zona
  * `legajos_de_estudiantes(un_curso)`: devuelve una lista con sólo los legajos
  * `nombre_completo_de(legajo, un_curso)`: busca un estudiante por legajo y devuelve su nombre completo, asumiendo que el legajo existe.
  * `legajo_registrado(legajo, un_curso)`: dice si existe un estudiante con el legajo dado
Ejemplos:

```python
>>> estudiantes_aprobados(curso_ejemplo)
[
  {
    'legajo': '123450',
    'nombre': 'Carlos',
    'apellido': '(...)',
    'notas' : [5, 8, 8],
    'zona': 'CABA'
  },
  {
    'legajo': '123110',
    'nombre': 'Ana',
    'apellido': '(...)',
    'notas' : [6, 7, 8],
    'zona': 'Quilmes'
  },
  {
    'legajo': '123371',
    'nombre': 'Ivana',
    'apellido': '(...)',
    'notas' : [7, 7, 9],
    'zona': 'Avellaneda'
  }
]
>>> cantidad_de_estudiantes_por_zona(curso_ejemplo)
{
  "Quilmes": 2,
  "CABA": 2,
  "Temperley": 1,
  "Avellaneda": 1
}
>>> legajos_de_estudiantes(curso_ejemplo)
['123446', '123450', '123430', '123453', '123110', '123371']
>>> nombre_completo_de('123446', curso_ejemplo)
"María (...)"
>>> legajo_registrado('89612', curso_ejemplo)
False # nadie tiene ese legajo
```

## Bonus

Creá un `DataFrame` en pandas con los datos de ejemplo ....

```python
estudiantes = pd.DataFrame(curso_ejemplo)
```

... y realizá un gráfico de barras donde se ve la cantidad de estudiantes por zona.
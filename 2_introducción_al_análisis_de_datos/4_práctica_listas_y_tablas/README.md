# Práctica listas y tablas

## 1. Registrando todo

> Escribí una procedimiento `registrar_cursada` que tome como parámetro el nombre de un una materia (por ejemplo _pensamiento computacional_), un día de la semana y un horario, y los almacene en las correspondientes variables globales `materias`, `dias_de_cursada` y `horarios_de_cursada`


## 2. Armando un calendario

> Reescribí el procedimiento anterior para que almacene los datos de la cursada en una tabla cuyas columnas sean `materias`, `dias_de_cursada` y `horarios_de_cursada`
>
> Para pensar 🤔: ¿Que nombre le darías a esta variable?

<details>
  <summary>**Pistas**</summary>

```python
una_tabla = pd.DataFrame(columns=['materias', 'dias','horario'])
```

Nuestro procedimiento debría:

- paso 1: generar el `una_tabla` con las materias, dias, etc que vienen de parámetro
- paso 2: es _appendear_ al `una_tabla` global
</details>

## 3. ¡Otra vez sopa!

> Escribí una función `materia_que_mas_se_repite` que no tome argumentos
> y retorne la materia de la tabla anterior que más se repite.
>
> Ejemplo:
>
> ```python
> >>> registrar_cursada("Matemática 1", "Lunes", 9)
> >>> registrar_cursada("Historia del arte", "Lunes", 11)
> >>> registrar_cursada("Pensamiento sistémico", "Martes", 10)
> >>> registrar_cursada("Pensamiento sistémico", "Jueves", 11)
> >>> materia_que_mas_se_repite()
> "Pensamiento sistémico"
> ```

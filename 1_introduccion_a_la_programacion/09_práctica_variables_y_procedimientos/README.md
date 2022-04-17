# Práctica variables y procedimientos

## 1. Alcancía

Vamos a ahorrar para un viaje post COVID 😷. Tenemos una alcancía comunitaria (nuestro _pozo_) y para decidir si podemos viajar, debemos corroborar que el pozo tenga plata.

> Definí una función `pozo_vacio`, que nos indique si el `pozo` está en 0. Ejemplo:
>
> ```python
> >>> pozo = 0
> >>> pozo_vacio()
> True
> >>> pozo = 100
> >>> pozo_vacio()
> False
> ```


## 2. ¿Ya llegamos al Chaltén?

Sabemos que para llegar al Chaltén necesitamos por persona 3000 pesos

> Hacé una función `cuanta_gente_viaja_al_chalten` que retorne, según el monto del `pozo`, la cantidad de personas que pueden viajar. ¡Tené en cuenta que media persona no puede viajar! 😛
>
> Ejemplo:
>
> ```python
> >>> pozo = 3000
> >>> cuanta_gente_viaja_al_chalten()
> 1
> >>> pozo = 1500
> >>> cuanta_gente_viaja_al_chalten()
> 0
> >>> pozo = 6000
> >>> cuanta_gente_viaja_al_chalten()
> 2
> >>> pozo = 6500
> >>> cuanta_gente_viaja_al_chalten()
> 2
> ```


## 3. Destino alternativo

¡A quién no le gusta tener opciones! Sabemos cuánto nos sale por persona el viaje al Chaltén y nos pasaron en la agencia de viaje los valores por persona a Tilcara ($3500 por persona) y Mendoza ($2500 por persona).

> Definí una función `hasta_donde_llegamos` que según la cantidad de personas que van a viajar, nos devuelva un string con el nombre de la ciudad a la que podemos llegar. Y si no nos alcanza, que nos recomiende seguir ahorrando:
>
> ```python
> >>> hasta_donde_llegamos(2)
> 'Tilcara'
> >>> hasta_donde_llegamos(5)
> 'Seguí ahorrando'
> ```

## 4. Hora de aportar

Pero para todo esto tenga sentido, hay que poner plata 🤑

> Definí un procedimiento llamada `aportar_al_pozo`, que tome como parámetro un aporte (monto de plata) y actualice el monto del `pozo`:
>
> ```python
> >>> pozo = 500
> >>> aportar_al_pozo(1000)
> >>> pozo
> 1500
> ```

## 5. Me quiero bajar

¿Pero qué pasa si alguien se quiere bajar? La agencia nos devuelve solo 500, sin importar el monto inicial (asumimos que las personas deben aportar inicialmente más de 500)

> Definí el procedimiento `darse_de_baja`, que descuenta del pozo 500

## 6. Tiempo de descuento

Por una nueva reglamentación, todos pozos de dinero que tengan más de $15000, deberán tributar un impuesto (llamado _I.V.G.: Impuesto a las Variables Globales_) del 1% si el pozo. Por la misma reglamentación, el valor máximo del impuesto será de $500.

> Definí:
>
>  * una **función** `calcular_monto_ivg`, que indique el valor del impuesto I.V.G. que el pozo debe pagar;
>  * un **procedimiento** `aplicar_ivg`, que descuente del `pozo` el valor del impuesto que corresponda.
>
> Ejemplos:
>
> ```python
> >>> pozo = 1000
> >>> calcular_monto_ivg()
> 0 # porque para tributar el monto debe ser de al menos $15000
> >>> pozo = 16000
> >>> calcular_monto_ivg()
> 160 # porque es un pozo de más de $15000, y debe tributar el 1%
> >>> pozo = 125000
> >>> calcular_monto_ivg()
> 500 # porque el valor máximo del impuesto es 500 (el 1% de 125000 hubiera sido $1250)
> >>> aplicar_ivg()
> >>> monto
> 124500 # porque le restó los $500 del impuesto
> ```

## 7. La tercera es la vencida

¡Otra nueva reglamentación! Después de algunas quejas contra el I.V.G. 😡, se determinó que ningún pozo deberá pagar el impuesto más de tres veces. En otras palabras, al aplicar el impuesto, sólo deberemos descontar del pozo su monto si se aplicó hasta 3 veces. Ejemplo:

```python
>>> monto = 100000
>>> aplicar_ivg() # primera aplicación
>>> monto
99500
>>> aplicar_ivg() # segunda aplicación
>>> monto
99000
>>> aplicar_ivg() # tercera aplicación
>>> monto
98500
>>> aplicar_ivg() # cuarta aplicación
>>> aplicar_ivg() # quinta aplicación
>>> aplicar_ivg() # etc
>>> aplicar_ivg() # etc
>>> monto
98500 # a partir de la cuarta aplicación ya no se descuenta más del pozo
```

> Modificá el procedimiento `aplicar_ivg` para que refleje estos cambios de reglamentación.
>
> 💡 Sugerencia: para poder hacer estos cambios en la aplicación del impuesto I.V.G., quizás te convenga agregar nuevas variables globales (_qué ironía 😜_).


## 8. El delegado/a
En la clase están votando al delagado que representará en el curso. Pero como esta es una clase de pensamiento computacional,vamos a crear un procedimiento escribir_delegado_a que escriba en la variable global delegado_a el nombre de la persona que tenga más votos:

```python
>>> escribir_delegado_a("Perla", 5, "Enzo", 2)
>>> print(delegado_a)
Perla 2022
```

## 9. Registro histórico
En la comisión E están creando el registro histórico de delegados/as del curso. Para ello quieren retomar modificar el código desarrollado en el punto anterior para obtener un procedimiento que les permita registrar los/las delegados/as del curso en cada año en la variable global delegados_por_anio

```python
>>> registrar_delegado_a("Sol", 2021)
>>> registrar_delegado_a("Perla", 2022)
>>> print(delegados_por_anio)
Sol 2021, Perla 2022
```
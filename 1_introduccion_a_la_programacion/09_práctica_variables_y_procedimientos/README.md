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

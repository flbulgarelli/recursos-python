# para obtener los valores de una columna,
# la sintaxis es tabla[nombre_de_columna]
florerias["TITULAR"]


# ojo con esta función, que se escribe como
# columna.head()
florerias["TITULAR"].head(5)

# de igual forma tenemos la función tail
florerias["TITULAR"].tail(5)

# por ejemplo, podemos combinar head y tail para obtener de la 10 a la 20
florerias["TITULAR"].head(20).tail(10)


florerias["Calle"].unique()

florerias["Calle"].value_counts()

# Ordená, ¡es una orden!

# sort_values también es una función infija
# tabla.sort_values(nombre_columna)
florerias.sort_values("COMUNA")

# Del derecho y del revés

florerias.sort_values("COMUNA", ascending=False)

# Índices

# otro uso de corchetes:
# la función iloc se usa de la siguiente forma:
# tabla.iloc[indice]
# con iloc podemos obtener una fila en base a su número (índice) de fila
# OJO: el número o indice de fila no necesariamente coincide con la posición de la fila en la tabla
florerias.iloc[4]

# No estás en posición de indicar

# TODO continuar con bicileterías
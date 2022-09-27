def aplicar_descuento_2x1(cantidad, precio_base):
  """
  Aplica el descuento 2 X 1 a un precio: los pares de productos los cobra a la mitad de precio
  """
  if cantidad % 2 == 0:
    return precio_base * cantidad / 2
  else:
    return precio_base * (1 + (cantidad - 1) / 2)
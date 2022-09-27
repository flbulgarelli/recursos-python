from descuento import *

def test_descuento_cuando_cantidad_es_cero():
  assert aplicar_descuento_2x1(0, 450) == 0
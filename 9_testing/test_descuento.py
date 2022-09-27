from descuento import *

def test_descuento_cuando_cantidad_es_cero():
  assert aplicar_descuento_2x1(0, 450) == 0

def test_el_precio_es_100_cuando_cantidad_es_2_y_precio_es_100():
  assert aplicar_descuento_2x1(2, 100) == 100

def test_el_precio_es_200_cuando_la_cantidad_es_1_y_el_precio_base_es_200():
  assert aplicar_descuento_2x1(1, 200) == 200

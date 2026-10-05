import pytest
from desconto_original import calcular_desconto

@pytest.mark.parametrize("valor, tipo, esperado", [
    (99.99, "COMUM", 0.00),
    (100, "COMUM", 10.00),
    (499.99, "COMUM", 50.00),
    (500, "COMUM", 100.00),
    (300, "vip", 45.00),
    (1000, "VIP", 200.00),
])
def test_calcular_desconto(valor, tipo, esperado):
    assert calcular_desconto(valor, tipo) == pytest.approx(esperado)
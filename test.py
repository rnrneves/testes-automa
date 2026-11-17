from app import calcular_estoque

def test_calculo_estoque():
    assert calcular_estoque(10, 5) == 50

def test_estoque_zero():
    assert calcular_estoque(0, 5) == 0

def test_valor_negativo():
    try:
        calcular_estoque(-1, 5)
        assert False
    except ValueError:
        assert True
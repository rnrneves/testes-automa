def calcular_estoque(quantidade, preco):
    if quantidade < 0 or preco < 0:
        raise ValueError("Valores inválidos")

    return quantidade + preco

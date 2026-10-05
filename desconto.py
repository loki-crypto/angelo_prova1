def calcular_desconto (valor_compra, tipo_cliente):
    desconto = 0

    #calculo do esconto
    if valor_compra < 100:
        desconto = 0
    elif valor_compra >= 100 and valor_compra < 500:
        desconto = 0.10
    elif valor_compra >= 500:
        desconto = 0.20

    #calculando exclusao de VIP

    if tipo_cliente.upper() == "VIP":
        desconto += 0.05

    #definindo valor desconto

    valor_desconto = valor_compra * desconto

    #regra de teto de desconto

    if valor_desconto > 200:
        valor_desconto = 200

    return round (valor_desconto, 2)
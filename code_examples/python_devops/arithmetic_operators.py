nome_estabelecimento = "Pastelaria Devops"
pastel1 = "Carne"
pastel2 = "Queijo"
pastel3 = "Frango"
pastel4 = "Calabresa"

status = True

valor_pastel1 = 6.0
valor_pastel2 = 6.0
valor_pastel3 = 20
valor_pastel4 = 6

print (nome_estabelecimento)

print (pastel1,valor_pastel1, status)
print (pastel2,valor_pastel2, status)
print (pastel3,valor_pastel3, status)
print (pastel4,valor_pastel4, status)

# Addition

pedido_1 = valor_pastel1 + valor_pastel2
print("Valor igual a:", pedido_1)

pedido_2= valor_pastel1 + valor_pastel3
print("Valor igual a:", pedido_2)

# Substraction

custo = 3.0

subtracao1 = pedido_1 - custo
print ('Subtraction:', subtracao1)

# Division

ticket_medio= (pedido_1 + pedido_2)/2
print (ticket_medio)

# Multiplication

dias_mes = 22
faturamento = ticket_medio * 22
print ('Previsão de faturamento:', faturamento)

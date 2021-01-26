print ('Seja bem vindo')
print ('Faça seu pedido')
# item_pedido = input ('Faça seu pedido, qual sabor de sorvete você deseja?')
# print (f'O sabor pedido foi {item_pedido} - {type(item_pedido)}')

# valor = float(input('O valor é R$ 6.50, digite o valor de pagamento: '))
# print (f'O tipo de dado em troco é {type(valor)}')

'''
0 - Estabelecimento fechado
1 - Estabelecimento aberto
'''

item_pedido = []
count = 0
status = 1

# while status == 1:
#     item_pedido.append(input('Qual sabor do seu pedido?:'))
#     print ('Pedido confirmado')
#     status = int(input('Digite 1 para novo pedido, e 0 para encerrar: '))

quantidade_de_pedidos = int(input('Quantos pedidos deseja realizar'))
print (quantidade_de_pedidos)
while count < quantidade_de_pedidos:
    item_pedido.append(input('Qual sabor do seu pedido?:'))
    print ('Pedido confirmado')
    count += 1

print (f'Seus pedidos são: {item_pedido}')

cardapio = ['Carne','Queijo', 'Frango', 'Calabresa']

print (cardapio)

print (f'Tamanho da lista: {len(cardapio)}')

print (f'Tipo da variável: {type(cardapio)}')

print (f'Acessando primeiro item da lista {cardapio[0]}')

print (f'Acessando segundo item da lista {cardapio[1]}')

print (f'Acessando o ultimo item da lista {cardapio[-1]}')

print ('')
print ('---')
print ('')

print ('Mudando elementos:\n')

cardapio[1] = 'Mussarela'

print (cardapio)

print ('')
print ('---')
print ('')

print ('Append:\n')

novo_cardapio = []

novo_cardapio.append('Carne')
novo_cardapio.append('Queijo')
novo_cardapio.append('Napolitano')
novo_cardapio.append('Frango')
novo_cardapio.append('Palmito')
novo_cardapio.append('Calabresa')

print (novo_cardapio)

print ('')
print ('---')
print ('')

print ('Slicing:\n')

print (novo_cardapio[1:3])
print (novo_cardapio[2:])
print (novo_cardapio[:2])
print (novo_cardapio[:-2])
print (novo_cardapio[-2:])

print ('')
print ('---')
print ('')

print ('Sorting:\n')

print (novo_cardapio)
print (sorted(novo_cardapio, key=str.lower))

print ('')
print ('---')
print ('')

print ('Removendo e adicionando elementos:\n')

novo_cardapio.remove('Calabresa')

print (novo_cardapio)

novo_cardapio.insert(2,'Palmito')
novo_cardapio.insert(3,'Pizza')

print (novo_cardapio)

print(novo_cardapio.pop())
print (novo_cardapio)


print(novo_cardapio.pop(3))
print (novo_cardapio)

print ('')
print ('---')
print ('')

vendas = []

vendas.append(12.0)
vendas.append(16.3)
vendas.append(24.0)

print (vendas)

print (sum(vendas))
print (max(vendas))
print (min(vendas))

print (f'A media e: {sum(vendas)/len(vendas):.2f}')

print ('')
print ('---')
print ('')

numeros = list(range(1,101))

print (numeros)
print (len(numeros))

del numeros[:10]

print (numeros)

print (numeros[0:10])

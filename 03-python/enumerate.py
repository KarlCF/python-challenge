# Sourced from for.py

cardapio = ['Carne', 'Queijo', 'Frango', 'Calabresa', 'Pizza', 'Carne Seca']


'''

Code was originally simpler, but decided to try a proper interaction with the "client"

'''

print ('')
print ('---')
print ('')

for item, item2 in enumerate(cardapio):
    print (f'[{item}]: {item2}')
    
count = 0

while count == 0:
    opcao = input('Digite o numero de seu pedido')
    try:
        opcao = int(opcao)
    except:
        print ('Insira um número')
        continue
    
    if opcao > (len(cardapio) - 1):
        print ('Número alto demais')
        continue
    
    count += 1


print (f'Opção escolhida: {cardapio[opcao]}')

# print (list(enumerate(cardapio)))

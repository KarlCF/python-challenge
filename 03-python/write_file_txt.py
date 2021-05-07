clientes = ['Jose', 'Carlos', 'Lucas', 'Pedro', 'Paulo', 'Jackson', 'Gustavo', 'Joaquin']

file = open ('clientes.txt', 'w')
# file = open ('clientes.txt', 'a')

for cliente in clientes:
    print (f'Cliente {cliente} adicionado à lista')
    file.write(f'{cliente}\n')

file.close()

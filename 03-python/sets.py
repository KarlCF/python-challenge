pedidos_dia1 = [
    {'cliente': 'Jose', 'pastel': 'Queijo'},
    {'cliente': 'Jose', 'pastel': 'Queijo'},
    {'cliente': 'Pedro', 'pastel': 'Carne'},
    {'cliente': 'Lucas', 'pastel': 'Queijo'},
    {'cliente': 'Carlos', 'pastel': 'Frango'},
]

pedidos_dia2 = [
    {'cliente': 'Marcos', 'pastel': 'Pizza'},
    {'cliente': 'Daniel', 'pastel': 'Queijo'},
    {'cliente': 'Pedro', 'pastel': 'Carne'},
    {'cliente': 'Lucas', 'pastel': 'Queijo'},
    {'cliente': 'Joaquin', 'pastel': 'Frango'},
]

clientes_dia1 = set()
print (type(clientes_dia1))

print ('')
print ('---')
print ('')

for pedido in pedidos_dia1:
    clientes_dia1.add(pedido['cliente'])

print (f'Dia 1:{clientes_dia1}')

clientes_dia2 = set()

for pedido in pedidos_dia2:
    clientes_dia2.add(pedido['cliente'])

print (f'Dia 2:{clientes_dia2}')

print ('')
print ('---')
print ('')

print ('Joining sets')

todos_clientes = clientes_dia1 | clientes_dia2

print(todos_clientes)

print ('')
print ('---')
print ('')

print ('Intersection')

clientes_todos_dias = clientes_dia1.intersection(clientes_dia2)

print (f'Clientes de todos os dias: {clientes_todos_dias}')

print ('')
print ('---')
print ('')

print ('Difference from sets')

clientes_diff = clientes_dia1 - clientes_dia2
print (clientes_diff)

clientes_diff2 = clientes_dia2 - clientes_dia1
print (clientes_diff2)

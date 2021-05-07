minha_tupla = ()

'''
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) 
'''

pastel1 = (
    'Queijo',
    6.00,
    True
    )

print (pastel1)

for info in pastel1:
    print (info)

sabor, valor, status = pastel1

print (sabor, valor, status)

print (type(sabor))
print (type(valor))
print (type(status))

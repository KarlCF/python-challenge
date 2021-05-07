cardapio = {}

pastel1 = {
    'sabor':'queijo',
    'valor':6.00,
    'status': True
    }

print (pastel1)

print (pastel1['sabor'])
print (pastel1['valor'])
print (pastel1['status'])

#     print (pastel1['quantidade']) # KeyError, key not found

pastel1['valor'] = 7.00
print (pastel1)

### METHODS ### 

if pastel1.get('quatnidade'):
    print (pastel1['quantidade'])
else:
    pastel1['quantidade'] = 10

print (pastel1)

keys = pastel1.keys()

for key in keys:
    print (key)

values = pastel1.values()

for value in values:
    print (value)
    
dict_items = pastel1.items()

for item in dict_items:
    print (item)

pastel1.pop('status')
print (pastel1)

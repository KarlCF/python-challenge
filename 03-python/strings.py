nome_estabelecimento = "Pastelaria Devops"
pastel1 = "Carne"
pastel2 = "Queijo"
pastel3 = "Frango"
pastel4 = "Calabresa"
pastel5 = "Carne com queijo"
pastel6 = " Carne com frango "

print ('')
print ('---')
print ('')

print ('Replacing characters')
print (pastel5.replace('queijo','frango'))
print (pastel5)

novo_sabor = pastel5.replace('queijo','frango')

print (novo_sabor)

print (pastel5.upper())
print (pastel5.lower())


print ('')
print ('---')
print ('')

print (pastel5.startswith('Carne'))
print (pastel5.startswith('Queijo'))
print (pastel5.endswith('queijo'))
print (pastel5.endswith('frango'))

print ('')
print ('---')
print ('')

print ('Pastel 6:', pastel6)
print ('Pastel 6:', pastel6.replace(' ','-'))

novo_pastel = pastel6.strip()
novo_pastel = novo_pastel.replace(' ','-')

print ('Novo pastel 6: ', novo_pastel)

novo_pastel = pastel6.lstrip()
novo_pastel = novo_pastel.replace(' ','-')

print ('Novo pastel 6: ', novo_pastel)

novo_pastel = pastel6.rstrip()
novo_pastel = novo_pastel.replace(' ','-')

print ('Novo pastel 6: ', novo_pastel)

print (' Função Length (LEN)')
print ('Caracteres em pastel 5', len(pastel5))


print ('')
print ('---')
print ('')

print ('Var slicing')
print (pastel1)
print (pastel1[0])
print (pastel1[-1])
print (pastel1[0:2])
print (pastel1[2:])
print (pastel1[-2:])
print (pastel1[:-1])

print ('')
print ('---')
print ('')

print ('Operador IN')

print ('carne' in pastel5)
print ('Carne' in pastel5)
print ('queijo' in pastel5)
print ('frango' in pastel5)

print ('')
print ('---')
print ('')

print ('Operador NOT IN')

print ('carne' not in pastel5)
print ('Carne' not in pastel5)
print ('queijo' not in pastel5)
print ('frango' not in pastel5)

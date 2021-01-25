nome_estabelecimento = "Pastelaria Devops"
pastel1 = "Carne"
pastel2 = "Queijo"
pastel3 = "Frango"
pastel4 = "Calabresa"

status = True

valor_pastel1 = 6.0
valor_pastel2 = 6.0
valor_pastel3 = 6
valor_pastel4 = 6

# print (nome_estabelecimento)

# print (pastel1,valor_pastel1, status)
# print (pastel2,valor_pastel2, status)
# print (pastel3,valor_pastel3, status)
# print (pastel4,valor_pastel4, status)

print ('Concatenation')

mensagem = "O nome do estabelecimento é " + nome_estabelecimento

print (mensagem)

print ('')
print ('---')
print ('')

print ('Interpolation')

print ('O nome do estabelecimento é %s' %nome_estabelecimento)

print ('O pastel de %s custa R$ %f' %(pastel1,valor_pastel1))
print ('O pastel de %s custa R$ %.2f' %(pastel1,valor_pastel1))
print ('O pastel de %s custa R$ %d' %(pastel1,valor_pastel1))
print ('O pastel de %s custa R$ %.3d' %(pastel1,valor_pastel1))

print ('')
print ('---')
print ('')

print ('format()')

print ('O nome do estabelecimento é {}'.format(nome_estabelecimento))

print ('O pastel de {} custa R$ {}'.format(pastel1, valor_pastel1))
print ('O pastel de {} custa R$ {:f}'.format(pastel1, valor_pastel1))
print ('O pastel de {} custa R$ {:.2f}'.format(pastel1, valor_pastel1))
print ('O pastel de {} custa R$ {}'.format(pastel3, valor_pastel3))
print ('O pastel de {} custa R$ {}'.format(pastel1, valor_pastel1))
print ('O pastel de {} custa R$ {:03}'.format(pastel3, valor_pastel3))

print ('')
print ('---')
print ('')

print ('f-string')

print (f'O nome do estabelecimento é {nome_estabelecimento}')

print (f'O pastel de {pastel1} custa R$ {valor_pastel1}')
print (f'O pastel de {pastel1} custa R$ {valor_pastel1:f}')
print (f'O pastel de {pastel1} custa R$ {valor_pastel1:.2f}')
print (f'O pastel de {pastel3} custa R$ {valor_pastel3:.3f}')
print (f'O pastel de {pastel1} custa R$ {valor_pastel1}')
print (f'O pastel de {pastel3} custa R$ {valor_pastel3:03}')

print ('')
print ('---')
print ('')

print ('END')
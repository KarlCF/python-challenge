# numeros = range (10)

numeros = range(1,200)

print (numeros)
print (type(numeros))
print (list(numeros))

numeros_impar = []
numeros_par = []

print ('')
print ('---')
print ('')

for numero in numeros:
    print (f'O valor atual é: {numero}')
    if numero % 2 == 0:
        numeros_par.append(numero)
    else:
        numeros_impar.append(numero)

print (f'Numeros pares: {numeros_par}')
print (f'Numeros impares: {numeros_impar}')

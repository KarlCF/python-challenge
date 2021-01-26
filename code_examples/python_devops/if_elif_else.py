'''
Sistema de calculo de IMC

O IMC é calculado dividindo o peso (em kg) pela altura ao quadrado (em metros)

IMC 	            Classificação 	  Obesidade (grau)
Menor que 18,5 	    Magreza 	        0
Entre 18,5 e 24,9 	Normal 	            0
Entre 25,0 e 29,9 	Sobrepeso 	        I
Entre 30,0 e 39,9 	Obesidade 	        II
Maior que 40,0 	    Obesidade Grave 	III
'''

altura = float(input('Digite sua altura (EX.: 1.75): '))
peso = float(input('Digite o seu peso(EX.: 80.5): '))

imc = peso / ( altura**2 ) 

** = operador de potencia

print (f'IMC igual a: {imc}')

# The form if-if-if tests all conditions, whereas the if-elif-else tests only as many as needed: if it finds one condition that is True, it stops and doesn't evaluate the rest. In other words: if-elif-else is used when the conditions are mutually exclusive.

if imc < 18.5:
    print ('Magreza')

elif (imc >= 18.5) and (imc <= 24.9) :
    print ('Normal')

elif imc >= 25.0 and imc <=29.9:
    print ('Sobrepeso')

elif imc >= 30.0 and imc <= 39.9:
    print ('Obesidade')

elif imc > 40.0:
    print ('Obesidade Grave')

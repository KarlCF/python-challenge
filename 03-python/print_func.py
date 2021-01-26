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

print (nome_estabelecimento, end='\n\n')

print ((pastel1),valor_pastel1, status, end='\n\n', sep='  ==>  ')
print ((pastel2),valor_pastel2, status, end='\n\n', sep=';')
print ((pastel3),valor_pastel3, status, end='\n\n', sep='\t')
print ((pastel4),valor_pastel4, status, end='\n\n', sep=';')

print (type(pastel1))

"""
print function
    Arguments:
        end= Defines what is on the end of the line of the print function, defaults to \n
        sep= Defines what is between each object being printed, defaults to ' '
"""
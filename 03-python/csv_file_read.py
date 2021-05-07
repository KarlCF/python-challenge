import csv

open_file = open('menu.csv','r')
file_csv = csv.reader(open_file, delimiter=';')

'''

for line in file_csv:
    print (line)
    print (line[0])
    print (line[1])
    print (line[2])
    print (type(line))

'''

for [sabor,valor,status] in file_csv:
    print (f'O pastel {sabor} custa {valor} e está {status}')

open_file.close()

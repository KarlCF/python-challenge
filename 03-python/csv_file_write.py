import csv

create_file = open('pedidos.csv', 'w', newline='', encoding='utf-8')
write = csv.writer(create_file, delimiter=';')

header = ['ID', 'Cliente', 'Valor total']

write.writerow(header)

pedido1 = ['01','Jose','24.00']
pedido2 = ['02','Carlos','30.00']
pedido3 = ['03','Daniel','50.00']
pedido4 = ['04','Pedro','33.00']

write.writerow(pedido1)
write.writerow(pedido2)
write.writerow(pedido3)
write.writerow(pedido4)

create_file.close()

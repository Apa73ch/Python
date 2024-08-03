#datos = [1,2,3,4,5]
#with open('datos.txt','w') as archivo:
#    for numero in datos:
#        archivo.write(str(numero)+'\n')

###Texto Plano
#datos_leidos=[]
#with open('datos.txt','r') as archivo:
#    for linea in archivo:
#        datos_leidos.append(int(linea))

#print(datos_leidos)

#import csv

#productos=[[1, 'arroz', 43.0],[2, 'habichuelas',70.0],[3, 'azúcar',40.0]]
#with open('productos.csv','w', newline='') as archivo:
#    escritor=csv.writer(archivo)
#    escritor.writerows(productos)

#productos_leidos=[]
#with open('productos.csv','r') as archivo:
#   for fila in lector:
#        productos_leidos.append([int(fila[0]),fila[1], float(fila[2])])

#print(productos_leidos)

import json

#clientes=[{'id':1, 'nombre':'Joshua Pérez', 'totalGastado':950650, 'descuento':0.05},
#          {'id':2, 'nombre':'Marino Rodríguez', 'totalGastado':100000, 'descuento':0.0},
#          {'id':3, 'nombre':'Pedro Tineo', 'totalGastado':2365894, 'descuento':0.15}]

#with open('clientes.json','w') as archivo:
#    json.dump(clientes, archivo, indent=4)

clientes_leidos=[]
with open('clientes.json', 'r') as archivo:
    clientes_leidos=json.load(archivo)

print(clientes_leidos)
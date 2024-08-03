import json
import os
#{'id':1, 'isbn':'ghkfdk3232jh3', 'nombre':'nombrelibro', 'cantidad':4}
libros=[]
id_sec=1

def menu(libros):
    opc=''
    while opc!='5':
        os.system("cls")
        print('''
            ---Menú---
            1. Insertar libro
            2. Listar libros
            3. Actualizar libro
            4. Eliminar libro  
            5. Salir
            ''')
        opc=input("Elige una de las opciones: ")
        if opc=='1':
            isbn=input("ISBN: ")
            nombre=input("Nombre: ")
            cantidad=int(input("Cantidad: "))
            insertar_libro(isbn, nombre, cantidad, libros)
            input("Presione ENTER para continuar")
        elif opc=='2':
            listar_libros(libros)
            input("Presione ENTER para continuar")
        elif opc=='3':
            print("Actualizando libro...\nSi no deseas actualizar un campo, déjalo vacío")
            id=input("ID: ")
            isbn=input("ISBN: ")
            nombre=input("Nombre: ")
            cantidad=input("Cantidad: ")
            result=actualizar_libro(id, isbn, nombre, cantidad, libros)
            if result==0:
                print("El libro no existe")
            else:
                print("Actualización exitosa")
            input("Presione ENTER para continuar")
        elif opc=='4':
            print("Eliminado libros")
            id=input("ID: ")
            result=eliminar_libro(id, libros)
            if result==0:
                print("El libro no existe")
            else:
                print("Eliminación exitosa")
            input("Presione ENTER para continuar")
        elif opc=='5':
            guardar_libros(libros)
            print("Adiós")

def insertar_libro(isbn, nombre, cantidad, libros):
    global id_sec
    id_sec+=1
    libros.append({'id': id_sec, 'isbn':isbn, 'nombre':nombre, 'cantidad':cantidad})
    guardar_libros(libros)

def listar_libros(libros):
    if len(libros)!=0:
        for libro in libros:
            print("----------------------------") 
            print("ID:", libro['id'])   
            print("ISBN:", libro['isbn'])
            print("Nombre:",libro['nombre'])
            print("Cantidad:",libro['cantidad'])
            print("----------------------------") 
    else:
        print("No hay libros aún")

def actualizar_libro(id, isbn, nombre, cantidad, libros):
    libro=buscar_libro(id, libros)
    if libro!=None:
        if isbn!="":
            libro['isbn']=isbn
        if nombre!="":
            libro['nombre']=nombre
        if cantidad!="":
            libro['cantidad']=int(cantidad)
        return 1 #Actualización exitosa
    else:
        return 0 #No existe el libro

def buscar_libro(id, libros):
    for libro in libros:
        if libro['id']==int(id):
            return libro
    return None

def eliminar_libro(id, libros):
    libro=buscar_libro(id, libros)
    if libro!=None:
        libros.remove(libro)
        return 1 #Eliminación exitosa
    else:
        return 0 #El libro no existe

def guardar_libros(libros):
    with open('libros.json','w') as archivo:
        json.dump(libros, archivo, indent=4)

with open('libros.json','r') as archivo:
    libros=json.load(archivo)
    id_sec=libros[len(libros)-1]['id']  
menu(libros)
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
    libros.append({'ID': id_sec, 'ISBN':isbn, 'Nombre':nombre, 'Cantidad':cantidad})
    guardar_libros(libros)

def listar_libros(libros):
    librostemp=libros[:]
    if len(libros)!=0:
        cabecera=list(libros[0].keys())
        imprimirTabla(librostemp, cabecera)
        #for libro in libros:
        #    print("----------------------------") 
        #    print("ID:", libro['ID'])   
        #    print("ISBN:", libro['ISBN'])
        #    print("Nombre:",libro['Nombre'])
        #    print("Cantidad:",libro['Cantidad'])
        #    print("----------------------------") 
    else:
        print("No hay libros aún")

def actualizar_libro(id, isbn, nombre, cantidad, libros):
    libro=buscar_libro(id, libros)
    if libro!=None:
        if isbn!="":
            libro['ISBN']=isbn
        if nombre!="":
            libro['Nombre']=nombre
        if cantidad!="":
            libro['Cantidad']=int(cantidad)
        return 1 #Actualización exitosa
    else:
        return 0 #No existe el libro

def buscar_libro(id, libros):
    for libro in libros:
        if libro['ID']==int(id):
            return libro
    return None

def eliminar_libro(id, libros):
    libro=buscar_libro(id, libros)
    if libro!=None:
        libros.remove(libro)
        return 1 #Eliminación exitosa
    else:
        return 0 #El libro no existe
    
def imprimirTabla(tabla, titulos):
    tabla.insert(0, titulos)
    tamax=[]
    i=0
    for fila in tabla:
        i+=1
        j=0
        for elemento in titulos:
            if i==1:
                tamax.append(len(str(elemento)))
            elif tamax[j]<len(str(fila[elemento])):
                tamax[j]=len(str(fila[elemento]))
            j+=1
    i=0
    for fila in tabla:
        j=0
        if i==0:
            for elemento in fila:
                print(f'{str(elemento):{tamax[j]}}', end=' ')
                j+=1
        else:
            for elemento in titulos:
                print(f'{fila[str(elemento)]:{tamax[j]}}', end=' ')
                j+=1
        print()
        i+=1

def guardar_libros(libros):
    with open('libros.json','w') as archivo:
        json.dump(libros, archivo, indent=4)

with open('libros.json','r', encoding='UTF-8') as archivo:
    libros=json.load(archivo)
    if len(libros)!=0:
        id_sec=libros[len(libros)-1]['ID']  
    else:
        id_sec=0
menu(libros)
with open('ejemplo.txt','r') as archivo:
    contenido=archivo.read()
    print(contenido)

with open('ejemplo2.txt', 'w') as archivo:
    archivo.write("Bienvenidos a Python")

with open('ejemplo2.txt', 'a') as archivo:
    archivo.write("\nEs un lenguaje amigable")
n=int(input("Ingresa un número: "))

contador_de_divisores=0
for i in range(1,n+1):
    if n%i==0:
        contador_de_divisores+=1

if contador_de_divisores==2:
    print("El número", n, "es un número primo")
else:
    print("El número", n, "no es un número primo")


n=int(input("Ingrese un número: "))

i=1
contador_de_divisores=0
while i<=n:
    if n%i==0:
        contador_de_divisores+=1
    i+=1

if contador_de_divisores==2:
    print("El número",n,"es primo")
else:
    print("El número",n,"no es primo")
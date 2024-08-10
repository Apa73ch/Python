numeros=[2,4,6,8,10,12]
cuadrados=map(lambda x:x**2, numeros)
print(list(cuadrados))

numeros2=[1,2,3,4,5,6,7,8,9,10,11]
numeros_impares=filter(lambda x:x%2!=0, numeros2)
print(list(numeros_impares))

nombres=["Manuel", "Pedro", "Randy", "Rigoberto", "Carlos"]
nombres_termina_o=filter(lambda nombre:nombre[-1].lower()=='o', nombres)
print(list(nombres_termina_o))

nombres_en_mayuscula=map(lambda nombre:nombre.upper(), nombres)
print(list(nombres_en_mayuscula))
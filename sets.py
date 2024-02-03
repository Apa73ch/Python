myset = {2,3,4,5,6}
myset2 = {1,2,7,8,9}

union=myset.union(myset2)
interseccion=myset.intersection(myset2)
diferencia1=myset.difference(myset2)
diferencia2=myset2.difference(myset)

print("La intersección de A y B es ", interseccion)
print("La unión de A y B es ",union)
print("La diferencia A-B es ",diferencia1)
print("La diferencia B-A es ",diferencia2)


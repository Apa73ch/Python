"""try:
    numero=int(input("Ingresa un número: "))
    division=10/numero
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
except ValueError:
    print("Error: Solo se admiten números")
else:
    print(f"División: {division}")
finally:
    print("Proceso terminado")"""

def verificar_edad(edad):
    if edad<18:
        raise ValueError("La edad debe ser mayor o igual a 18 años")
    return "Edad válida"
try:
    edad=int(input("Ingresa una edad: "))
    print(verificar_edad(edad))
except ValueError as error:
    print(error)


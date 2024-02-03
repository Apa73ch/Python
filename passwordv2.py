password="1823"
cant_intentos=3
pass_intento=input("Bienvenido Usuario\nIngresa tu contraseña: ")
while(pass_intento!=password and cant_intentos>1):
    cant_intentos-=1
    pass_intento=input("Tienes "+str(cant_intentos)+" intento disponibles. Ingresa la contraseña correcta: ")
if(pass_intento==password):
    print("Login exitoso")
else:
    print("Cantidad de intentos agotada")

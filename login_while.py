usuario="ITLA"
pwd="somositla"

usuario_intento=""
pwd_intento=""

while(usuario!=usuario_intento or pwd!=pwd_intento):
    print("Ingresa tus credenciales")
    usuario_intento=input("Usuario: ")
    pwd_intento=input("Contraseña: ")

    if usuario!=usuario_intento or pwd!=pwd_intento:
        print("Credenciales incorrectas. Intente de nuevo")

print("Login exitoso")
usuario=input("ingrese su usuario")
contraseña=input("ingrese su contraseña:")
if usuario == "admin" and contraseña == "1234":
    print("Cargando tu perfil")
else:
    print("Acceso denegado, Datos incorrectos")

a=int(input("Ingrese su edad:"))
b=input("Cuenta con carnet de socio vigente (si/no):")
if a > 14 and b== 'si':
    print ("puede ingresar a el gimnasio")
    
else :
    c=input("Cuenta con pase de invitado(si/no):")
    d=input("Ingresa con un socio activo?(si/no):")
    if c== 'si' or d == 'si':
        print ("puede ingresar al gimnasio")
    else :
        print ("No puede ingresar al gimnasio")

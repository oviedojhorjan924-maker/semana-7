a=int(input("Temperatura en grados Celsius:"))
if a < 0 :
    print("BAJO CERO: congelacion")
elif a>= 0 and a < 15 :
    print("FRIA")
elif a >= 15 and a < 25 :
    print("TEMPLADA: temperatura ideal")
elif a >= 25 and a <= 35 :
    print("CALIDA")
else :
    print("EXTREMADAMENTE CALIENTE")

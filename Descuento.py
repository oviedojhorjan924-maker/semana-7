a=input("Es estudiante? (si/no):")
b= int(input("Total de su compra en pesos:"))
if a == 'si' or b > 200000 :
    c = b* 0.15
    d = b - c
    print("Descuento aplicado del 15%!")
    print("Descuento:     $", c)
    print("Total a pagar: $", d)
else :
    print("Sin descuento. Total: $", b)

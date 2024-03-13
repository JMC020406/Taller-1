# Problema de los 3 numeros
a=float(input("ingrese el primer sumando: "))
b=float(input("ingrese el segundo sumando: "))
c=float(input("ingrese la comparacion del total: "))

if a+b < c:
    print("la suma de "+str(a)+" con "+str(b)+" es menor que "+str(c))

elif a+b > c:
    print("la suma de "+str(a)+" con "+str(b)+" es mayor que "+str(c))

else:
    print("la suma de "+str(a)+" con "+str(b)+" es igual que "+str(c))



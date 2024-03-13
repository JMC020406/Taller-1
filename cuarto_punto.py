# Leer dos números reales desde el usuario
numero1 = float(input("Ingrese el primer número real: "))
numero2 = float(input("Ingrese el segundo número real: "))

# Determinar si el primero es múltiplo del segundo
if numero2 != 0 and numero1 % numero2 == 0:
    print(numero1, "es múltiplo de", numero2)
else:
    print(numero1, "no es múltiplo de", numero2)

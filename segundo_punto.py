# Leer tres números reales desde el usuario
numero1 = float(input("Ingrese el primer número real: "))
numero2 = float(input("Ingrese el segundo número real: "))
numero3 = float(input("Ingrese el tercer número real: "))

# Determinar cuál es el mayor número
if numero1 > numero2 and numero1 > numero3:
    mayor = numero1
elif numero2 > numero1 and numero2 > numero3:
    mayor = numero2
else:
    mayor = numero3

# Mostrar el resultado
print("El mayor número es:", mayor)

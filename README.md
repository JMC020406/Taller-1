# Taller-1
## Los LegoCoders
![Los LegoCoders](https://github.com/JMC020406/Taller-1/assets/159207395/1a07492a-d8da-4634-bc80-309179f38158)
### Integrantes

-Jeyson Fernando Romero

-Bryan Felipe Jaime  

-Juan Manuel Coronell
 <br>

### 1. (Jeyson Fernando Romero Fajardo)

   <br>

   ![Captura de pantalla 2024-03-02 201335](https://github.com/JeysonRomero/Taller-1/assets/159095091/f65da960-04a9-4bcc-bdbc-145d676ac6f5)


   <br>

### 2.Realice un programa que lea tres números reales y determine cuál es el mayor.

<br>

```
# Leer tres números reales 
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


```

-El programa solicita al usuario que ingrese tres números reales guardandolos en la variable.

-Luego, determina cuál de los tres números es el mayor utilizando condiciones if, elif, y else.

-Finalmente, muestra el mayor número entre los tres ingresados por el usuario utilizando el codigo print("El mayor número es:", mayor)


### 3.Realice un programa que lea un número enteros y determine si es par o impar.

<br>

```
# Solicitar que ingrese un número entero
numero = int(input("Ingrese un número entero: "))

# Determinar si el número es par o impar
if numero % 2 == 0:
    print(numero, "es un número par.")
else:
    print(numero, "es un número impar.")

```

<br>

-El programa solicita al usuario que ingrese un número entero con La línea numero = int(input("Ingrese un número entero: "))

-Luego, determina si el número ingresado es par o impar utilizando la operación de módulo (%), Si el número dividido por 2 tiene un residuo de 0, significa que es par; de lo contrario, es impar.

-Finalmente, imprime un mensaje indicando si el número es par o impar,utilizando la instrucción print().

### 4.Realice un programa que lea dos números reales y determine si el primero es múltiplo del segundo.


<br>

```
# Leer dos números reales 
numero1 = float(input("Ingrese el primer número real: "))
numero2 = float(input("Ingrese el segundo número real: "))

# Determinar si el primero es múltiplo del segundo
if numero2 != 0 and numero1 % numero2 == 0:
    print(numero1, "es múltiplo de", numero2)
else:
    print(numero1, "no es múltiplo de", numero2)

```

<br>

-El programa solicita al usuario que ingrese dos números reales.

-Luego, verifica si el segundo número es distinto de cero (numero2 != 0) para evitar la división por cero.

-Si el segundo número es distinto de cero y el residuo de la división del primer número entre el segundo es igual a cero (numero1 % numero2 == 0), entonces el primer número es múltiplo del segundo.

-Si se cumple la condición anterior, el programa imprime un mensaje indicando que el primer número es múltiplo del segundo. De lo contrario, imprime un mensaje indicando lo contrario.

![image](https://github.com/JeysonRomero/Taller-1/assets/159095091/9355def5-c55b-4c6b-ad46-5ce4927bc237)

# Taller-1
## Los LegoCoders
![Los LegoCoders](https://github.com/JMC020406/Taller-1/assets/159207395/1a07492a-d8da-4634-bc80-309179f38158)

### Integrantes
Jeyson Fernando Romero    - Bryan Felipe Jaime    - Juan Manuel Coronell
 <br>

## Resultados del quiz
##### 1. Jeyson Fernando Romero Fajardo

   <br>

   ![Captura de pantalla 2024-03-02 201335](https://github.com/JeysonRomero/Taller-1/assets/159095091/f65da960-04a9-4bcc-bdbc-145d676ac6f5)

##### 2. Juan Manuel Corornell

   ![image](https://github.com/JMC020406/Taller-1/assets/159207395/48abc5bb-d5cd-4907-98ef-46913389955e)

   <br>


## 2.Realice un programa que lea tres números reales y determine cuál es el mayor.

<br>

```py
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


## 3.Realice un programa que lea un número enteros y determine si es par o impar.

<br>

```py
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

```py
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


### 5.Realice un programa que lea tres números reales y determine si la suma de los dos primeros es mayor, menor o igual que el tercer número.
```py
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
```
la solución a este problema fue primero definir las 3 variables numéricas reales que va a usar la computadora en su proceso de analisis. Una vez el emisor haya dado sus 3 valores para las variables se empezara el procedimiento de analisis, empezando por ver si la sumatoria de los dos primeros números es menor al tercer número, si no es así, entonces se analizara si la suma de los dos primeros números es mayor que el tercero, y si ninguna de las dos condiciones se cumple la computador devolvera la respuesta que la suma de los dos primeros es igual al tercer número. 

### 6. Escriba un programa que solicite al usuario una letra y determine si es una vocal o una consonante.
```py
# Problema de vocales y consonantes
letra=(input("ingrese una letra cualquiera: "))

if (ord(letra)) == 65:
    print("la letra "+str(letra)+" es una vocal")

elif (ord(letra)) == 69:
     print("la letra "+str(letra)+"  es una vocal")

elif (ord(letra)) == 73:
    print("la letra "+str(letra)+"  es una vocal")

elif (ord(letra)) == 79:
     print("la letra "+str(letra)+"  es una vocal")

elif (ord(letra)) == 85:
      print("la letra "+str(letra)+"  es una vocal")

elif (ord(letra)) == 97:
      print("la letra "+str(letra)+"  es una vocal")

elif (ord(letra)) == 101:
      print("la letra "+str(letra)+"  es una vocal")

elif (ord(letra)) == 105:
      print("la letra "+str(letra)+"  es una vocal")

elif (ord(letra)) == 111:
      print("la letra "+str(letra)+"  es una vocal")

elif (ord(letra)) == 117:
      print("la letra "+str(letra)+"  es una vocal")

else:
     print("la letra "+str(letra)+"  es una consonante")
```
Para este problema lo que se hizo fue hacer que existiera una variable la cual se pudiera determinar, luego se transforma esa variable con la palabra reservada ord() que nos pasa nuestra variable al código ASCII. Una vez se determina que valor tiene en el código ASCII, este se compara con todas las posibilidades que hay de vocales; incluyendo las variables de mayúsculas y minúsculas. Si en algunos de los condicionales es verdadero la computador escribira que "la letra elegida es una vocal", si no, la computadora devolvera la respuesta de "la letra elegida es una consonante".

### 7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones:

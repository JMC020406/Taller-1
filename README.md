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

##### 3. Bryan Felipe Jaime
   
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
```py
# variables
a=float(input("ingrese un numero: "))
b=float(input("ingrese otro numero: "))
c=float(input("ingrese otro numero mas: "))
d=float(input("ingrese otro numero: "))
e=float(input("ingrese el ultimo numero: "))
```
lo primero que hay que hacer es definir las variables que va a usar el programa.

#### 7.1 El promedio
```py
# Calcular el promedio
print("el promedio es: "+str((a+b+c+d+e)/5))
```
Para cálcular el promedio de 5 números lo que hay que hacer es sumar los valores de todos estas variables y dividirlas entre 5. Algo bastante simple.

#### 7.2 La mediana
```py
if a<=b and a<=c and a<=d and a<=e:
    if b<=c and b<=d and b<=e:
        if c<=d and c<=e:
            print(" la mediana es "+str(c))
        elif d<=c and d<=e:
            print("la mediana es "+str(d))
        else:
            print("la mediana es "+str(e))
    elif c<=b and c<=d and c<=e:
        if b<=d and b<=e:
            print("la mediana es "+str(b))
        elif d<=b and d<=e:
            print("la mediana es "+str(d))
        else:
            print("la mediana es "+str(e))
    elif d<=b and d<=c and d<=e:
        if b<=c and b<=e:
            print("la mediana es "+str(b))
        elif c<=b and c<=e:
            print("la mediana es "+str(c))
        else:
            print("la mediana es "+str(e))
    else:
        if b<=c and b<=d:
            print("la mediana es "+str(b))
        elif c<=b and c<=d:
            print("la mediana es "+str(c))
        else:
            print("la mediana es "+str(d))

elif b<=a and b<=c and b<=d and b<=e:
    if a<=c and a<=d and a<=e:
        if c<=d and c<=e:
            print(" la mediana es "+str(c))
        elif d<=c and d<=e:
            print("la mediana es "+str(d))
        else:
            print("la mediana es "+str(e))
    elif c<=a and c<=d and c<=e:
        if a<=d and a<=e:
            print("la mediana es "+str(a))
        elif d<=a and d<=e:
            print("la mediana es "+str(d))
        else:
            print("la mediana es "+str(e))
    elif d<=a and d<=c and d<=e:
        if a<=c and a<=e:
            print("la mediana es "+str(a))
        elif c<=a and c<=e:
            print("la mediana es "+str(c))
        else:
            print("la mediana es "+str(e))
    else:
        if a<=c and a<=d:
            print("la mediana es "+str(a))
        elif c<=a and c<=d:
            print("la mediana es "+str(c))
        else:
            print("la mediana es "+str(d))

elif c<=b and c<=a and c<=d and c<=e:
    if b<=a and b<=d and b<=e:
        if a<=d and a<=e:
            print(" la mediana es "+str(a))
        elif d<=a and d<=e:
            print("la mediana es "+str(d))
        else:
            print("la mediana es "+str(e))
    elif a<=b and a<=d and a<=e:
        if b<=d and b<=e:
            print("la mediana es "+str(b))
        elif d<=b and d<=e:
            print("la mediana es "+str(d))
        else:
            print("la mediana es "+str(e))
    elif d<=b and d<=a and d<=e:
        if b<=a and b<=e:
            print("la mediana es "+str(b))
        elif a<=b and a<=e:
            print("la mediana es "+str(a))
        else:
            print("la mediana es "+str(e))
    else:
        if b<=a and b<=d:
            print("la mediana es "+str(b))
        elif a<=b and a<=d:
            print("la mediana es "+str(a))
        else:
            print("la mediana es "+str(d))

elif d<=b and d<=c and d<=a and d<=e:
    if b<=c and b<=a and b<=e:
        if c<=a and c<=e:
            print(" la mediana es "+str(c))
        elif a<=c and a<=e:
            print("la mediana es "+str(a))
        else:
            print("la mediana es "+str(e))
    elif c<=b and c<=a and c<=e:
        if b<=a and b<=e:
            print("la mediana es "+str(b))
        elif a<=b and a<=e:
            print("la mediana es "+str(a))
        else:
            print("la mediana es "+str(e))
    elif a<=b and a<=c and a<=e:
        if b<=c and b<=e:
            print("la mediana es "+str(b))
        elif c<=b and c<=e:
            print("la mediana es "+str(c))
        else:
            print("la mediana es "+str(e))
    else:
        if b<=c and b<=a:
            print("la mediana es "+str(b))
        elif c<=b and c<=a:
            print("la mediana es "+str(c))
        else:
            print("la mediana es "+str(a))

else:
    if b<=c and b<=d and b<=a:
        if c<=d and c<=a:
            print(" la mediana es "+str(c))
        elif d<=c and d<=a:
            print("la mediana es "+str(d))
        else:
            print("la mediana es "+str(a))
    elif c<=b and c<=d and c<=a:
        if b<=d and b<=a:
            print("la mediana es "+str(b))
        elif d<=b and d<=a:
            print("la mediana es "+str(d))
        else:
            print("la mediana es "+str(a))
    elif d<=b and d<=c and d<=a:
        if b<=c and b<=a:
            print("la mediana es "+str(b))
        elif c<=b and c<=a:
            print("la mediana es "+str(c))
        else:
            print("la mediana es "+str(a))
    else:
        if b<=c and b<=d:
            print("la mediana es "+str(b))
        elif c<=b and c<=d:
            print("la mediana es "+str(c))
        else:
            print("la mediana es "+str(d))
```
Este código ya es un poco mas complejo ya que toca especificar todas las combinaciones que hay de que un número sea mayor que dos de la lista, y menor que los otros dos. Saliendo así un total de 55 convinaciones entre los 5 números para determinar la mediana.

#### 7.3 El promedio multiplicativo
```py
print("el promedio multiplicativo es: "+str((a*b*c*d*e)**(0.2)))
```
Similar al código de "El promedio" este en lo único que difiere es que en vez de sumar las variables hay que multiplicarlas y ese producto hay que aplicarle la raiz de 5, ya que son un total de 5 elementos.

#### 7.4 y 7.5 Organizar de manera ascendente y descente ( estos dos son muy largos asi que estaran únicamente en el Notebook de los puntos impares)
Para ordenar de mayor a menor y de menor a mayor hay que hacer largas cadenas de condicionales que comparen las variables. Lo que hicimos fue usar comparaciones de <= para ordenar de manera ascendente y el >= para el descendente.

#### 7.6 La potencia del mayor número elevado al menor número
```py
if a>= b and a>=c and a>=d and a>=e:
    if b<=c and b<=d and b<=e and b<=a:
        print("la potencia del numero mayor elevada al menor es: "+str(a**b))
    elif c<=b and c<=d and c<=e and c<=a:
        print("la potencia del numero mayor elevada al menor es: "+str(a**c))
    elif d<=b and d<=c and d<=e and d<=a:
        print("la potencia del numero mayor elevada al menor es: "+str(a**d))
    else:
        print("la potencia del numero mayor elevada al menor es: "+str(a**e))

elif b>a and b>c and b>d and b>e:
    if a<=c and a<=d and a<=e and a<=b:
        print("la potencia del numero mayor elevada al menor es: "+str(b**a))
    elif c<=a and c<=d and c<=e and c<=b:
        print("la potencia del numero mayor elevada al menor es: "+str(b**c))
    elif d<=a and d<=c and d<=e and d<=b:
        print("la potencia del numero mayor elevada al menor es: "+str(b**d))
    else:
        print("la potencia del numero mayor elevada al menor es: "+str(b**e))

elif c>a and c>b and c>d and c>e:
    if a<=b and a<=d and a<=e and a<=c:
        print("la potencia del numero mayor elevada al menor es: "+str(c**a))
    elif b<=a and b<=d and b<=e and b<=c:
        print("la potencia del numero mayor elevada al menor es: "+str(c**b))
    elif d<=a and d<=b and d<=e and d<=c:
        print("la potencia del numero mayor elevada al menor es: "+str(c**d))
    else:
        print("la potencia del numero mayor elevada al menor es: "+str(c**e))

elif d>a and d>b and d>c and d>e:
    if a<=b and a<=c and a<=e and a<=d:
        print("la potencia del numero mayor elevada al menor es: "+str(d**a))
    elif b<=a and b<=c and b<=e and b<=d:
        print("la potencia del numero mayor elevada al menor es: "+str(d**b))
    elif c<=a and c<=b and c<=e and c<=d:
        print("la potencia del numero mayor elevada al menor es: "+str(d**c))
    else:
        print("la potencia del numero mayor elevada al menor es: "+str(d**e))

else:
    if a<=b and a<=c and a<=d and a<=e:
        print("la potencia del numero mayor elevada al menor es: "+str(e**a))
    elif b<=a and b<=c and b<=d and b<=e:
        print("la potencia del numero mayor elevada al menor es: "+str(e**b))
    elif c<=a and c<=b and c<=d and c<=e:
        print("la potencia del numero mayor elevada al menor es: "+str(e**c))
    else:
        print("la potencia del numero mayor elevada al menor es: "+str(e**d))
```
En este caso para determinar cual es la base toca hacer una comparación de >= o solamente > y para determinar el exponente hay que hacer comparaciones de <=. El resto de las especificaciones es que hay que hacer un total de 20 combinaciones, cada letra, es decir 5, tiene 4 conbinaciones posibles.

#### 7.7 La raíz cúbica del menor número
```py
if a<= b and a<=c and a<=d and a<=e:
    print("la raiz cubica del menor numero es: "+str(a**(1/3)))
elif b<a and b<c and b<d and b<e:
    print("la raiz cubica del menor numero es: "+str(b**(1/3)))
elif c<a and c<b and c<d and c<e:
    print("la raiz cubica del menor numero es: "+str(c**(1/3)))
elif d<a and d<b and d<c and d<e:
    print("la raiz cubica del menor numero es: "+str(d**(1/3)))
else:
    print("la raiz cubica del menor numero es: "+str(e**(1/3)))
```
En este problema lo que hay que hacer es poner todas las posibilidades de que una variable sea el número menor en comparacion a otros 4, y luego seguir el sencillo paso de aplicarle la raíz cúbica a este.

### 8. 

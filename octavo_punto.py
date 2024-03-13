#Calcular el espectro electromagnetico en que se encuentra la onda ingresada
frecuencia= float(input("Ingrese los digitos de la frecuencia de una onda en Hz: "))
if  30*10**3 >= frecuencia:
    print("La frecuencia se encuentra en la parte del espectro electromagnetico de Muy Baja Frecuencia - Radio.")
elif 30*10**3 <= frecuencia < 650*10**3:
    print("La frecuencia se encuentra en la parte del espectro electromagnetico de Onda Larga - Radio.")
elif 650*10*3 <= frecuencia < 1.7*10**6:
    print("La frecuencia se encuentra en la parte del espectro electromagnetico de Onda Media - Radio.")
elif 1.7*10**6 <= frecuencia < 30*10**6:
    print("La frecuencia se encuentra en la parte del espectro electromagnetico Onda Corta - Radio.")
elif 30*10**6 <= frecuencia < 300*10**6:
    print("La frecuencia se encuentra en la parte del espectro electromagnetico Muy Alta Frecuencia - Radio.")
elif 300*10**6 <= frecuencia < 3*10**9:
    print("La frecuencia se encuentra en la parte del espectro electromagnetico Ultra Alta Frecuencia - Radio.")
elif 3*10**9 <= frecuencia < 300*10*9:
    print("La frecuencia se encuentra en la parte del espectro electromagnetico Microondas.")
elif 300*10**9 <= frecuencia < 6*10**12:
    print("La frecuencia se encuentra en la parte del espectro electromagnetico Infrarojo Lejano.")
elif 6*10**12 <= frecuencia < 120*10**12:
    print("La frecuencia se encuentra en la parte del espectro electromagnetico Infrarojo Medio.")
elif 120*10**12 <= frecuencia < 384*10**12:
    print("La frecuencia se encuentra en la parte del espectro electromagnetico Infrarrojo Cercano.")
elif 384*10**12 <= frecuencia < 7.89*10**14:
    print("La frecuencia se encuentra en la parte del espectro electromagnetico Visible.")
elif 7.89*10**14 <= frecuencia < 1.5*10**15:
    print("La frecuencia se encuentra en la parte del espectro electromagnetico Ultravioleta Cercano.")
elif 1.5*10**15 <= frecuencia < 30*10**15:
    print("La frecuencia se encuentra en la parte del espectro electromagnetico Ultravioleta Lejano.")
elif 30*10**15 <= frecuencia< 30*10**18:
    print("La frecuencia se encuentra en la parte del espectro electromagnetico de Rayos X.")
elif 30*10**18 <= frecuencia:
    print("La frecuencia se encuentra en la parte del espectro electromagnetico de Rayos Gamma.")


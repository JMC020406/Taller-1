#Dada una distancia calcular tiempo que tardaria en recorrerla distintas variables
distancia=float(input("Ingrese los digitos de una distancia en metros: "))
distancia_luz= distancia/299792458
distancia_sonido= distancia/343.2
distancia_carro= distancia/141.11
distancia_bolt= distancia/10.44
print("Tiempo que le tomaria a la luz en el vacio recorrer esa distancia es", distancia_luz, "segundos")
print("Tiempo que le tomaria a el sonido en el aire recorrer esa distancia es", distancia_sonido, "segundos")
print("Tiempo que le tomaria a el Shelby Tuatara, el carro comercial mas rapido del mundo recorrer esa distancia es", distancia_carro, "segundos")
print("Tiempo que le tomaria a Usain Bolt recorrer esa distancia es de", distancia_bolt, "segundos")
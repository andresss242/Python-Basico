#Calcular el area de un terreno
#solicitar al usuario que ingrese la base del terreno triangular
base = float(input("ingrese la base del terreno en metro: "))

#solicitar al usuario que ingrese la "altura" del terreno triangular
altura = float(input("ingrese la altura del terreno: "))

#calculamos el area 
area = (base * altura) / 2
print(f"el area del terreno es de:{area} metros cuadrados.")
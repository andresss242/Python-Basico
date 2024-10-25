#estructura de repeticion
#for i in range(5):
 #   print(f"su dato es:{i} ")

#for i in range(0,5):#inicion, fin -1
 #   print(f"su dato es:{i} ")
#for i in range(1,10,2):#inicio, fin -1 incremento 
  #  print(f"su dato es:{i} ")

#for letra in "python":
 #   print(f"su dato es:{letra} ")

#ejemplo
cadena = "Programacion"
for letra in cadena:
    if letra == "r":
        print("se encontro una r")
        break
    else:
        print("letra no encontrada ")
print("esta por fuera del ciclo for")

#tabla del 2
for i in range(1, 13):
    for j in range(1, 13):
        print(f"{i} x {j} = {i * j}")
    print()  # Imprime una línea en blanco para separar las tablas



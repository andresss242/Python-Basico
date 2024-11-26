import random

def generar_matriz(n, m, min_temp=0, max_temp=100):
    """
    Genera una matriz de tamaño x con valores aleatorios 
    entre temperatura minima y maxima
    """
    matriz = [[random.randint(min_temp, max_temp) for _ in range(m)] for _ in range(n)]
    return matriz

def detectar_valores_criticos(matriz, umbral_critico=80):
    """
    Recorre la matriz y detecta valores mayores al umbral crítico
    Devuelve una lista con las ubicaciones y valores críticos
    """
    valores_criticos = []
    for i in range(len(matriz)):  
        for j in range(len(matriz[i])):  
            if matriz[i][j] > umbral_critico:
                valores_criticos.append((i, j, matriz[i][j])) 
    return valores_criticos

def mostrar_matriz(matriz):
    """
    Muestra la matriz en un formato legible
    """
    print("\nMatriz de sensores(temperaturas):")
    for fila in matriz:
        print(fila)

def menu_interactivo():
    """
    Menú para interactuar con el usuario
    """
    print("Bienvenido al sistema de monitoreo de sensores")
    while True:
        print("\nMenu")
        print("1. Generar una nueva matriz")
        print("2. Detectar valores críticos")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            try:
                n = int(input("Ingrese el número de filas de la matriz: "))
                m = int(input("Ingrese el número de columnas de la matriz: "))
                min_temp = int(input("Ingrese la temperatura mínima: "))
                max_temp = int(input("Ingrese la temperatura máxima: "))
                
                global matriz_sensores
                matriz_sensores = generar_matriz(n, m, min_temp, max_temp)
                mostrar_matriz(matriz_sensores)
            except ValueError:
                print("Por favor, ingrese valores numéricos válidos.")
        
        elif opcion == "2":
            try:
                if 'matriz_sensores' not in globals():
                    print("Debe generar una matriz primero.")
                    continue
                
                umbral = int(input("Ingrese el umbral crítico: "))
                valores_criticos = detectar_valores_criticos(matriz_sensores, umbral)
                
                print("\nValores críticos detectados (fila, columna, temperatura):")
                if valores_criticos:
                    for critico in valores_criticos:
                        print(critico)
                else:
                    print("No se detectaron valores críticos")
            except ValueError:
                print("Por favor, ingrese un valor numérico válido para el umbral")
        
        elif opcion == "3":
            print("gracias por usar el programa ")
            break
        else:
            print("Opción no válida. Intente nuevamente")

menu_interactivo()
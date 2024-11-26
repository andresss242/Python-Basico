logs = [
    ["Andres", "08:30", "10:30"],
    ["David", "09:15", "11:20"],
    ["Felipe", "10:10", "11:40"],
    ["Juan", "14:00", "16:45"],
    ["Diego", "11:00", "13:30"],
    ["Camila", "12:05", "13:45"],
    ["Daniela","12:24","14:28"]
]

resultados = []

# Proceso para leer y analizar los datos secuencialmente usando while
indice = 0
usuarios_accesos = {}

while indice < len(logs):
    registro = logs[indice]
    nombre_usuario = registro[0]
    
    # Actualizar el conteo de accesos por usuario
    if nombre_usuario in usuarios_accesos:
        usuarios_accesos[nombre_usuario] += 1
    else:
        usuarios_accesos[nombre_usuario] = 1
    
    indice += 1

# Crear la lista de resultados usando un bucle for
for usuario, accesos in usuarios_accesos.items():
    resultados.append([usuario, accesos])

# Imprimir los resultados
print("Resultados (nombre_usuario, numero_de_accesos):")
for resultado in resultados:
    print(resultado)

tablero = []
for i in range(8):
    fila = []
    for j in range(8):
        if (i + j) % 2 == 0:
            fila.append("▣")  # Casillas blancas
        else:
            fila.append("▢")  # Casillas negras
    tablero.append(fila)

for fila in tablero:
    print(' '.join(fila))

import random

def obtener_eleccion_usuario():
    eleccion = input("Elige piedra, papel o tijera: ").lower()
    while eleccion not in ["piedra", "papel", "tijera"]:
        print("Opción no válida. Intenta de nuevo.")
        eleccion = input("Elige piedra, papel o tijera: ").lower()
    return eleccion

def obtener_eleccion_computadora():
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)

def determinar_ganador(usuario, oponente):
    if usuario == oponente:
        return "empate"
    elif (usuario == "piedra" and oponente == "tijera") or \
        (usuario == "papel" and oponente == "piedra") or \
        (usuario == "tijera" and oponente == "papel"):
        return "usuario"
    else:
        return "oponente"

def jugar_ronda(pvp=False):
    eleccion_usuario = obtener_eleccion_usuario()
    if pvp:
        eleccion_oponente = input("Jugador 2, elige piedra, papel o tijera: ").lower()
    else:
        eleccion_oponente = obtener_eleccion_computadora()
        print(f"Computadora elige: {eleccion_oponente}")

    ganador = determinar_ganador(eleccion_usuario, eleccion_oponente)
    if ganador == "empate":
        print("¡Es un empate!")
    elif ganador == "usuario":
        print("¡Jugador 1 gana esta ronda!")
    else:
        print("Jugador 2 gana esta ronda." if pvp else "Computadora gana esta ronda.")

    return ganador

def juego():
    modo = input("Elige el modo de juego (PvP o PvE): ").lower()
    pvp = (modo == "pvp")
    
    puntuacion_usuario = 0
    puntuacion_oponente = 0
    while puntuacion_usuario or puntuacion_oponente == 3:
        ganador = jugar_ronda(pvp)
        if ganador == "usuario":
            puntuacion_usuario += 1
        elif ganador == "oponente":
            puntuacion_oponente += 1

        print(f"Puntuación: Jugador 1 {puntuacion_usuario} - {'Jugador 2' if pvp else 'Computadora'} {puntuacion_oponente}")

    if puntuacion_usuario == 3:
        print("¡Felicidades! Jugador 1 gana el juego.")
    else:
        print("Jugador 2 ganó el juego." if pvp else "La computadora ganó el juego. Mejor suerte la próxima vez.")

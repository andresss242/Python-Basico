import random

#determina las elecciones del jugador
def seleccion_jugador():
    seleccion = input("escoge: Piedra, Papel o Tijera")
    while seleccion not in ["piedra", "papel", "tijera"]:
        print("opcion no valida")
        seleccion = input("escoge: piedra, papel o tijera ")
        return seleccion
    

#determinar las elecciones de la maquina
def seleccion_maquina():
    opciones = ["piedra", "papel", "tijeras"]
    seleccion = random.choice(opciones)
    return seleccion

def escoger_ganador(jugador,maquina):
    if jugador == maquina:
        return "empate"
    elif (jugador == "piedra" and maquina == "tijera") or \
        (jugador == "papel" and maquina == "piedra") or \
        (jugador == "tijera" and maquina == "papel"):
        return "jugador"
    else:    
        return "maquina"
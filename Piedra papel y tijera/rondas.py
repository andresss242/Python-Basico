from seleccion_opciones import (seleccion_jugador, seleccion_maquina, escoger_ganador)

def jugar_rondas():
    rondas = int(input("¿cuantas rondas desea jugar?"))
    puntaje_jugador = 0
    puntaje_maquina = 0

    for i in range (rondas):
        print(f"\nRonda{i + 1}")
        jugador = seleccion_jugador()
        maquina = seleccion_maquina()
        print(f"la maquina escogio{maquina}")

        ganador = escoger_ganador(jugador,maquina)
        if ganador == "jugador":
            puntaje_jugador += 1
            print("ganas esta ronda")

        elif ganador== "maquina":
            puntaje_maquina += 1
            print("la maquina gana esta ronda")

        else:
            print("empate")

#determinar resultado final
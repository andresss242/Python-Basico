def recoger_informacion():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    genero = input("Género (M/F): ")
    altura = float(input("Altura (en metros): "))
    peso = float(input("Peso (en kg): "))
    sintomas = input("Síntomas actuales: ")
    return {
        "Nombre": nombre,
        "Edad": edad,
        "Género": genero,
        "Altura": altura,
        "Peso": peso,
        "Síntomas": sintomas
    }

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def mostrar_formulario(datos):
    print("\n--- Información del Paciente ---")
    for key, value in datos.items():
        print(f"{key}: {value}")

    imc = calcular_imc(datos["Peso"], datos["Altura"])
    print(f"IMC: {imc:.2f}")

def main():
    datos_paciente = recoger_informacion()
    mostrar_formulario(datos_paciente)

if __name__ == "__main__":
    main()

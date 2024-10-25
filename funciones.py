def mensaje():
    """
    mostrar programacion 1: str
    """
    print("programacion 1")
    x=10

#llamar funcion
mensaje()

def suma (num1,num2):

    rta = num1 + num2
    print(f"la sumam entre {num1}y {num2} es de {rta}")
def solicitar_datos():
    """
    Solicitar num1 y num2, trnsformars a tipo de dato entero y retornar a la informacion 
    """
    num1 = int(input("digite el numero 1: "))
    num2 = int(input("digite el numero 2: "))
    return num1,num2

a,b = solicitar_datos()
print(f"numero digitados {a} y {b}")

suma(a,b)

#multiplicacion 
def multiplicacion (num1,num2):

    rta = num1 * num2
    
    return rta

rta = multiplicacion(a,b)
print(f"el resultado de la multiplicacion es: {rta}")

suma(rta,a)

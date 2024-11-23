class persona():
    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def saluda(self, otra_persona):
        return f"hola {otra_persona.nombre}, me llamo {self.nombre}."
    
#uso 
david = persona("david",35)
erika = persona("erika", 2)

print(david)
class Persona:
    def __init__(self, nombre, cedula, edad):
        self._nombre = nombre
        self._cedula = cedula
        self._edad = edad

    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nuevoNombre):
        self._nombre = nuevoNombre

persona1 = Persona("Mario","40239293929",23)
print(persona1.getNombre())
persona1.setNombre("Mario Pérez")
print("Nuevo nombre:",persona1.getNombre())
        
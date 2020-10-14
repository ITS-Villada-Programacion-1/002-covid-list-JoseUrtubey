class Persona:
    def __init__(self, dni,nombre,apellido,edad,sexo,provincia,fecha):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo
        self.provincia = provincia
        self.fecha = fecha

    def empty(self):
        return self.dni == ".." or self.apellido == "" or self.edad == "" or self.nombre == ""

    def __str__(self):
        return f"Persona: dni:{self.dni} nombre: {self.nombre} apellido:{self.apellido}"
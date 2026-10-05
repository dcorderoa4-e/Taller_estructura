class Estudiante:
    def __init__(self, id, carnet, nombre, apellido, materias=None, notas=None):
        self.id = id
        self.carnet = carnet
        self.nombre = nombre
        self.apellido = apellido
        self.materias = materias if materias else []
        self.notas = notas if notas else {}

    def a_diccionario(self):
        return {
            "id": self.id,
            "carnet": self.carnet,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "materias": self.materias,
            "notas": self.notas
        }

    def promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas.values()) / len(self.notas)

class calificacion:
    def __init__(self):
        pass
    def exámen_de_aprueba(self):
        c1 = float(input("ingrese la primera calificación:"))
        c2 = float(input("ingrese el valor de la segunda calificación:"))
        if c1>=80 or c2>=80:
            print("aceptado")
        else:
            print("rechazado")
tarea=calificacion()
tarea.exámen_de_aprueba()
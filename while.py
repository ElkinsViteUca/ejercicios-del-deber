class ciclow:
    def __init__(self):
        pass
    def ciclo_mientras(self):
        i,suma=1,0
        while i<=100:
            suma = i + 1
            print("el acumulador es:{} la suma es: {}".format(i,suma))
tarea=ciclow()
tarea.ciclo_mientras()
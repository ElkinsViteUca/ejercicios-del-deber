class forrepeticion:
    def __init__(self):
        pass
    def ciclo_for(self):
        suma,n,i=0,0,0
        for i in range(100):
            suma=suma+i*i
            print ("el contador es:{} la suma es:{}".format(i,suma))
tarea=forrepeticion()
tarea.ciclo_for()

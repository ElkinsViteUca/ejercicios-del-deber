class aumento:
    def __init__(self):
        pass
    def aumento_del_sueldo(self):
        sueldo = float(input("ingrese el sueldo:"))
        if sueldo >600:
            nsueldo = sueldo*0.10
            totalsueldo = nsueldo + sueldo
            print("el nuevo sueldo es de:{}".format(totalsueldo))
        else:
            sueldo = sueldo
            print("el sueldo es de:{} ".format(sueldo))

tarea=aumento()
tarea.aumento_del_sueldo()

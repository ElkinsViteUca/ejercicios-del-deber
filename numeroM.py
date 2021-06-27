class numero_mayor:
    def __init__(self):
        pass
    def mayor_de_tres(self):
        n1 = float(input("ingrese el primer número:"))
        n2 = float(input("ingrese el segundo número:"))
        n3 = float(input("ingrese el tercer número:"))
        if n1 > n2 and n1>n3:
            print("numero mayor es :",n1)
        else:
            if n2>n3:
                print("el numero mayor es :",n2)
            else:
                print("numero mayor es :", n3)
tarea=numero_mayor()
tarea.mayor_de_tres()


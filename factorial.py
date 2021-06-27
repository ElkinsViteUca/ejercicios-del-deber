class factorial:
    def factorial(self):
        numero = int(input("Ingrese el numero: "))
        acu=1
        for num in range(numero,1,-1):
            acu = acu * num
        print("numero={} ,factorial={}".format(numero,acu))

tarea = factorial()
tarea.factorial()
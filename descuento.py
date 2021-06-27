class Descuento:
    def __init__(self):
        pass
    def calcular_el_descuento_(self):
        des = float(input("ingres el descuento: "))
        compra = float(input("ingrse total de la compra: "))
        total = compra*(des/100)
        destotal=compra-total
        print("el descuento es del: {}% "  "el total de la compra es: {} lo que debe pagar es: ${}".format(des,compra,destotal))
tarea=Descuento()
tarea.calcular_el_descuento_()      
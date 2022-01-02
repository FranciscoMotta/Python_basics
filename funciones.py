''' def imprimir_mensaje():
    print("HOLA")
    print("BEBECITAAAA")

imprimir_mensaje()
imprimir_mensaje() '''

def conv (mensaje):
    mensaje = str(mensaje)
    print("elegiste la opcion " + mensaje)

opc = int(input('Elige (1, 2, 3): '))
if opc == 1:
    conv(opc)
elif opc == 2:
    conv(opc)
elif opc == 3:
    conv(opc)
else:
    pass

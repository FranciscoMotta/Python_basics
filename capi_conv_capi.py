from os import name


def capicuo (numer):
    numero_inv = numer[::-1]
    if numer == numero_inv:
        return True
    else:
        return False

def convertidor (numero):
    estado = True
    while(estado):
        numero_inv = numero[::-1]
        numero_inv = int(numero_inv)
        numero = int(numero)
        suma = numero_inv + numero
        suma = str(suma)
        des = capicuo(suma)
        if des == True:
            estado = False
        else:
            estado = True
            numero = suma
    return str(suma)



def main():
    num = input("Ingresa el numero: ")
    capi = capicuo(num)
    if capi == True:
        print("Es capicuo")
    else:
        print("No es capicuo")
        des = input("Desea convertirlo? Y/N: ")
        if des == 'Y':
            print("CONVERTIENDO...")
            result = convertidor(num)
            print("El numero convertido a capicua es: " + result)
            
        else:
            print("OK, BYE")

if __name__ == '__main__':
    main()
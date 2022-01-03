def capicuo (numer):
    numero_inv = numer[::-1]
    if numer == numero_inv:
        return True
    else:
        return False

def conv (numero):
    llave = True
    count = 0
    pasos = 1
    while(llave):
        for i in numero:
            count = count + int(i)
        val = int(numero) + count
        print(str(numero) + '+' + str(count) + '=' + str(val))
        count = 0
        if capicuo(str(val)) == True:
            llave = False
            print('El capicuo conv es: ' + str(val) + ' Hallado en: ' + str(pasos) + ' pasos')
        else:
            pass
        pasos+=1
        numero = str(val)

def main():
    num = input('Ingresa un numero: ')
    estado = True
    while(estado):
        valor = capicuo(num)
        if valor == True:
            print('Es capicuo')
            estado = False
        else:
            print('No es capicuo')
            des = input ('Desea convertirlo? Y/N: ')
            if des == 'Y':
                print('OK')
                conv(num)
                estado = False
            else:
                print('OK, BYE')
                estado = False
                
if __name__ == '__main__':
    main()
def paridad(num):
    par = num%2
    if par == 0:
        print('ES PAR')
    else:
        print('NO ES PAR')
def imparidad(num):
    impar = num%2
    if impar == 0:
        print('NO ES IMPAR')
    else:
        print('ES IMPAR')
def primalidad(num):
    estado = True
    contador = 2
    while(estado):
        primo = num%contador
        div = round(num / contador,0)
        if (primo == 0) and (div != 1):
            estado = False
            print('NO ES PRIMO: ')
            print(str(num) + '/' + str(contador) + '=' + str(div))
        else:
            estado = True
            pass

        contador = contador + 1

        if contador == 10:
            estado = False
            print('ES PRIMO')
        else:
            pass

def multiplicidad(num):
    MIN = 2
    MAX = 9
    for i in range(MIN, MAX):
        multiplo = num%i
        if (multiplo == 0):
            print(str(i) + ' es multiplo de ' + str(num))
            print(str(num) + '/' +str(i)+ '=' + str(round(num/i,0)))
        else:
            pass

def main():
    numero = int(input('introduce un numero: '))
    opciones = '''
    1.- paridad
    2.- imparidad
    3.- primalidad
    4.- multiplicidad
    '''
    op = input(opciones)
    if op == '1':
        print('PARIDAD')
        paridad(numero)
        pass
    elif op == '2':
        print('IMPARIDAD')
        imparidad(numero)
        pass
    elif op == '3':
        print('PRIMALIDAD')
        primalidad(numero)
        pass
    elif op == '4':
        print('MULTIPLICIDAD')
        multiplicidad(numero)
        pass
    else:
        pass
if __name__ == '__main__':
    main()
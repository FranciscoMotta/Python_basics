def tabla(nume):
    for i in range(1,11):
        prod = nume*i
        prod = str(prod)
        print(str(i) + ' x ' + str(nume) + ' = ' + prod)

def main():
    num = int(input('Ingresa un numero: '))
    print('la tabla del ' + str(num) + 'es: ')
    tabla(num)

if __name__ == '__main__':
    main()
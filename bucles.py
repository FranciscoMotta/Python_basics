def main():
    LIMITE = 1000 # Definimos una constante
    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print('La potencia de 2^' + str(contador) + ' es: ' + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador

if __name__ == '__main__':
    main()
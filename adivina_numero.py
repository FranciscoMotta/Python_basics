import random # Para funciones aleatorias 

def main():
    numero_rand = random.randint(0,100) # Numero aletorio dentre 0 - 100
    numero_elegido = int(input('Ingrese un numero entre 0 - 100 : '))
    intentos = 0
    while numero_elegido  != numero_rand:
        if numero_elegido > numero_rand:
            numero_elegido = int(input('Ingrese un numero menor: '))
            intentos -=-1
        elif numero_elegido < numero_rand:
            numero_elegido = int(input('Ingrese un numero mayor: '))
            intentos -=-1
        else:
            pass
    print('GANASTE! INTENTOS: ' + str(intentos))

if __name__ == '__main__':
    main()
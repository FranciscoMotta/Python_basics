import random

def generar_cont():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    caracte = MAYUS + MINUS + NUMS + CHARS

    contrase = []

    for i in range(15):
        caracter_ran = random.choice(caracte) # Elegimos un elementos aleatorio
        contrase.append(caracter_ran) # agregamos a la lista de la contraseña
    
    # convertimos una lista a string
    contrase = ''.join(contrase)

    return contrase

def main():
    passw = generar_cont()
    print('Tu nueva clave es: ' + passw)

if __name__ == '__main__':
    main()
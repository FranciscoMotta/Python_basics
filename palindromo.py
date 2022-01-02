def palindromo(palabra):
    palabra = palabra.replace(' ','')
    palabra = palabra.lower()
    palabra_inv = palabra[::-1] # Invertimos la palabra

    if palabra == palabra_inv:
        return True
    else:
        return False

def main():
    palabra = input("Introduce la frase o palabra: ")

    palin = palindromo(palabra)
    if palin == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__': # punto de entrada
    main()
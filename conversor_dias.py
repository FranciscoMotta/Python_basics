convs = """
BIENVENIDO AL CONVERSOR DE TIEMPO
ELIGE A QUE QUIERES CONVERTIR TUS DÍAS
1.- SEMANAS
2.- MESES
3.- AÑOS
4.- LUSTROS

"""

elecc = int(input(convs))

dias = int(input("Ingresa tus dias a convertir: "))

if elecc == 1:
    valor = dias/7
    valor = str(round(valor, 2))
    dias = str(dias)
    print("Tus " + dias + " equivale a :" + valor + " semanas")
elif elecc == 2:
    valor = dias/30
    valor = str(round(valor, 2))
    dias = str(dias)
    print("Tus " + dias + " equivale a :" + valor + " meses")
elif elecc == 3:
    valor = dias/365
    valor = str(round(valor, 2))
    dias = str(dias)
    print("Tus " + dias + " equivale a :" + valor + " años")
elif elecc == 4:
    valor = dias/1825
    valor = str(round(valor, 2))
    dias = str(dias)
    print("Tus " + dias + " equivale a :" + valor + " lustros")
else:
    pass


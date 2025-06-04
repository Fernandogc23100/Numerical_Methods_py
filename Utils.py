def pedir_lista_float(mensaje):
    lista = input(mensaje + " (separados por espacios): ")
    return [float(x) for x in lista.strip().split()]

def pedir_lista_pares():
    n = int(input("Ingrese la cantidad de pares de datos: "))
    pares = []
    for i in range(n):
        x = float(input(f"x[{i+1}]: "))
        y = float(input(f"y[{i+1}]: "))
        pares.append((x, y))
    return pares

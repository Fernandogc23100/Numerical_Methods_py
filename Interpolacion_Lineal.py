def interpolacion_lineal(pares, xi):
    """
    Realiza interpolacion lineal para el valor xi.
    pares: lista de tuplas (x, y)
    xi: valor de x a interpolar
    """
    pares = sorted(pares)
    for i in range(len(pares) - 1):
        x0, y0 = pares[i]
        x1, y1 = pares[i + 1]
        if x0 <= xi <= x1:
            return y0 + ((y1 - y0)/(x1 - x0)) * (xi - x0)
    raise ValueError("El valor de x esta fuera del rango de los datos.")
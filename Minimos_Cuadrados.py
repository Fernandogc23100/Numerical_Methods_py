def regresion_lineal(pares):
    """
    Realiza regresion lineal por minimos cuadrados.
    pares: lista de tuplas (x, y)
    Retorna pendiente (a) y ordenada (b)
    """
    n = len(pares)
    sum_x = sum_y = sum_xx = sum_xy = 0
    for x, y in pares:
        sum_x += x
        sum_y += y
        sum_xx += x * x
        sum_xy += x * y

    a = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x**2)
    b = (sum_y - a * sum_x) / n
    return a, b

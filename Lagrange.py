import sympy as sp

def lagrange_polinomio(pares):
    x = sp.symbols('x')
    n = len(pares)
    polinomio = 0
    for i in range(n):
        xi, yi = pares[i]
        termino = yi
        for j in range(n):
            if i != j:
                xj, _ = pares[j]
                termino *= (x - xj) / (xi - xj)
        polinomio += termino
    return sp.simplify(polinomio)

def lagrange_evaluacion(pares, xi):
    pol = lagrange_polinomio(pares)
    return pol.subs('x', xi).evalf()
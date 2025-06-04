import cmath

def evaluar_polinomio(coef, x):
    res = coef[0]
    for c in coef[1:]:
        res = res * x + c
    return res

def muller_method(coef, x0, x1, x2, tol=1e-6, max_iter=100):
    """
    Metodo de Muller para encontrar una raiz de un polinomio.
    coef: lista de coeficientes de mayor a menor grado
    x0, x1, x2: estimaciones iniciales
    """
    for _ in range(max_iter):
        f0 = evaluar_polinomio(coef, x0)
        f1 = evaluar_polinomio(coef, x1)
        f2 = evaluar_polinomio(coef, x2)
        
        h1 = x1 - x0
        h2 = x2 - x1
        d1 = (f1 - f0) / h1
        d2 = (f2 - f1) / h2
        a = (d2 - d1) / (h2 + h1)
        b = a * h2 + d2
        c = f2
        
        disc = cmath.sqrt(b**2 - 4*a*c)
        den1 = b + disc
        den2 = b - disc
        
        if abs(den1) > abs(den2):
            den = den1
        else:
            den = den2
            
        if den == 0:
            return x2  # evitar division por cero
            
        dx = -2 * c / den
        x = x2 + dx
        
        if abs(dx) < tol:
            return x
        
        x0, x1, x2 = x1, x2, x
    return x2  # retorna la ultima estimacion si no converge
def horner_evaluation(coeficientes, x):
    """
    Evalua un polinomio en x usando el metodo de Horner.
    coeficientes: lista de coeficientes de mayor a menor grado
    x: valor en el que se evaluara el polinomio
    """
    resultado = coeficientes[0]
    for coef in coeficientes[1:]:
        resultado = resultado * x + coef
    return resultado
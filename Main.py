from Horner import horner_evaluation
from Muller import muller_method
from Interpolacion_Lineal import interpolacion_lineal
from Lagrange import lagrange_evaluacion, lagrange_polinomio
from Minimos_Cuadrados import regresion_lineal
from Utils import pedir_lista_float, pedir_lista_pares

def menu():
    while True:
        print("\n" + "="*50)
        print("                      MENU")
        print("="*50)
        print("Seleccione una opción:\n")
        print("  [1] Evaluación Polinomial (Horner)")
        print("  [2] Método de Muller")
        print("  [3] Interpolación Lineal")
        print("  [4] Evaluación de Lagrange")
        print("  [5] Polinomio de Lagrange")
        print("  [6] Regresión Lineal (Mínimos Cuadrados)")
        print("  [0] Salir\n")
        print("\n" + "="*50)
        print("                      GC23100")
        print("="*50)


        opcion = input("Ingrese el número de opción: ")

        if opcion == "1":
            coef = pedir_lista_float("Ingrese los coeficientes del polinomio (de mayor a menor grado): ")
            x = float(input("Ingrese el valor de x: "))
            resultado = horner_evaluation(coef, x)
            print(f"\nResultado: {resultado}")

        elif opcion == "2":
            coef = pedir_lista_float("Ingrese los coeficientes del polinomio (de mayor a menor grado): ")
            x0 = float(input("x0: "))
            x1 = float(input("x1: "))
            x2 = float(input("x2: "))
            raiz = muller_method(coef, x0, x1, x2)
            print(f"\nRaíz encontrada: {raiz}")

        elif opcion == "3":
            pares = pedir_lista_pares()
            xi = float(input("Ingrese el valor de x a interpolar: "))
            resultado = interpolacion_lineal(pares, xi)
            print(f"\nResultado: {resultado}")

        elif opcion == "4":
            pares = pedir_lista_pares()
            xi = float(input("Ingrese el valor de x a evaluar: "))
            resultado = lagrange_evaluacion(pares, xi)
            print(f"\nResultado: {resultado}")

        elif opcion == "5":
            pares = pedir_lista_pares()
            polinomio = lagrange_polinomio(pares)
            print(f"\nPolinomio de Lagrange: {polinomio}")

        elif opcion == "6":
            pares = pedir_lista_pares()
            a, b = regresion_lineal(pares)
            print(f"\nModelo: y = {a}x + {b}")

        elif opcion == "0":
            print("\nSaliendo del programa. ¡Gracias!")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
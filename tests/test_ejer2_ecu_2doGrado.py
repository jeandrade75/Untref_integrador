# Escribir una función que dado el ingreso de 3 variables (a, b, c) retorne las raíces resultantes de una ecuación cuadrática.

import math

def resolver_ecuacion_cuadratica(a, b, c):
    # Calculamos el discriminante
    discriminante = b**2 - 4*a*c
    
    # Si el discriminante es negativo, no hay raíces reales
    if discriminante < 0:
        return "No hay raíces reales"
    
    # Calculamos las dos soluciones
    raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
    raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
    
    return raiz1, raiz2

# Ejemplo de uso:
resolver_ecuacion_cuadratica(2, 3, -5)

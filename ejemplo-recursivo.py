"""

    Uso de recursividad para calcular el factorial de un número.
"""

def obtener_factorial(numero):
    """
    Función recursiva para calcular el factorial de un número.
    
    Parámetro:
    - numero (int): Número para calcular su factorial.
    
    Retorna:
    - int: El factorial del número ingresado.
    """
    
    if numero <= 1:
        # Caso base: Cuando el número es 1 o menor, se detiene la recursión
        # y retorna 1, ya que 1! = 1 y 0! = 1.
        return 1
    else:
        # Paso recursivo: Se multiplica el número actual por el factorial
        # del número anterior (numero - 1), llamando nuevamente a la función.
        return numero * obtener_factorial(numero - 1)

# Punto de entrada principal del script
if __name__ == '__main__':
    
    # Llamada a la función recursiva con el número 5
    resultado = obtener_factorial(5)
    
    # Se imprime el resultado del cálculo factorial
    print(f"Valor Factorial (-- usando recursividad --): {resultado}")


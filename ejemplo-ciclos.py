"""
    Uso de iteración para calcular el factorial de un número.
"""

def obtener_factorial(numero):
    """
    Función que tiene un proceso de iteraciónpara calcular el factorial de un 
    número.
    
    Parámetro:
    - numero (int): Número para calcular su factorial.
    
    Retorna:
    - int: El factorial del número ingresado.
    """

    # Inicializar la variable del factorial en 1
    valor_factorial = 1
    
    # Bucle para calcular el factorial en orden descendente
    for i in range(numero, 0, -1):
        valor_factorial = valor_factorial * i  # Multiplicar el valor actual del factorial por i
    
    return valor_factorial

if __name__ == '__main__':

    resultado = obtener_factorial(5)
    print(f"Valor Factorial (-- usando ciclos --): {resultado}")

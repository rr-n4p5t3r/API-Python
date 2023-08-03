import sys
from helpers import obtener_puerto_peticion, generar_password, generar_secreto_256_bits

# Obtener el nombre de la función desde la línea de comandos
nombre_funcion = sys.argv[1] if len(sys.argv) > 1 else None
parametro1 = sys.argv[2] if len(sys.argv) > 2 else None
parametro2 = sys.argv[3] if len(sys.argv) > 3 else None

if nombre_funcion and nombre_funcion in globals() and callable(globals()[nombre_funcion]):
    # Ejecutar la función
    if parametro1 is not None and parametro2 is not None:
        response = globals()[nombre_funcion](parametro1, parametro2)
    if parametro1 is not None and parametro2 is None:
        response = globals()[nombre_funcion](parametro1)
    if parametro1 is None and parametro2 is None:
        response = globals()[nombre_funcion]()
    print(response)
else:
    print("La función especificada no existe")
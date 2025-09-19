"""
Akemi Clarissa Olvera Arao
19/09/25
Determinar si una palabra comienza con una vocal      
"""

# Declaraciones
VOCALES = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

# Entradas
palabra = input("Ingrese una palabra: ")

# Proceso 
inicial_vocal = False 
for vocal in VOCALES:
    if palabra[0] == vocal:
        print(palabra, "empieza con una vocal")
        inicial_vocal = True
if inicial_vocal == False:
    print(palabra, "no empieza con vocal")

# Salidas


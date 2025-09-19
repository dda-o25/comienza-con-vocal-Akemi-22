"""
Akemi Clarissa Olvera Arao
19/09/25
Determinar si una palabra comienza con una vocal      
"""

# Declaraciones
VOCALES = ["A", "Á", "a", "á", "E", "É", "e", "é", "I", "Í", "i", "í", "O", "Ó", "o", "ó", "U", "Ú", "u", "ú"]

# Entradas
palabra = input("Ingrese una palabra: ")

# Proceso 
inicial_vocal = False 
for vocal in VOCALES:
    if palabra[0] == vocal:
        print(palabra, "comienza con una vocal")
        inicial_vocal = True
if inicial_vocal == False:
    print(palabra, "no comienza con vocal")

# Salidas


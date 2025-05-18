palabra = input("Escribe una palabra: ")
longitud = len(palabra)

if 4 <= longitud <= 8:
    print("La palabra tiene la longitud adecuada.")
elif longitud < 4:
    print(f"Faltan caracteres, por favor intenta de nuevo. {longitud} letras.")
else:
    print(f"exceso de caracteres. {longitud} letras.")

x = int(input("Ingrese X: "))
y = int(input("Ingrese Y: "))

if x == 0 or y == 0:
    print("Las coordenadas no pueden ser 0.")
else:
    if x > 0 and y > 0:
        print("El punto se encuentra en el cuadrante I.")
    elif x < 0 and y > 0:
        print("El punto se encuentra en el cuadrante II.")
    elif x < 0 and y < 0:
        print("El punto se encuentra en el cuadrante III.")
    elif x > 0 and y < 0:
        print("El punto se encuentra en el cuadrante IV.")
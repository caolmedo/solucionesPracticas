#Etructura iterativa: Pedir que el usuario ingrese (input) nombre de personas y mostrarlos hasta que el valor de lo que ingresa sea “fin”


nombre = ""

while nombre.lower() != "fin":
    nombre = input("Ingrese un nombre o 'fin' cuando desee terminar: ")
    if nombre.lower() != "fin":
        print(nombre)

print("Programa finalizado")

#Fin
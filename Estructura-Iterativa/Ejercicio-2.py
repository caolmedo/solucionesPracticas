#Mostrar sólo los números pares desde 0 hasta el número ingresado (input). Nota: para saber si un número es par hacer i % 2 == 0)
#Se solcita al usuario que ingrese un número entero

numero = int(input("Ingrese un numero entero: "))
for i in range (0, numero +1):
     if i % 2 == 0:
          print (i)

#Fin
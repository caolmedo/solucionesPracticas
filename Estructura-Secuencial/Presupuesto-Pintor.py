print ("Presupuesto de pintor")

#Ingresar los datos de la pared en metros y el costo por metro cuadrado

largo = float(input("Ingrese el largo de la pared en metros: "))
alto = float(input("Ingrese el alto de la pared en metros: "))
precio = float(input("Ingrese el precio por metro cuadrado: "))

#Calculo para saber el presupuesto

metroscuadrados = largo * alto
presupuesto = metroscuadrados * precio   

#Valor final del presupuesto

print(f"Metros cuadrados a pintar: {metroscuadrados:.2f}")
print(f"El presupuesto para pintar la pared es de: {presupuesto:.2f}")

#Fin

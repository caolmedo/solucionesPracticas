Algoritmo PresupuestoPintor
	Definir  largo, alto, metroscuadrados, precio, costo como real
	
	Escribir "Ingrese el largo de la pared en metros: "
	Leer largo
	
	Escribir "Ingrese el alto de la pared en metros: "
	Leer alto
	
	Escribir "Ingrese el precio por metro cuadrado: "
	Leer precio
	
	metroscuadrados = largo * alto
	costo = metroscuadrados * precio
	
	Escribir "Metros cuadrados totales: ", metroscuadrados
	Escribir "Costo final por pintar la pared: ", costo
	
FinAlgoritmo

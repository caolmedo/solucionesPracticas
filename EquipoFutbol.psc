Algoritmo EquipoFutbol
	Definir partidosPerdidos, partidosGanados, partidosEmpatados Como Entero
	Definir puntosporPartidoPerdido, puntosporPartidoGanado, puntosporPartidoEmpatado, puntajeTotal Como Real
	
	puntosporPartidoEmpatado = 1
	puntosporPartidoGanado = 3 
	puntosporPartidoPerdido = 0
	
	Escribir "Ingrese la cantidad de partidos ganados, empatados o perdidos para saber su puntaje total"
	
	Escribir "Total de partidos ganados: "
	Leer partidosGanados
	
	Escribir "Total de partidos empatados: "
	Leer partidosEmpatados
	
	Escribir "Total de partidos perdidos: "
	Leer partidosPerdidos
	
	puntajeTotal = (puntosporPartidoEmpatado * partidosEmpatados) + (puntosporPartidoGanado * partidosGanados) + (puntosporPartidoPerdido * partidosPerdidos)
	
	Escribir "El puntaje final del torneo es: ", puntajeTotal
	
FinAlgoritmo

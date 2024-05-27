print ("Puntos totales del equipo en el campeonato")

#Ingreso de datos de todos los partidos jugados

print ( "Ingrese la cantidad de partidos ganados, empatados o perdidos para saber su puntaje total" )

partidos_ganados = int(input("Total de partidos ganados: "))
partidos_empatados = int(input("Total de partidos empatados: ")) 
partidos_perdidos = int(input("Total de partidos perdidos: "))

#Calculo de los puntos de los partidos

puntos_ganados = partidos_ganados * 3
puntos_empatados = partidos_empatados * 1
puntos_perdidos = partidos_perdidos * 0
puntos_totales = puntos_ganados + puntos_empatados + puntos_perdidos 

#Calculo final de puntos totales

print(f"El puntaje final del torneo es: {puntos_totales}")

#Fin

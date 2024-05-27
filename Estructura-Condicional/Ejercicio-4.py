#Estructura condicional completa (if - else) + Expresión lógica compuesta (and)

#Corroborar si la persona puede comprar alcohol

edad= int(input( "Ingrese su edad: "))
comprar_alcohol = input("¿Tiene usted dinero? (True/False): ")
if edad >= 18 and comprar_alcohol.lower() == 'true': 
     print("Si puede comprar alcohol")
else:
     print("No puede comprar alcohol")

#Fin
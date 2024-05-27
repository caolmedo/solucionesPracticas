#Calculo de Leche Despensa

#Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos la unidad.
#Si el cliente compra más de 12  unidades (y hasta 24 unidades), el costo tiene un descuento del 10%.
#Si compra más de 24 unidades, el descuento es del 15%.
#Además posee la promoción a los jubilados.
#La promoción de jubilados es sumarle un 10% de descuento (si posee otros descuentos, se suma los descuentos).
#Desarrolle una solución algorítmica para saber cuento debe pagar el cliente.


Unidades_deleche= int(input ("Ingrese la cantidad de unidades de leche que usted desea comprar: "))

jubilado = input("¿Es usted jubilado? True/False: ").strip().lower() == "true"

Monto_Parcial = Unidades_deleche* 1000


if  Unidades_deleche <= 12:
    monto_a_pagar = Monto_Parcial

elif Unidades_deleche > 12 and Unidades_deleche <= 24:
    monto_a_pagar = (Monto_Parcial - (Monto_Parcial* 0.1))

elif Unidades_deleche > 24:
     monto_a_pagar = (Monto_Parcial - (Monto_Parcial* 0.15))

if jubilado:
    print ("Usted tiene un descuento")
    monto_a_pagar= monto_a_pagar - (monto_a_pagar * 0.1)


print (f"El costo total sin descuento es: {Monto_Parcial} y el monto total a pagar con descuento es {monto_a_pagar} .")

#Fin
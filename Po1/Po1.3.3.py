# un program que imprima
# el precio actual de un
# producto tras aplicarle
# un 10% de descuento


#1.imprimir matricula
print("20091665")
#2.leer precio
precio=input("digite precio: ")
precio=int(precio)
#3.calculamos el 10%
diez_porciento = precio * 0.1
#4. restamos el 10% al precio
precio_actual = precio - diez_porciento
#5. mostrarselo al usuario
print(precio_actual)

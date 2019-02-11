#Escribe un programa que imprima los numeros
# menores que 10 y divisibles entre 3


serie = [1,2,3,4,5,6,7,8,9,10]
serie = range(1,11) #esto es equivalente

#solucion usando for
contador = 0
for cada_valor in serie:
    if cada_valor<5 and cada_valor%3==0:
        contador += 1


print("Cantidad de numero que cumplen"
      "condicion: ", contador)

serie = [1,2,3,4,5,6,7,8,9,10]
i = 0
contador = 0
while i < len(serie):
    cada_valor = serie[i]
    if cada_valor<5 and cada_valor%3==0:
        contador += 1
    i += 1 # i = i + 1
print("Cantidad de numero que cumplen"
      "condicion: ", contador)

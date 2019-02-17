# crea una función que sume los elementos de una lista

listado = [20170596, 20180149, 20180812]

def suma(lista:list[int]) -> int:
    acumulador = 0
    for valores in lista:
        acumulador += valores
    return acumulador

resultado = suma(listado)

print(resultado)

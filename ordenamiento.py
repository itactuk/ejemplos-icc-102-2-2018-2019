# halla la mediada



def mediana(lista):
    lista.sort()
    n = len(lista)
    if n%2==0:
        punto_medio =  n/2
        punto_medio2 = punto_medio - 1
        res = (lista[punto_medio] + lista[punto_medio2])/2
        return res
    else:
        punto_medio = n//2
        return lista[punto_medio]


listado = [6,3,4,5,7]
listado.sort()
print(listado)
print(mediana(listado))


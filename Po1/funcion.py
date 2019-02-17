# funcion que calcule la moda de 3 numeros


def moda(a,b,c):
    if a==b and b==c:
        return a
    elif a==b:
        return a
    elif b==c:
        return b
    elif a==c:
        return a
    else:
        return None

print(moda(1,2,3))
x=moda(1,2,3)
print(x)
print(moda(a=2,b=2,c=3))

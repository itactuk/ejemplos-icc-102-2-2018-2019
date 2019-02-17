import math
# hallar la hipotenusa de un triangulo rectangulo

def hallar_hipotenusa(cateto1, cateto2):
    """
    esta función halla la hipotenusa de un triángulo rectángulo
    h = raiz cuadrada de (catero al cuadrado + el otro cateto al cuadrado)
    h = √(a^2 + b^2)
    """
    resultado = math.sqrt((cateto1**2)+(cateto2**2))
    return resultado

c1 = int(input("cateto1:"))
c2 = int(input("cateto2:"))

print(hallar_hipotenusa(c1,c2))




"""
Haz un programa que imprima el patron de abajo para un numero n
  *  2 espacios 1 asterisco
 **  1 espacios 2 asteriscos
***  0 espacios 3 asteriscos
 **  1 espacios 2 asteriscos
  *  2 espacios 1 asterisco

espacios serie
(n=5)
2,1,0,1,2
(n==9)
4,3,2,1,0,1,2,3,4
1,2,3,4,5,6,7,8,9
con mod n//2+1
1,2,3,4,0,1,2,3,4
(n//2+1)-i solo a los num < n//2
"""
print("20091665")

# 1.leer n
n = input("Lee n: ")
# 2.conv n a int
n =int(n)
# 3. repetir n veces:
for i in range(1,n+1):
    cant_espacios=None
    if i <=n//2:
        cant_espacios=(n//2+1)-i
        for x in range(0, (n//2+1)-i):
            print(" ", end='')
    else:
        cant_espacios=i%(n//2+1)
        for x in range(0, i%(n//2+1) ):
            print(" ", end='')
    for x in range(0, (n//2+1)-cant_espacios):
        print("*",end='')
#    3.a Imprimir x espacios, y asterisc:
#       3.a.1 para cada i en el rango de 1 a n (inclusive):
#           if i<n//2:
#               3.a.1.1.1 imprimimos (n//2+1)-i espacios
#           else:
#               3.a.1.2.1 imprimimos i%mod n//2+1 espacios
#     imprimimos (n//2+1)-espacios) asteriscos
#    3.b Imprimir y asteriscos
#    3.c Un cambio de linea
    print()
print("Fin del programa")

print("20091665")
""""
un programa que diga
si naciste en un dia
bueno, malo o regular
bueno es diciembre 10-Junio 10
regu es Junio 11 - sept 20
malo es sep 21 - deciembre 9

OR
TRUE or TRUE = TRUE
TRUE or FALSE = TRUE
FALSE or TRUE = TRUE
FALSE or FALSE = FALSE

AND
TRUE and TRUE = TRUE
TRUE and FALSE = FALSE
FALSE and TRUE = FALSE
FALSE and FALSE = FALSE

"""


#1. leer dia
dia = int(input("Digite el día (nn): "))
#2. leer mes
mes = int(input("Digite mes en forma númerica(n): "))

#2.2 Si el dia es valido cotniuna con 3, de lo contrario di no valido
if not((mes in [1,3,5,7,8,10,12] and dia<=31 and dia>=1) \
    or (mes in [4,6,9,11] and dia<=30 and dia>=1) \
    or (mes==2 and dia<=28 and dia>=1)):
    print("no dia valido")
#3. Si el dia esta entre dic 10 y Junio 10
#   mostramos "dia bueno"
elif (dia>=10 and mes ==12) or (mes==6 and dia<=10) or (mes>=1 and mes <=9):
    print("dia bueno")
#4. de lo contrario, Si dia entre junio 11, sept 20
#  mostramos "dia regular"
elif (dia>=11 and mes ==6) or (mes==9 and dia<=20) or (mes>=7 and mes <=8):
    print("dia regular")
#5. de lo contrario, Si dia entre sep 11-dec9
#  mostramos "dia malo"
else:
    print("dia malo")



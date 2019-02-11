#Programa que imprima serie de abajo hasta n
#1
#12
#123
#1234


n=int(input("Digite n: "))
for i in range(1,n+2):
    for j in range(1,i):
        print(j,end='')
    print()

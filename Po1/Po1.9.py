
#hacer programa que imprima la siguente serie hasta n
# 2, 4, 8, 16, 32, 64, 128, etc.
# 2, 2*2, (2*2)*2, (2*2*2*2)*2,...

n = int(input("Digite n: "))


valor = 1
while n > valor:
    valor = valor * 2 # valor*=2
    print(valor, ','  , end='')

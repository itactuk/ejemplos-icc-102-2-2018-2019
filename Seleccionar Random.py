import random

estudiantes = [
    "JEAN A. GRULLÓN E.",
    "ELIÁN D. AMPARO L.",
    # "AYLEEN BETANCES D.",
    "CHANTAL M. READ R.",
    "GISELLE M. ÁNGELES E.",
    "DIEGO A. GONZÁLEZ L.",
    "KENNEDY R. SANTANA G.",
    "ALVIN D. RODRÍGUEZ D.",
    # "NICOLE M. MEDINA C.",
    "GERMINA V. GERMEILLE",
    "MARCOS C. NÚÑEZ G.",
    "MIGUEL D. GUZMÁN V.",
    # "EMELY RODRÍGUEZ M.",
    "HERBERT N. CASTILLO P.",
]

ejercicios = []
Ex1 = ['a', 'b', 'c', 'd']
Ex1_cant = 18
Ex1P = ['a', 'b', 'c']
Ex1P_cant = 3
Ex2P = ['a', 'b', 'c', 'd']
Ex2P_cant = 13
Ex2T = ['a', 'b', 'c']
Ex2T_cant = 16
def add_ex(suffix, versions, cant):
    for v in versions:
        for i in range(1, cant+1):
            ejercicios.append(suffix + v + '.' + str(i))
add_ex('Ex1', ['a', 'b', 'c', 'd'], 18)
add_ex('Ex1P', ['a', 'b', 'c'], 3)
add_ex('Ex2P', ['a', 'b', 'c', 'd'], 13)
add_ex('Ex2T', ['a', 'b', 'c'], 16)

cur_estudiante = 0
cur_ej = 0

print_ex = input('Print ex?')

while True:
    if cur_ej == 0:
        print('Ejercios fueron reiniciados')
        random.shuffle(ejercicios)
    if cur_estudiante == 0:
        print('Estudiantes fueron reiniciado')
        random.shuffle(estudiantes)
    print(estudiantes[cur_estudiante:])
    if print_ex.upper() != 'N':
        print(ejercicios[cur_ej] + ' para ' + estudiantes[cur_estudiante])
    lectura = input()
    if lectura == 'n':
        cur_estudiante -= 1
    cur_ej += 1
    cur_estudiante +=1
    cur_ej %= len(ejercicios)
    cur_estudiante %= len(estudiantes)

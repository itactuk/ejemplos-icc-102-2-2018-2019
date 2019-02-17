# Un programa que lea una matricula,
# imprima el nombre del estudiante
# y diga si el nombre del estudiante contiene una letra a

matriculas = {
    '20170596': "EDWARD",
    '2018-0018':"Diego",
    "2018-0149": "ELIAN"
} # se declaro el diccionario matriculas que contiene las llaves 20170596, 2018-0018, 2018-0149
  # y los EDWARD, Diego, ELIAN

matricula_a_buscar = input("Digite la matricula: ") # Se le pide la matricula al usuario

if matricula_a_buscar in matriculas: # Si la matricula digitada por el usuario se encuentra en el diccionario matricula, imprime la matricula y verifica si contiene la letra a; de lo contrario di que la matricula no existe
    nombre = matriculas[matricula_a_buscar]
    print(nombre)
    if 'a' in nombre:
        print("Sí tiene la letra a")
    else:
        print ("No tiene la letra a")
else:
    print("Esta matricula no esta registrada")

#Sintaxis simple
# if condición:
#   sentencia1
#   sentencia2
# sentencias fuera del if

# Sintaxis con else
# if condición:
#   sentencia1
#   sentencia2
# else:
#   sentenciaAlternativa1
#   sentenciaAlternativa2
# sentencias fuera del if







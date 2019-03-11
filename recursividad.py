# Resolver expresiones matemáticas con paréntesis. Solo suma

#Ejemplo
#Entrada: "(1+2+(3+4+3+(1+2)))"
#Proceso: "(1+2+(3+4+3+1))"
#Proceso: "(1+2+13)"
#Proceso: "16"
#Salida: 16

def solucionar(expresion):
    inicio = expresion.find('(')
    if inicio!=-1: #no hay parentesis
        fin = expresion.rfind(')')
        expresion_sin_parentisis = expresion[inicio+1:fin]
        res_parentesis = solucionar(expresion_sin_parentisis)
        expresion=expresion.replace("("+expresion_sin_parentisis+")",res_parentesis)
    sum = 0
    for e in expresion.split("+"):
        sum+=int(e)
    return str(sum)
    # return resultado #String

res = solucionar("(1+2+(3+4+3+(1+2)))")
print(res)

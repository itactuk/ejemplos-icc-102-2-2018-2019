# mover_pieza(pieza,coord): True (si es valida) y False (si no lo es)
# asignar_posicion(pieza,coord): True (si es valida) y False (si no lo es)
# quitar_pieza(coord): None
# inicializar_tablero(tablero)
# jugar():None
# gano(): String (Jugador1, Jugador2, tabla, ninguno)
# mostrar_tablero()
tablero = [
    ['T','C','A','R','D','A','C','T'],
    ['P','P','P','P','P','P','P','P'],
    ['v','v','v','v','v','v','v','v'],
    ['v','v','v','v','v','v','v','v'],
    ['v','v','v','v','v','v','v','v'],
    ['v','v','v','v','v','v','v','v'],
    ['p','p','p','p','p','p','p','p'],
    ['t','c','a','r','d','a','c','t']
]

def mostrart_tablero(tablero):
    for fila in tablero:
        for cuadro in fila:
            print(cuadro,end='')
        print()
mostrart_tablero(tablero)
def jugar():
    nombre1 =input("Nombre Jugador Blancas:")
    nombre2=input("Nombre Jugador Negras:")
    turno = 'blancas'
    while gano()=='ninguno':
        mostrar_tablero()
        pieza = input('Digite pieza')
        coord = input('Digite coordena')
        mover_pieza(pieza,coord)




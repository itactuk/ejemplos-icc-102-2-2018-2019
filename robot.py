#camine
#escriba
#haga tarea
#trabaje


## declaro el tipo de dato llamdo robot
class robot:
    def __init__(self, nombre): # función especial para inicializar (o crear) un robot
        self.nombre = nombre
    def camine(self, destino):
        print("El "+self.nombre+" camina hacia "+destino)
    def escribe(self, text):
        print("El "+self.nombre+" escribe: '"+text+"'")
    def hacer_tarea(self, nombre_tarea, fecha_entrega):
        print(self.nombre+" dice haré "+nombre_tarea+ 'para el '+fecha_entrega)
    def trabajar(self,horas):
        ganado = horas*100
        print("He ganado: "+str(ganado))
        return ganado

hebert = robot("Herbert")
nicole = robot("Nic")
marcos = robot("Mac")

lista_robots = [hebert,nicole,marcos]
total =0
for r in lista_robots:
    r.camine("Kiosko")
    r.hacer_tarea("Tarea Calculo", " el miercoles" )
    total += r.trabajar(20)

print("Los robots ganaron: "+str(total))


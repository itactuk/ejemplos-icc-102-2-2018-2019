import pickle

x=65756
y=[1,2,3,4]

def guardar(nombre_archivo, variable):
    with open(nombre_archivo, 'wb') as archivo:
        pickle.dump(variable, archivo)

def leer_del_disco(nombre_archivo):
    with open(nombre_archivo, 'rb') as archivo:
        res = pickle.load(archivo)
    return res

# guardar('y.pkl',x)
x = leer_del_disco("y.pkl")
print(x)

import random

class ObjetoMochila:
    def __init__(self, nombre, costo, volumen):
        self.nombre = nombre
        self.costo = costo
        self.volumen = volumen
        self.contribucion = costo / volumen

def inicializar_parametros(objetos):
    volumen_maximo_permitido = sum(obj.volumen for obj in objetos) * (2 / 3)
    return volumen_maximo_permitido

def generar_mochilas_aleatorias(objetos, volumen_maximo_permitido, num_mochilas):
    mochilas = []
    for _ in range(num_mochilas):
        mochila = []
        volumen_actual = 0
        while volumen_actual < volumen_maximo_permitido:
            obj = random.choice(objetos)
            if volumen_actual + obj.volumen <= volumen_maximo_permitido:
                mochila.append(obj)
                volumen_actual += obj.volumen
        mochilas.append(mochila)
    return mochilas

def calcular_fuerza_mochilas(mochilas):
    for mochila in mochilas:
        fuerza_mochila = sum(obj.costo for obj in mochila) / sum(obj.volumen for obj in mochila)
        print("Fuerza de la mochila:", fuerza_mochila)

def torneo(mochilas):
    for i in range(len(mochilas) - 1):
        for j in range(i + 1, len(mochilas)):
            print(f"Mochila {i + 1} vs Mochila {j + 1}")
            if random.random() < 0.5:
                print(f"Gana Mochila {i + 1}")
            else:
                print(f"Gana Mochila {j + 1}")

def cambiar_objeto_mochila(mochila):
    menor_contribucion = min(mochila, key=lambda x: x.contribucion)
    mochila.remove(menor_contribucion)
    return mochila

def ejecutar_algoritmo_mochila(objetos, num_mochilas, num_fechas):
    volumen_maximo_permitido = inicializar_parametros(objetos)
    mochilas = generar_mochilas_aleatorias(objetos, volumen_maximo_permitido, num_mochilas)
    
    for fecha in range(num_fechas):
        print(f"Fecha {fecha + 1}:")
        print("Mochilas iniciales:")
        for i, mochila in enumerate(mochilas):
            print(f"Mochila {i + 1}: {[obj.nombre for obj in mochila]}")
        
        calcular_fuerza_mochilas(mochilas)
        torneo(mochilas)

        # Cambiar un objeto de cada mochila
        for mochila in mochilas:
            mochila = cambiar_objeto_mochila(mochila)
        
        print("Mochilas después de cambiar objetos:")
        for i, mochila in enumerate(mochilas):
            print(f"Mochila {i + 1}: {[obj.nombre for obj in mochila]}")

# Definir los objetos de la mochila con nombre, costo y volumen
objetos = [
    {"nombre": "Objeto 1", "costo": 12, "volumen": 24},
    {"nombre": "Objeto 2", "costo": 4, "volumen": 17},
    {"nombre": "Objeto 3", "costo": 8, "volumen": 3},
    {"nombre": "Objeto 4", "costo": 10, "volumen": 27},
    {"nombre": "Objeto 5", "costo": 7, "volumen": 16},
    {"nombre": "Objeto 6", "costo": 16, "volumen": 30},
    {"nombre": "Objeto 7", "costo": 1, "volumen": 7},
    {"nombre": "Objeto 8", "costo": 4, "volumen": 20},
    {"nombre": "Objeto 9", "costo": 30, "volumen": 4},
    {"nombre": "Objeto 10", "costo": 22, "volumen": 9},
    {"nombre": "Objeto 11", "costo": 23, "volumen": 10},
    {"nombre": "Objeto 12", "costo": 6, "volumen": 19},
    {"nombre": "Objeto 13", "costo": 20, "volumen": 28},
    {"nombre": "Objeto 14", "costo": 17, "volumen": 9},
    {"nombre": "Objeto 15", "costo": 28, "volumen": 10},
    {"nombre": "Objeto 16", "costo": 17, "volumen": 27},
    {"nombre": "Objeto 17", "costo": 24, "volumen": 19},
    {"nombre": "Objeto 18", "costo": 11, "volumen": 28},
    {"nombre": "Objeto 19", "costo": 11, "volumen": 7},
    {"nombre": "Objeto 20", "costo": 20, "volumen": 5},
    {"nombre": "Objeto 21", "costo": 6, "volumen": 13},
    {"nombre": "Objeto 22", "costo": 3, "volumen": 28},
    {"nombre": "Objeto 23", "costo": 25, "volumen": 25},
    {"nombre": "Objeto 24", "costo": 19, "volumen": 4},
    {"nombre": "Objeto 25", "costo": 21, "volumen": 12},
    {"nombre": "Objeto 26", "costo": 4, "volumen": 22},
    {"nombre": "Objeto 27", "costo": 1, "volumen": 27},
    {"nombre": "Objeto 28", "costo": 28, "volumen": 8},
    {"nombre": "Objeto 29", "costo": 22, "volumen": 2},
    {"nombre": "Objeto 30", "costo": 6, "volumen": 29}
]

# Convertir los objetos en instancias de la clase ObjetoMochila
objetos = [ObjetoMochila(obj["nombre"], obj["costo"], obj["volumen"]) for obj in objetos]

num_mochilas = 6
num_fechas = 5

# Ejecutar el algoritmo de la mochila LCA
ejecutar_algoritmo_mochila(objetos, num_mochilas, num_fechas)
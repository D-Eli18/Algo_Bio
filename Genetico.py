import random

def calcular_aptitud(individuo):
    
    return sum(individuo)

def seleccionar_padres(poblacion, aptitudes):
    total_aptitudes = sum(aptitudes)
    probabilidad_seleccion = [aptitud / total_aptitudes for aptitud in aptitudes]
    padre1 = random.choices(poblacion, weights=probabilidad_seleccion)[0]
    padre2 = random.choices(poblacion, weights=probabilidad_seleccion)[0]
    return padre1, padre2

def cruzar(padre1, padre2):
    punto_cruce = random.randint(1, len(padre1) - 1)
    hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
    hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
    return hijo1, hijo2

def mutar(individuo, probabilidad_mutacion):
    for i in range(len(individuo)):
        if random.random() < probabilidad_mutacion:
            individuo[i] = random.randint(0, 15)

num_individuos = 30
num_genes = 15
probabilidad_mutacion = 0.1
num_generaciones = 100

poblacion = [[random.randint(0, 15) for _ in range(num_genes)] for _ in range(num_individuos)]

for generacion in range(num_generaciones):

    aptitudes = [calcular_aptitud(individuo) for individuo in poblacion]

    padre1, padre2 = seleccionar_padres(poblacion, aptitudes)

    hijo1, hijo2 = cruzar(padre1, padre2)

    mutar(hijo1, probabilidad_mutacion)
    mutar(hijo2, probabilidad_mutacion)

    poblacion.sort(key=calcular_aptitud)
    poblacion[0] = hijo1
    poblacion[1] = hijo2

mejor_individuo = max(poblacion, key=calcular_aptitud)
print("Mejor individuo:", mejor_individuo)
print("Aptitud del mejor individuo:", calcular_aptitud(mejor_individuo))
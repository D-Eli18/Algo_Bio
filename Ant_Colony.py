import random
num_hormigas = 10
num_iteraciones = 100
feromona_inicial = 1.0
alfa = 1.0
beta = 2.0
evaporacion = 0.5
grafo = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

feromonas = [[feromona_inicial] * len(grafo) for _ in range(len(grafo))]

for _ in range(num_iteraciones):
    soluciones = []

    for _ in range(num_hormigas):
        nodo_actual = random.randint(0, len(grafo) - 1)
        ruta = [nodo_actual]

        while len(ruta) < len(grafo):
            probabilidades = []
            for j in range(len(grafo)):
                if j not in ruta:
                    denominador = 0
                    for k in range(len(grafo)):
                        if k not in ruta:
                            denominador += (feromonas[nodo_actual][k] ** alfa) * (1 / (grafo[nodo_actual][k] ** beta))
                    probabilidad = ((feromonas[nodo_actual][j] ** alfa) * (1 / (grafo[nodo_actual][j] ** beta))) / denominador
                    probabilidades.append((j, probabilidad))

            siguiente_nodo = max(probabilidades, key=lambda x: x[1])[0]
            ruta.append(siguiente_nodo)
            nodo_actual = siguiente_nodo

        soluciones.append((ruta, sum(grafo[i][j] for i, j in zip(ruta, ruta[1:] + [ruta[0]]))))

    for i in range(len(feromonas)):
        for j in range(len(feromonas[i])):
            feromonas[i][j] *= (1 - evaporacion)

    for ruta, costo in soluciones:
        for i in range(len(ruta) - 1):
            feromonas[ruta[i]][ruta[i + 1]] += (1 / costo)

mejor_solucion = min(soluciones, key=lambda x: x[1])
print("Mejor solución:", mejor_solucion)
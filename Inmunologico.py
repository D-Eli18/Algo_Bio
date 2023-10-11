import random

population_size = 20  # Población
generations = 100    # Num de generaciones
mutation_rate = 0.1  
selection_rate = 0.5 

def objective_function(solution):
    return sum(solution)

# Inicialización Pob
population = [[random.randint(0, 1) for _ in range(10)] for _ in range(population_size)]

for generation in range(generations):
    # Evaluación Pob
    fitness_values = [objective_function(individual) for individual in population]

    # Individuos para reproducción
    selected_population = []
    num_parents = int(population_size * selection_rate)

    for _ in range(num_parents):
        parent_index = fitness_values.index(min(fitness_values))
        selected_population.append(population[parent_index])
        # Marcar como no seleccionable
        fitness_values[parent_index] = float('inf')

    # Reproducción y mutación
    offspring_population = []
    for _ in range(population_size - num_parents):
        parent1 = random.choice(selected_population)
        parent2 = random.choice(selected_population)
        crossover_point = random.randint(0, len(parent1))

        child = parent1[:crossover_point] + parent2[crossover_point:]
        
        # Aplicar mutación
        for i in range(len(child)):
            if random.random() < mutation_rate:
                child[i] = 1 - child[i]

        offspring_population.append(child)

    # Reemplazar la población anterior
    population = selected_population + offspring_population

# Buscar la mejor solución
best_solution = min(population, key=objective_function)
best_fitness = objective_function(best_solution)

print("Mejor solución encontrada:", best_solution)
print("Valor de la función objetivo:", best_fitness)
import random
import math

def simulated_annealing(problem, T, T_min, alpha):
    current_solution = problem.initial_solution()
    current_cost = problem.calculate_cost(current_solution)
    best_solution = current_solution
    best_cost = current_cost

    while T > T_min:
        # Ciclo principal
        neighbor_solution = problem.get_neighbor(current_solution)
        neighbor_cost = problem.calculate_cost(neighbor_solution)
        cost_diff = neighbor_cost - current_cost

        if cost_diff < 0 or random.random() < math.exp(-cost_diff / T):
            current_solution = neighbor_solution
            current_cost = neighbor_cost

        if neighbor_cost < best_cost:
            best_solution = neighbor_solution
            best_cost = neighbor_cost

        # Reducción de la temp
        T *= alpha

    return best_solution, best_cost

#Problema de optimización
class OptimizationProblem:
    def initial_solution(self):
        return random.randint(0, 100)

    # Acercase a 50
    def calculate_cost(self, solution):
        return abs(solution - 50)

    def get_neighbor(self, solution):
        return solution + random.randint(-10, 10)

if __name__ == "__main__":
    initial_temperature = 1000
    min_temperature = 0.01
    cooling_rate = 0.95

    problem = OptimizationProblem()
    best_solution, best_cost = simulated_annealing(problem, initial_temperature, min_temperature, cooling_rate)

    print("Mejor solución encontrada:", best_solution)
    print("Costo de la mejor solución:", best_cost)

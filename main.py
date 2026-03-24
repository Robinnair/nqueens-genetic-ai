from ga import solve_n_queens,fitness
from visualization import visulaiser
history,solution=solve_n_queens(10,1000,2000)

print("Solution: ",solution)
if solution:
    print("Conflicts: ",fitness(solution))
    visulaiser(history)
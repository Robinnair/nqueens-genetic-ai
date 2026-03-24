from ga import solve_n_queens,fitness
from visualization import visualiser
solution=solve_n_queens(8)

print("Solution: ",solution)
if solution:
    print("Conflicts: ",fitness(solution))
    visualiser(solution)
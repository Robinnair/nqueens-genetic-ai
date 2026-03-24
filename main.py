from ga import solve_n_queens,fitness

solution=solve_n_queens(8)

print("Solution: ",solution)
if solution is not None:
    print("Conflicts: ",fitness(solution))
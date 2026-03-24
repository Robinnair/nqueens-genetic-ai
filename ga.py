import random

def fitness(board):
    conflicts=0
    n=len(board)

    for i in range(n):
        for j in range(i+1,n):
            if board[i]==board[j]:
                conflict+=1
            elif(abs(board[i]-board[j])==abs(i-j)):
                conflicts+=1
    return conflicts

def create_individuals(n):
    return [random.randint(0,n-1) for _ in range(n)]

def create_population(size,n):
    return [create_individuals(n) for _ in range(size)]

def tournament_selection(population,k=3):
    selected=[]
    for _ in range(len(population)//2):
        tournament=random.sample(population,k)
        winner=min(tournament,key=lambda x: fitness(x))
        selected.append(winner)
    return selected

def crossover(parent1,parent2):
    n=len(parent1)
    point=random.randint(0,n-1)
    child=parent1[:point]+parent2[point:]
    return child

def mutate(board,rate=0.1):
    if random.random()<rate:
        i=random.randint(0,len(board)-1)
        board[i]=random.randint(0,len(board)-1)
    return board

def solve_n_queens(n,population_size=100,generations=1000):
    population=create_population(population_size,n)

    for gen in range(generations):
        population=sorted(population,key=lambda x: fitness(x))
        best=population[0]
        print(f"Generation= {gen} |best fitness: {fitness(best)}")
        if fitness(best)==0:
            print("Solution is Found:\n")
            return best
        
        selected=tournament_selection(population)

        next_gen=[]

        while(len(next_gen)>population_size):
            p1=random.choice(selected)
            p2=random.choice(selected)

            child=crossover(p1,p2)
            child=mutate(child)
            next_gen.append(child)
        population=next_gen
    print("No Solution Found")
    return None
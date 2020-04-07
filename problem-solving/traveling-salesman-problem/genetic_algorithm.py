import random, math, graph

# Calculating and assigning fitness to every population
def assign_fitness(pop_list):
    for population in pop_list:
        population.fitness = 1 / graph.get_total_distance(population.nodes)

# Normalizing fitness means dividing all fitness values by the sum
def normalize_fitness(population):
    total_sum = 0
    for pop in population:
        total_sum += pop.fitness
    for pop in population:
        pop.fitness = pop.fitness / total_sum

# Assign values to items for next generation
def nextGen(population):
    for _ in range(len(population)):
        selected_item_01 = pool_selection(population)
        mutate(selected_item_01)

    return population

# Pool selection algorithm based on probabilities
def pool_selection(population):
    index = 0
    r = random.random()
    while r > 0:
        r = r - population[index].fitness
        index += 1
    index -= 1
    return population[index]

# Mutate method
def mutate(population):
    itemA = math.floor(random.randint(0, len(population.nodes)-1))
    itemB = math.floor(random.randint(0, len(population.nodes)-1))
    population.nodes[itemA], population.nodes[itemB] = population.nodes[itemB], population.nodes[itemA] 
    return population
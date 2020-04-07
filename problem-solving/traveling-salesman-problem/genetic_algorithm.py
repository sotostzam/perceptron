import random, math, graph

# Calculating and assigning fitness to every population
def assign_fitness(pop_list):
    for population in pop_list:
        eucl_dist = graph.get_total_distance(population.nodes)
        population.distance = eucl_dist
        population.fitness = 1 / eucl_dist

# Normalizing fitness means dividing all fitness values by the sum
def normalize_fitness(population):
    total_sum = 0
    for pop in population:
        total_sum += pop.fitness
    for pop in population:
        pop.fitness = pop.fitness / total_sum

# Assign values to items for next generation
def advance_generation(population):
    new_population = []
    for _ in range(len(population)):
        selected_parent_1 = pool_selection(population)
        selected_parent_2 = pool_selection(population)
        offspring = crossover(selected_parent_1, selected_parent_2)
        mutate(offspring, 0.01)
        new_population.append(offspring)
    return new_population

# Pool selection algorithm based on probabilities
def pool_selection(population):
    index = 0
    r = random.random()
    while r > 0:
        r = r - population[index].fitness
        index += 1
    index -= 1
    return population[index]

# Crossover method
def crossover(parent_1, parent_2):
    start_index = math.floor(random.randint(0, len(parent_1.nodes)-1))
    end_index = math.floor(random.randint(start_index, len(parent_1.nodes)-1))
    new_order = parent_1.nodes[start_index: end_index]
    while len(new_order) != len(parent_1.nodes):
        for node in parent_2.nodes:
            if node not in new_order:
                new_order.append(node)
    return graph.Population(new_order)

# Mutate method
def mutate(population, rate):
    for _ in range(len(population.nodes)):
        if random.random() < rate:
            itemA = math.floor(random.randint(0, len(population.nodes)-1))
            itemB = math.floor(random.randint(0, len(population.nodes)-1))
            population.nodes[itemA], population.nodes[itemB] = population.nodes[itemB], population.nodes[itemA] 
    return population

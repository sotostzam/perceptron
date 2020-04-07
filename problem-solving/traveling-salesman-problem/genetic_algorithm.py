import random, math
  
def normalize_fitness(population):
    total_sum = 0
    for pop in population:
        total_sum += pop.fitness
    for pop in population:
        pop.fitness = pop.fitness / total_sum

def nextGen(current_pop):
    pass
    #time.sleep(.05)
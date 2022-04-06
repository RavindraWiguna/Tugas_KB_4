from solution import Solution
import random as rd
# import numpy as np

def get_random_chromosome():
    '''return random chromosome for 8 queens (8 char)'''
    chromosome = []
    i = 0
    while i < 8:
        chromosome.append(rd.randint(0, 7))
        i+=1
    return chromosome

def generate_initial_population(n):
    '''n = total population (integer)'''
    population = []
    i = 0
    while i < n:
        random_chromosome = get_random_chromosome()
        individu = Solution(random_chromosome)
        population.append(individu)
        i+=1
    # return np.array(population)
    return population


def get_fitness(chromosome):
    total_kill = 0
    for i, gen in enumerate(chromosome):
        # gen = int(gen)
        t_kill = 0
        rel_id = 0
        # print(f'check: {gen}')
        while(i < 7):
            i+=1
            rel_id+=1
            # next_queen = int(chromosome[i])
            next_queen = chromosome[i]
            # check if same row
            if(next_queen == gen):
                t_kill+=1
                # print(f'{gen} same row with {next_queen} on {i}')
            # check if got positive diagonal
            elif(next_queen == gen-(rel_id)):
                t_kill+=1
                # print(f'{gen} positive diagonal {next_queen} on {i}')
            elif(next_queen == gen+(rel_id)):
                t_kill+=1
                # print(f'{gen} negative diagonal {next_queen} on {i}')

        total_kill -= t_kill
    
    # print(total_kill)
    return total_kill

def mutate_chromosome(chromosome):
    id_mutated_gen = rd.randint(0, 7)
    chromosome[id_mutated_gen] = rd.randint(0, 7)


def make_baby(father, mother, mutation_rate):
    fate = rd.getrandbits(8)
    child1 = []
    child2 = []
    # print(fate)
    bits = (1, 2, 4, 8, 16, 32, 64, 128)
    for i, bit in enumerate(bits):
        # print(fate&bit == bit)
        if(fate&bit == bit):
            # True then crossover
            child1.append(father[i])
            child2.append(mother[i])
        else:
            child1.append(mother[i])
            child2.append(father[i])
    
    # print(f'f: {father} | m: {mother}')
    mutate_1 = rd.uniform(0.0, 1.0)
    mutate_2 = rd.uniform(0.0, 1.0)
    if(mutate_1 < mutation_rate):
        mutate_chromosome(child1)
    if(mutate_2 < mutation_rate):
        mutate_chromosome(child2)
    
    return Solution(child1), Solution(child2)


def generate_next_population(parents, mutation_rate):
    total_parrent = len(parents)
    new_population = []
    for i, individu in enumerate(parents):
        i+=1
        while(i < total_parrent):
            offsprings = make_baby(individu.chromosome, parents[i].chromosome, mutation_rate)
            new_population.extend(offsprings)
            i+=1
    
    # print(new_population)
    print(f"Got new: {len(new_population)} invididuals")
    return new_population


if __name__=="__main__":
    sol = Solution([0, 2, 4, 6, 4, 2, 0, 2])
    # get_fitness(sol.chromosome)
    make_baby(get_random_chromosome(), get_random_chromosome())
    # generate_next_population(generate_initial_population(5))


# from solution import Solution
from utils import generate_initial_population, generate_next_population, get_fitness, visualize_chromosome, get_parameter


def main():
    print("8 Queens Baby :D")
    # generate populations
    start_individuals, pick_n_best, mutation_rate = get_parameter()
    current_population = generate_initial_population(start_individuals)
    # print(init_population)
    isReached = False
    generation = 0
    while(not isReached):
        for individu in current_population:
            individu.fitness = get_fitness(individu.chromosome)

        current_population.sort(reverse=True)

        # average(current_population)
        print(f'Finished Gen: {generation}| Best Individu: {current_population[0]}')
        generation+=1
        # isReached = True
        if(current_population[0].fitness > -1):
            print("Reached")
            isReached = True
        else:
            current_population = generate_next_population(current_population[0:pick_n_best], mutation_rate)

    visualize_chromosome(current_population[0].chromosome)

if __name__ =="__main__":
    main()
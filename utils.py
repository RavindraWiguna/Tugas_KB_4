from solution import Solution

def get_fitness(sol: Solution):
    total_kill = 0
    for i, gen in enumerate(sol.chromosome):
        gen = int(gen)
        t_kill = 0
        rel_id = 0
        # print(f'check: {gen}')
        while(i < 7):
            i+=1
            rel_id+=1
            next_queen = int(sol.chromosome[i])
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
    
    print(total_kill)

if __name__=="__main__":
    sol = Solution("02464202")
    get_fitness(sol)


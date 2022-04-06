class Solution:
    def __init__(self, chromosome) -> None:
        '''chromosome for 8 queens is the row location for the queen on each columns'''
        self.chromosome = chromosome
        self.fitness = 0
    
    def __eq__(self, other) -> bool:
        return self.chromosome == other.chromosome
    
    def __gt__(self, other):
        return self.fitness > other.fitness

    def __str__(self):
        return f'[{self.chromosome}: {self.fitness}]'
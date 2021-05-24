import random

import numpy as np
from baseoptimizer import BaseOptimizer
from individual import Individual


class DifferentialEvolution(BaseOptimizer):
    def __init__(self, fn, LB, UB, CR=0.9, F=0.8, seed=None):
        super().__init__(fn=fn, seed=seed)
        self.LB = LB
        self.UB = UB
        self.CR = CR
        self.F = F
        self.n_dim = None
            
    def cloning(self, population):
        return [Individual(individual.copy()) for individual in population]            
        
    def __call__(self, population):

        population = self.cloning(population)
        
        if self.n_dim is None:
            self.n_dim = len(population[0].x)

        popsize = len(population)

        for i_individual, individual in enumerate(population):

            agents = np.arange(len(population))
            agents = np.delete(agents, i_individual)
            agents = self.rng.choice(agents, size=3)

            x_agent_a = population[agents[0]].x
            x_agent_b = population[agents[1]].x
            x_agent_c = population[agents[2]].x

            random_index = self.rng.choice(agents, size=1)

            x = individual.x

            for i_dim in range(self.n_dim):
                if self.rng.uniform() < self.CR or i_dim == random_index:
                    x[i_dim] = x_agent_a[i_dim] + self.F * (
                        x_agent_b[i_dim] - x_agent_c[i_dim]
                    )
                    x[i_dim] = max(self.LB[i_dim], min(self.UB[i_dim], x[i_dim]))
                fn_x = self.fn(x)
                if fn_x < individual.fn_x:
                    individual.x = x
                    individual.fn_x = fn_x
        return population

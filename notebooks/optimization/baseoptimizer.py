import numpy as np
from individual import Individual

class BaseOptimizer:
    def __init__(self, fn, seed=None):
        
        self.fn = fn
        self.n_dim = None
        
        if seed is None:
            self.rng = np.random.default_rng()
        else:
            self.rng = np.random.default_rng(seed)  
            
    def random_direction(self):
        w = rng.uniform(low=-1, high=+1, size=self.n_dim)
        m = np.linalg.norm(w)
        return w / m
    
    def cloning(self, population):
        return [Individual(individual.copy())  for individual in population]

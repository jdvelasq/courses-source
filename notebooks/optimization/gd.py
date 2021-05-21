
import numpy as np

class GradientDescendent:
    def __init__(self, fn, learning_rate, delta_x=0.001):
        self.fn = fn
        self.delta_x = delta_x
        self.learning_rate = learning_rate
        
    def __call__(self, population):
        
        def gradient(individual):
            x = individual.x
            n_dim = len(x)
            gd = np.zeros(n_dim)
            fn_x = self.fn(x)
            for i_dim in range(n_dim):
                x_plus_delta = x.copy()
                x_plus_delta[i_dim] += self.delta_x
                fn_x_plus_delta = self.fn(x_plus_delta)
                gd[i_dim] = (fn_x_plus_delta - fn_x) / self.delta_x
            return gd

        
        for individual in population:
            gd = gradient(individual)
            individual.x = individual.x - self.learning_rate * gd
            individual.fn_x = self.fn(individual.x)

        return population
                
            
    

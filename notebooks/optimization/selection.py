from operator import itemgetter
import random

class SelectionBest:
    #
    # Selecciona los k mejores individuos de la población
    #
    def __init__(self, k, as_index=False):
        self.k = k
        self.as_index = as_index

    def __call__(self, population):
        idx = [(idx, individual.fn_x) for idx, individual in enumerate(population)]
        idx = sorted(idx, key=itemgetter(1), reverse=False)
        idx = [i for i, _ in idx]
        idx = idx[: self.k]
        if self.as_index is False:
            return [population[i] for i in idx]
        return idx

    
class SelectionWorst:
    #
    # Selecciona los k peores individuos de la población
    #
    def __init__(self, k, as_index=False):
        self.k = k
        self.as_index = as_index

    def __call__(self, population):
        
        idx = [(idx, individual.fn_x) for idx, individual in enumerate(population)]
        idx = sorted(idx, key=itemgetter(1), reverse=False)
        idx = [i for i, _ in idx]
        idx = idx[-self.k:]
        if self.as_index is False:
            return [population[i] for i in idx]    
        return idx

    
class SelectionRandom:
    #
    # Selecciona aleatoriamente k individuos de la población
    #
    def __init__(self, k, as_index=False):
        self.k = k
        self.as_index = as_index

    def __call__(self, population):
        index = list(range(len(population)))
        idx = random.choices(index, k=self.k)
        if self.as_index is False:
            return [population[i] for i in idx]        
        return idx
    
    
class SelectionTournament:
    def __init__(self, k, tournsize):
        self.k = k
        self.tournsize = tournsize
        
    def __call__(self, population):
        
        popsize = len(population)
        fitness = []
        
        for idx, individual in enumerate(population):
            
            oponents = list(range(popsize))
            oponents.remove(idx)
            oponents = random.choices(oponents, k=self.k)
            
            fn_x_values = [population[oponent].fn_x for oponent in oponents]
            fn_x = individual.fn_x
            winings = sum([0 if fn_x_value < fn_x else 1 for fn_x_value in fn_x_values])
            fitness.append((idx, winings))
            
        fitness = sorted(fitness, key=itemgetter(1), reverse=True)
        idx = [i  for i, _ in fitness]
        idx = idx[:self.k]
        return [population[i] for i in idx]
   
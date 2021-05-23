# import numpy as np
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

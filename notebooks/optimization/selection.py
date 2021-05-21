# import numpy as np
from operator import itemgetter

class BestK:
    def __init__(self, K):
        self.k = K

    def __call__(self, population):
        #
        # Selecciona los k mejores individuos de la población
        #
        idx = [(idx, individual.fn_x) for idx, individual in enumerate(population)]
        idx = sorted(idx, key=itemgetter(1), reverse=False)
        idx = [i for i, _ in idx]
        idx = idx[: self.k]
        return [population[i] for i in idx]


import numpy as np

class BaseOptimizer:
    def __init__(self, fn):
        self.fn = fn
        self.n_dim = None
    def random_direction(self):
        w = np.random.uniform(low=-1, high=+1, size=self.n_dim)
        m = np.linalg.norm(w)
        return w / m

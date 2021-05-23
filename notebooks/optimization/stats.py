import numpy as np
import matplotlib.pyplot as plt

class Statistics:
    def __init__(self):
        #
        # Estadísticos a almacenar por generación
        #
        self.avg = []
        self.std = []
        self.min = []
        self.max = []
        self.best = []
        self.worst = []
        self.x = []
        self.x_opt = None
        self.fn_opt = None

    def __call__(self, population):

        #
        # Evalua la función objetivo
        #
        fn_x = [individual.fn_x for individual in population]

        #
        # Cómputa los estadísticos para la población actual
        #
        self.avg.append(np.mean(fn_x))
        self.std.append(np.std(fn_x))
        self.min.append(np.min(fn_x))
        self.max.append(np.max(fn_x))
        
        self.best.append(np.min(self.min))
        self.worst.append(np.max(self.max))
        
        argmin = np.argmin(fn_x)
        self.x.append(population[argmin].x)
        
        if self.fn_opt is None or self.fn_opt < np.min(fn_x):
            self.fn_opt = np.min(fn_x)
            self.x_opt = population[argmin].x
        
    def plot(self, figsize=(10, 6)):
        
        fig = plt.figure(figsize=figsize)
        ax = fig.gca()
        n = list(range(len(self.avg)))
        plt.plot(n, self.worst, '--g', label='Worst',  alpha=0.6)
        plt.plot(n, self.best, '--r', label='Best',  alpha=0.6)
        plt.plot(n, self.min, '-k', label='Min',  alpha=1.0)
        plt.plot(n, self.max, '-k', label='Max',  alpha=1.0)
        plt.plot(n, self.avg, '-', c='blue', label='Avg',  alpha=1.0)
        plt.yscale('log')
        plt.legend()
        


from baseoptimizer import BaseOptimizer

class CoordinateSearch(BaseOptimizer):
    #
    # Propueto por Fermi y Metropolis en 1952. Fue diseñado
    # para solucionar sistemas complejos de ecuaciones en
    # fisica nuclear
    #
    def __init__(self, fn, delta=0.5):
        super().__init__(fn=fn)
        self.delta = delta

    def __call__(self, population):
         
        population = self.cloning(population)    
        
        #
        # Asume que ya fue evaluada la función objetivo 
        # para toda la población. Busca a lo largo de cada
        # eje hasta encontrar un punto mejor
        #
        for individual in population:
            
            if 'CS_delta' not in individual.keys():
                individual['CS_delta'] = self.delta
            
            x = individual.x
            fn_x = individual.fn_x
        
            for i_coordinate in range(len(x)):

                x_left = x.copy()
                x_left[i_coordinate] = x_left[i_coordinate] - individual.CS_delta
                fn_x_left = self.fn(x_left)

                x_right = x.copy()
                x_right[i_coordinate] = x_right[i_coordinate] + individual.CS_delta
                fn_x_right = self.fn(x_right)

                if fn_x_left > fn_x and fn_x < fn_x_right:

                    #
                    # Encontró un punto de minima entre
                    #  x_left y x_right
                    #
                    for n in range(20):

                        l = x_left + 0.382 * (x_right - x_left)
                        u = x_left + 0.618 * (x_right - x_left)

                        fl = self.fn(l)
                        fu = self.fn(u)

                        if fl > fu:
                            x_left = l
                            fn_x_left = fl
                        else:
                            x_right = u
                            fn_x_right = fu

                    
                    x_mean = 0.5 * (x_left + x_right)
                    fn_x_mean = self.fn(x_mean)
                    
                    if fn_x_left < fn_x:
                        x = x_left
                        fn_x = fn_x_left
                        
                    if fn_x_right < fn_x:
                        x = x_right
                        fn_x = fn_x_right
                        
                    if fn_x_mean < fn_x:
                        x = x_mean
                        fn_x = fn_x_mean
                    

                else:

                    #
                    # El punto de mínima está en uno de los extremos
                    #
                    if fn_x_left < fn_x:
                        x = x_left
                        fn_x = fn_x_left
                    if fn_x_right < fn_x:
                        x = x_right
                        fn_x = fn_x_right
                        
            individual.x = x
            individual.fn_x = fn_x

        return population

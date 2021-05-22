
from baseoptimizer import BaseOptimizer

class BacterialChemotaxis(BaseOptimizer):
    #
    # Propuesto por Muller, Airgahi, Marchetto y Koumoustsakos
    # en el año 2000. Es un algoritmo de búsqueda local 
    # elitista. Se base en la imitación de como las bacterias
    # son atraidas a los mejores ambientes (a nivel macro)
    # y con el comportamiento de las colonias a nivel micro.
    #
    def __init__(self, fn, rho=0.5):
        super().__init__(fn=fn)
        #
        # tamaño del avance
        #
        self.rho = rho

    def __call__(self, population):

        if self.n_dim is None:
            self.n_dim = len(population[0].x)
        
        for individual in population:
                    
            x_base = individual.x.copy()
            fn_x_base = individual.fn_x

            #
            # Genera un vector con dirección aleatoria
            # y radio rho
            #
            v = self.rho * self.random_direction()

            while True:

                #
                # Avanza en la dirección aleatoria. Si 
                # fn(x) mejora se continua avanzando 
                # en esa misma dirección
                #
                x = x_base + v
                fn_x = self.fn(x)

                if fn_x < fn_x_base:
                    x_base = x
                    fn_x_base = fn_x
                else:
                    break
                    
            individual.x = x_base.copy()
            individual.fn_x = fn_x_base

        return population

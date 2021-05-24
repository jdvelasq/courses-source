
class FnEvaluator:
    def __init__(self, fn, decoder=None):
        self.fn = fn
        self.decoder = decoder

    def __call__(self, population):
        #
        # Evalua la función objetivo
        #
        if self.decoder is not None:
            for individual in population:
                if individual.fn_x is None:
                    x = self.decoder(individual.x)
                    individual.fn_x = self.fn(x)
        else:            
            for individual in population:
                if individual.fn_x is None:
                    individual.fn_x = self.fn(individual.x)

        return population

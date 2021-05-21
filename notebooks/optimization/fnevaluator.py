
class FnEvaluator:
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, population):
        #
        # Evalua la función objetivo
        #
        for individual in population:
            if individual.fn_x is None:
                individual.fn_x = self.fn(individual.x)

        return population

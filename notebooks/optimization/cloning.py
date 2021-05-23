#


class Cloning:
    def __call__(self, population, idx=None):

        if idx is None:
            idx = list(range(len(population)))

        clones = [Individual() for _ in idx]

        for clon, individual in zip(clones, population):
            for k in individual.keys():
                clon[k] = individual[k].copy()

        return clones
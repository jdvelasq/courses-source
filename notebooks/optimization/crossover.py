import numpy as np
from individual import Individual


class CrossoverUniform:
    def __init__(self, probability=0.5, both=False):
        self.probability = probability
        self.both=both
        
    def __call__(self, parent1, parent2):

        n_dim = len(parent1[0].x)
        n_offsprings = len(parent1)

        rand = [
            np.random.uniform(size=n_dim)
            for _ in range(len(parent1))
        ]

        offsprings1 = [
            Individual(
                {
                    "x": np.where(rnd < self.probability, p1.x, p2.x),
                    "fn_x": None,
                }
            )
            for rnd, p1, p2 in zip(rand, parent1, parent2)
        ]
        
        offsprings2 = [
            Individual(
                {
                    "x": np.where(rnd < self.probability, p2.x, p1.x),
                    "fn_x": None,
                }
            )
            for rnd, p1, p2 in zip(rand, parent1, parent2)
        ]
        
        if "ES_sigma" in parent1[0].keys() and isinstance(parent1[0].ES_sigma, (int, float)):
            
            rand = [np.random.uniform() for _ in range(len(parent1))]
            
            for r, o1, o2, p1, p2 in zip(rand, offsprings1, offsprings2, parent1, parent2):
                
                if r < self.probability:
                    o1['ES_sigma'] = p2.ES_sigma
                    o2['ES_sigma'] = p1.ES_sigma
                else:
                    o1['ES_sigma'] = p1.ES_sigma
                    o2['ES_sigma'] = p2.ES_sigma
            
        if "ES_sigma" in parent1[0].keys() and not isinstance(parent1[0].ES_sigma, (int, float)):
            
            rand = [
                np.random.uniform(size=n_dim)
                for _ in range(len(parent1))
            ]
            
            for r, o1, o2, p1, p2 in zip(rand, offsprings1, offsprings2, parent1, parent2):
                
                o1['ES_sigma'] = np.where(r < self.probability, p1.ES_sigma, p2.ES_sigma)
                o2['ES_sigma'] = np.where(r < self.probability, p2.ES_sigma, p1.ES_sigma)
                
                
        if self.both is True:
            return offsprings1 + offsprings2
        
        return [ o1 if np.random.uniform() < 0.5 else o2   for o1, o2 in zip(offsprings1, offsprings2)]


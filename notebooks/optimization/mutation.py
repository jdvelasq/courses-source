import numpy as np


class MutationGaussianES:
    def __init__(
        self,
        probability=1.0,
        sigma_min=0.01,
        sigma_max=10,
    ):
        self.probability = probability
        self.sigma_min = sigma_min
        self.sigma_max = sigma_max

    def __call__(self, population):

        #
        # Número de dimensiones
        #
        n_dim = len(population[0].x)

        #
        # Constante definida por el algoritmo
        #
        tau = 1.0 / np.power(2.0, 1.0 / n_dim)

        if "ES_sigma" in population[0].keys():

            if isinstance(population[0].ES_sigma, (int, float)):
                #
                # El individuo tienen un solo parámetro de
                #  estrategia int o float
                #
                for individual in population:
                    #
                    # Primero se muta el parámetro de
                    #  estrategia
                    #
                    if np.random.uniform() < self.probability:
                        individual.ES_sigma = np.max(
                            self.sigma_min,
                            np.min(
                                self.sigma_max,
                                individual.ES_sigma * np.exp(tau * np.random.normal()),
                            ),
                        )

                    #
                    # Luego se mutan las variables x del problema
                    #
                    if np.random.uniform() < self.probability:
                        individual.x = (
                            individual.x
                            + individual.ES_sigma * np.random.normal(size=n_dim)
                        )
            else:
                #
                # El individuo tiene un vector de sigmas, una
                # por cada dimensión del vector x.
                #
                for individual in population:
                    #
                    # Muta los parámetros de estrategia
                    #
                    individual.ES_sigma = individual.ES_sigma * np.exp(
                        tau * np.random.normal(size=n_dim)
                    )
                    individual.ES_sigma = np.where(
                        individual.ES_sigma < self.sigma_max,
                        individual.ES_sigma,
                        self.sigma_max,
                    )
                    individual.ES_sigma = np.where(
                        individual.ES_sigma > self.sigma_min,
                        individual.ES_sigma,
                        self.sigma_min,
                    )
                    #
                    # Luego muta las x con los nuevos sigmas
                    #
                    individual.x = (
                        individual.x
                        + individual.ES_sigma * np.random.normal(size=n_dim)
                    )

        return population
    
    
class MutationGaussianEP:
    def __init__(
        self,
        alpha=0.2,
        probability=1.0,
        sigma_min=0.01,
        sigma_max=10,
    ):
        self.alpha = float(alpha)
        self.probability = float(probability)
        self.sigma_min = float(sigma_min)
        self.sigma_max = float(sigma_max)

    def __call__(self, population):

        #
        # Número de dimensiones
        #
        n_dim = len(population[0].x)

        if "EP_sigma" in population[0].keys():

            if isinstance(population[0].EP_sigma, (int, float)):
                #
                # El individuo tienen un solo parámetro de
                # estrategia int o float
                #
                for individual in population:
                    #
                    # Primero se muta el parámetro de
                    # estrategia
                    #
                    if np.random.uniform() < self.probability:
                        individual.EP_sigma = max(
                            self.sigma_min,
                            min(
                                self.sigma_max,
                                individual.EP_sigma * (1.0 + self.alpha * np.random.normal()),
                            ),
                        )

                    #
                    # Luego se mutan las variables x del problema
                    #
                    if np.random.uniform() < self.probability:
                        individual.x = (
                            individual.x
                            + individual.EP_sigma * np.random.normal(size=n_dim)
                        )
            else:
                #
                # El individuo tiene un vector de sigmas, una
                # por cada dimensión del vector x.
                #
                for individual in population:
                    #
                    # Muta los parámetros de estrategia
                    #
                    individual.EP_sigma = individual.EP_sigma * (
                        1.0 + self.alpha * np.random.normal(size=n_dim)
                    )
                    individual.EP_sigma = np.where(
                        individual.EP_sigma < self.sigma_max,
                        individual.EP_sigma,
                        self.sigma_max,
                    )
                    individual.EP_sigma = np.where(
                        individual.EP_sigma > self.sigma_min,
                        individual.EP_sigma,
                        self.sigma_min,
                    )
                    #
                    # Luego muta las x con los nuevos sigmas
                    #
                    individual.x = (
                        individual.x
                        + individual.EP_sigma * np.random.normal(size=n_dim)
                    )

        return population

    

class MutationFlipBit:
    def __init__(self, probability):
        self.probability = probability
        self.n_dim = None
        
    def __call__(self, population):
        
        if self.n_dim is None:
            self.n_dim = len(population[0].x)
        
        for individual in population:
            individual.x = np.where(np.random.uniform() <= self.probability, 1 - individual.x, individual.x)
            
        return population
import numpy as np
from baseoptimizer import BaseOptimizer
from selection import SelectionBest


class ParticleSwarmOptimization(BaseOptimizer):
    def __init__(
        self,
        fn,
        init_velocity=0.5,
        omega=0.9,
        phi_local=0.5,
        phi_global=0.5,
    ):
        super().__init__(fn=fn)
        self.n_dim = None
        self.best_global = None
        self.Best = SelectionBest(k=1)
        self.init_velocity = init_velocity
        self.omega = omega
        self.phi_local = phi_local
        self.phi_global = phi_global

    def __call__(self, population):

        if self.n_dim is None:
            self.n_dim = len(population[0].x)

        if self.best_global is None:
            best_solution = self.Best(population)[0]
            self.best_global = best_solution

        if "best_local_x" not in population[0].keys():

            for individual in population:
                individual.best_local_x = individual.x
                individual.best_local_fn_x = individual.fn_x

        if "velocity" not in population[0].keys():
            for individual in population:
                individual.velocity = [self.init_velocity] * self.n_dim

        for individual in population:

            for i_dim in range(self.n_dim):

                #
                # Actualiza todas las velocidades
                #
                r_best_local = np.random.uniform()
                r_best_global = np.random.uniform()

                individual.velocity[i_dim] = (
                    self.omega * individual.velocity[i_dim]
                    + self.phi_local
                    * r_best_local
                    * (individual.best_local_x[i_dim] - individual.x[i_dim])
                    + self.phi_global
                    * r_best_global
                    * (self.best_global.x[i_dim] - individual.x[i_dim])
                )

            for i_dim in range(self.n_dim):
                #
                # Actualiza la posición de la particula
                #
                individual.x[i_dim] += individual.velocity[i_dim]

            #
            # Evalua el individuo actual y actualiza el mejor
            # punto local conocido
            #
            fn_x = self.fn(individual.x)

            if fn_x < individual.best_local_fn_x:
                individual.best_local_x = individual.x
                individual.best_local_fn_x = individual.fn_x
                
            if fn_x < self.best_global.fn_x:
                self.best_global = individual

                
        return population

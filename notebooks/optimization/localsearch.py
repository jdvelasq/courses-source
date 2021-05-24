
from baseoptimizer import BaseOptimizer

class LocalSearch(BaseOptimizer):
    #
    # Desarrollada por Hooke & Jeeves en 1962. Combina la
    # búsqueda lineal con la explotación de las direcciones
    # encontradas.
    #
    def __init__(self, fn, delta0=0.5, reduction_factor=0.9):
        super().__init__(fn=fn)
        self.delta0 = delta0
        self.reduction_factor = reduction_factor

    def __call__(self, population):

        population = self.cloning(population)    
        
        #
        # Asume que ya fue evaluada la función objetivo 
        # para toda la población. Busca a lo largo de cada
        # eje hasta encontrar un punto mejor y luego toma
        # tomar una dirección diagonal para avanzar.
        #
        
        for individual in population:
            
            if 'LS_delta' not in individual.keys():
                individual['LS_delta'] = self.delta0
                
            x_base = individual.x.copy()
            fn_x_base = individual.fn_x
            x = x_base.copy()
            fn_x = fn_x_base

            for i_coordinate in range(len(x)):

                x_left = x.copy()
                x_left[i_coordinate] = x_left[i_coordinate] - individual.LS_delta
                fn_x_left = self.fn(x_left)

                if fn_x_left < fn_x:
                    x = x_left
                    fn_x = fn_x_left
                else:
                    x_right = x.copy()
                    x_right[i_coordinate] = x_right[i_coordinate] + individual.LS_delta
                    fn_x_right = self.fn(x_right)

                    if fn_x_right < fn_x:
                        x = x_right
                        fn_x = fn_x_right

            #
            # En este punto  x y fn(x) son los puntos más
            # bajos encontrados usando un ciclo de búsqueda
            # por coordenadas. Intenta avanzar en la 
            # dirección de descenso encontrada.
            #
            x_next = 2 * x - x_base
            fn_x_next = self.fn(x_next)

            #
            # Si el nuevo punto es más bajo actualiza x y
            # fn(x)
            #
            if fn_x_next < fn_x:
                x = x_next
                fn_x = fn_x_next
             
            #
            # Verifica si el ciclo permitio encontrar un
            # punto más bajo. Si no lo encuentra, reduce el
            # valor del delta de las coordenadas cíclicas
            #
            if fn_x < fn_x_base:
                individual.x = x
                individual.fn_x = fn_x
            else:
                individual.LS_delta *= self.reduction_factor

        return population

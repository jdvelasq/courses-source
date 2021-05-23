class Individual(dict):
    #
    # Este es básicamente un diccionario cuyas
    # claves pueden accederse como propiedades
    #
    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, attr, value):
        self[attr] = value

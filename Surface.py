from Unit import Unit


class Surface(Unit):
    def __init__(self, id: int, name = "Surface"):
        super().__init__(id, name)
        self.__name = name
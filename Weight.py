from Unit import Unit


class Weight(Unit):
    def __init__(self, id: int, multiplier: float, name="Weight"):
        super().__init__(id, name)
        self.__multiplier = multiplier

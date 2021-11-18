from Ratio import Ratio
from Unit import Unit



class UnitRatio(Ratio):
    def __init__(self, id: int, unit1: Unit, unit2: Unit, name: str = "Unit Ratio"):
        super().__init__(id, name = name)

        self.__unit1 = unit1
        self.__unit2 = unit2

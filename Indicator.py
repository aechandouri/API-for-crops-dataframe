from IndicatorGroup import IndicatorGroup
from Unit import Unit
from Describable import Describable

class Indicator(Describable):

    def __init__(self, id: int, frequency: int, freqDesc: str, geogLocation: str, indicatorGroup: IndicatorGroup, unit: Unit, name: str):
        self.id = id
        self.unit = unit
        self.indicatorGroup = indicatorGroup
        self.__frequency = frequency
        self.__frequencyDesc = freqDesc
        self.__geogLocation = geogLocation
        self.name = name

    def describe(self):
        return f'Geography : {self.__geogLocation}\n\tIndicator : {self.name} ({self.indicatorGroup.name})'

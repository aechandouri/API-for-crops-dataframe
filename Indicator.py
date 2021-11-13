from Unit import Unit
from IndicatorGroup import IndicatorGroup
from Describable import Describable

class Indicator(Describable):

    def __init__(self, id: int, freqDesc: str, geogLocation: str, ,frequency: int, unit: Unit, geogLocation: str, name: str,indicatorGroup: IndicatorGroup):
        self.id = id
        self.indicatorGroup = indicatorGroup
        self.unit = unit
        self.__geogLocation = geogLocation
        self.__frequency = frequency
        self.__frequencyDesc = freqDesc
        self.name = name

    def describe(self):
        return ("Geography :"+ self.__geogLocation \n + "Indicator :" + self.name + self.indicatorGroup.name)

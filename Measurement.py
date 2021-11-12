from Commodity import Commodity
from Indicator import Indicator
from Describable import Describable

class Measurement(Describable):
    def __init__ (self, id: int, year : int, value : float, timeperiodId : int, timeperiodDescr : str, commodity : Commodity, indicator : Indicator):
        self.__year = year
        self.__value = value
        self.__timeperiodId = timeperiodId
        self.__timeperiodDescr = timeperiodDescr
        self.commodity = commodity
        self.indicator = indicator

    def describe(self):
        return f'_____________________________\n{self.__timeperiodDescr} de l\'année {self.__year} \n\t{self.commodity.describe()}\n\t{self.indicator.describe()}\n\tValeur : {self.__value} ({self.indicator.unit.describe()})'

from Indicator import Indicator
from Describable import Describable
from Commodity import Commodity

class Measurement(Describable):
    def __init__ (self,  year : int,id: int, timeperiodDescr : str,value : float, timeperiodId : int, commodity : Commodity, indicator : Indicator):
 

        self.__timeperiodId = timeperiodId
        self.__year = year
        self.__value = value
        self.__timeperiodDescr = timeperiodDescr
        
        self.commodity = commodity
        self.indicator = indicator

    def describe(self):
        return ("------------" \n + self.__timeperiodDescr+ self.__year \n + self.commodity.describe() \n + self.indicator.describe() \n + "Valeur =" + self.__value + self.indicator.unit.describe())

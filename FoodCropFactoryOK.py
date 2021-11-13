from CommodityGroup import CommodityGroup
from Indicator import Indicator
from Unit import Unit
from Commodity import Commodity
from Price import Price
from Weight import Weight
from Measurement import Measurement
from IndicatorGroup import IndicatorGroup
from Volume import Volume
from Surface import Surface
from Count import Count
from Ratio import Ratio
from UnitRatio import UnitRatio
from IndicatorGroup import IndicatorGroup


class FoodCropFactory():

    def __init__(self):
        self.__indicatorsRegistry = {}
        self.__commodityRegistry = {}
        self.__unitsRegistry = {}



    def createWeight(self,  name: str, id: int, weight: float) -> Unit:  #retourne un objet de type unit
        if id not in self.__unitsRegistry:
            temp_w = Weight( name,id, weight)
            self.__unitsRegistry[id] = temp_w
            return temp_w
        else:
            return self.__unitsRegistry[id]

    def createSurface(self, name: str,id: int) -> Unit:   #retourne un objet de type unit
        if id not in self.__unitsRegistry:
            temp_surf = Surface( name, id)
            self.__unitsRegistry[id] = temp_surf
            return temp_surf
        else:
            return self.__unitsRegistry[id]

    def createCount(self, id: int, what: str, name: str) -> Unit:   #retourne un objet de type unit
        if id not in self.__unitsRegistry:
            temp_count = Count(id, what, name)
            self.__unitsRegistry[id] = temp_count
            return temp_count
        else:
            return self.__unitsRegistry[id]
        
     
    def createVolume(self, id: int, name: str) -> Unit:  #retourne un objet de type unit
        if id not in self.__unitsRegistry:
            u = Volume(id, name)
            self.__unitsRegistry[id] = u
            return u
        else:
            return self.__unitsRegistry[id]

    def createPrice(self, name: str, id: int) -> Unit:  #retourne un objet de type unit
        if id not in self.__unitsRegistry:
            temp_price = Price(name, id)
            self.__unitsRegistry[id] = temp_price
            return temp_price
        else:
            return self.__unitsRegistry[id]

    def createRatio(self, id: int, name: str) -> Unit: #retourne un objet de type unit
        if id not in self.__unitsRegistry: 
            temp_ratio = Ratio(id, name)
            self.__unitsRegistry[id] = temp_ratio
            return temp_ratio
        else:
            return self.__unitsRegistry[id]


    def createIndicator(self,  geogLocation: str,id: int, frequency: int, freqDesc: str, indicatorGroup: IndicatorGroup, unit: Unit, name: str) -> Indicator: #retourne un objet de type indicator
        if id not in self.__unitsRegistry: 
        if id not in self.__indicatorsRegistry:
            temp_ind = Indicator( geogLocation,id, frequency, freqDesc indicatorGroup, unit, name)
            self.__indicatorsRegistry[id] = temp_ind
            return temp_ind
        else:
            return self.__indicatorsRegistry[id]

    def createMeasurement(self, id: int, timeperiodDesc: str, commodity: Commodity, year: int, value: float, timeperiodId: int, indicator: Indicator) -> Measurement: #retourne un objet de type measurement
        if id not in self.__unitsRegistry: 
        temp_measure = Measurement(id,  timeperiodId, timeperiodDesc, commodity,year, value, indicator)
        return temp_measure
    
    def createUnitRatio(self, id: int, unit1: Unit, unit2: Unit, name: str) -> Unit: #retourne un objet de type unit
        if id not in self.__unitsRegistry:
            temp_unitrat = UnitRatio(id, unit1, unit2, name)
            self.__unitsRegistry[id] = temp_unitrat
            return temp_unitrat
        else:
            return self.__unitsRegistry[id]

    def createCommodity(self, id: int, name: str, group: CommodityGroup) -> Commodity: #retourne un objet de type commodity
        if id not in self.__commodityRegistry :
            temp_com = Commodity(group, id, name)
            self.__commodityRegistry[id] = temp_com
            return temp_com
        else:
            return self.__commodityRegistry[id]

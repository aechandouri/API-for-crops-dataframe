from CommodityGroup import CommodityGroup
from Describable import Describable

class Commodity(Describable):

    def __init__(self,  name: str,group: CommodityGroup, id: int):
        self.id = id
        self.__name = name
        self.group = group
        

    def describe(self):
        return "Commodity :" + self.__name + self.group.name

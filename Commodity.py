from CommodityGroup import CommodityGroup
from Describable import Describable

class Commodity(Describable):

    def __init__(self, group: CommodityGroup, id: int, name: str):
        self.id = id
        self.group = group
        self.__name = name

    def describe(self):
        return f'Commodity : {self.__name} ({self.group.name})'

from Describable import Describable

class Unit(Describable):
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def describe(self):
        return f'{self.name}'

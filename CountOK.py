from Unit import Unit


class Count(Unit):
    def __init__(self, what: str, id: int, name = "Count"):
        self.__what = what
        super().__init__(id, name)
        

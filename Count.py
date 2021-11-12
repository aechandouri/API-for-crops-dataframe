from Unit import Unit


class Count(Unit):
    def __init__(self, id: int, what: str, name = "Count"):
        super().__init__(id, name)
        self.__what = what

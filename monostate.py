class StringReprMixin:
    def __str__(self):
        params = [f"{k}={v}" for k, v in self.__dict__.items()]
        return f"{self.__class__.__name__}({', '.join(params)})"

    def __repr__(self):
        return self.__str__()


class Monostate:
    _state = {}

    def __init__(self):
        self.__dict__ = self._state


a = StringReprMixin()
a.name = "Hello"
a.surname = "world"
print(a)
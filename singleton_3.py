class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        
        return cls._instances[cls]


class Person(metaclass=Singleton):
    def __init__(self):
        self.name = "Jane"


p1 = Person()
p1.name = "Martha"
p2 = Person()
print(p2.name)
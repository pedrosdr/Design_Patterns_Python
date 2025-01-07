def singleton(cls):
    instances = {}

    def get_cls(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    
    return get_cls


@singleton
class A:
    def __init__(self):
        self.theme = "light"


a1 = A()
a1.theme = "dark"

a2 = A()
print(a2.theme)


@singleton
class B:
    def __init__(self):
        self.font = "Sans"


b1 = B()
b1.font = "Serif"

b2 = B()
print(b2.font)
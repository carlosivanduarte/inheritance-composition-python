class Super:
    def __init__(self):
        self.supvar = 11


class Sub(Super):
    def __init__(self):
        super().__init__()
        self.supvar = 12


object = Sub()
print(object.supvar)
print(object.supvar)


class Super1:
    def __init__(self):
        self.supvar = 11


class Sub1(Super1):
    def __init__(self):
        super().__init__()
        self.subvar = 12


object2 = Sub1()
print(object2.subvar)
print(object2.supvar)
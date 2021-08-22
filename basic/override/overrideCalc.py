class Cal(object):
    def __init__(self, v1):
        self.value = v1

    def info(self):
        return "Calcurator"

class CalChild(Cal):
    def info(self):
        return "Calcurator Child"


class CalNoArg(object):
    def info(self):
        return "this class has no arguments"

c1 = Cal(1)
print(c1.info())

c2 = CalChild(10)
print(c2.info())

c3 = CalNoArg()
print(c3.info())
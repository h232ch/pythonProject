class Cal(object):
    def __init__(self, v1, v2):
        if isinstance((v1 and v2), int):
            self.v1 = v1
            self.v2 = v2
    def add(self):
        return self.v1+self.v2
    def sub(self):
        return self.v1-self.v2

class Multi(Cal):
    def multiply(self):
        return self.v1*self.v2

class Div(Cal):
    def division(self):
        return self.v1/self.v2


c1 = Multi(45, 34)
print(c1, c1.multiply())
print(c1, c1.add())
print(c1, c1.sub())

c2 = Div(56, 5)
print(c2, c2.division())
print(c2, c2.add())
print(c2, c2.sub())
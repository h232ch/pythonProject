
class Cal(object):
    _history = [] # class member variable
    def __init__(self, v1, v2):
        if isinstance((v1 and v2), int):
            self.v1 = v1
            self.v2 = v2
    def add(self):
        Cal._history.append(self.__str__() + " add : %d+%d=%d" % (self.v1, self.v2, self.v1+self.v2))
        return self.v1+self.v2
    def sub(self):
        Cal._history.append(self.__str__() + " sub : %d-%d=%d" % (self.v1, self.v2, self.v1-self.v2))
        return self.v1-self.v2

    @classmethod
    def history(cls):
        for item in Cal._history:
            print(item)

c1 = Cal(50, 60)
print(c1, c1.add())
print(c1, c1.sub())
print(c1, c1.add())
c1.history()

c2 = Cal(10, 6)
print(c2, c2.add())
print(c2, c2.sub())
print(c2, c2.add())
c2.history()
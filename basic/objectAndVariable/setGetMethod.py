
class C(object):
    def __init__(self, v):
        self.value = v # 외부 설정 가능 (외부에서 값 변경 가능)
        self.__value = v # 외부 설정 불가 (내부 메서드를 통해서 설정)
    def show(self):
        print(self.value)
        print(self.__value)
    def getValue(self):
        return self.value
    def setValue(self, v):
        if isinstance(v, int): # True/False return
            self.value = v
            self.__value = v
        else:
            print("input type error.")

c1 = C(10)
print(c1.getValue())
c1.setValue(20)
print(c1.getValue())

c1.setValue('one')
print(c1.getValue())

c1.setValue(50)
c1.value = 20
print(c1.show())
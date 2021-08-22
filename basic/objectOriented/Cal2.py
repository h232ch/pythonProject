
class Cal2(object): # object 형태를 받는다
    def __init__(self, v1, v2): # 셀프는 인스턴스 객체 자신을 가르킴 (생성자)
        self.v1 = v1
        self.v2 = v2
    def add(self): # 인스턴스 변수를 사용하고자 한다면 self를 붙여야 함
        return self.v1+self.v2
    def sub(self):
        return self.v1-self.v2

c1 = Cal2(10, 20)
print(c1.add())
print(c1.sub())
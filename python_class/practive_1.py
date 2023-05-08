class HCN():
    def __init__(self, dai, rong) -> None:
        self.dai = dai
        self.rong = rong
    
    def chuvi(self):
        return 2*(self.dai + self.rong)

a = HCN(10, 5)
print(a.chuvi())
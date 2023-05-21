class SieuNhan:
    suc_manh = 50
    def __init__(self, ten) -> None:
        self.ten = ten

class SieuNhanGao(SieuNhan):
    def __init__(self, ten, type):
        super().__init__(ten)
        self.type = type


A = SieuNhanGao('do', 'nam')
print(A.suc_manh)
print(A.ten)
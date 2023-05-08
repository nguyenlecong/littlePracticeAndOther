class SieuNhan:
    suc_manh = 50
    def __init__(self, ten) -> None:
        self.ten = ten

    @property  # getter
    def in_ten(self):
        print('ten toi la', self.ten)

    @in_ten.setter
    def in_ten(self, ten_moi):
        self.ten = ten_moi

    @in_ten.deleter
    def in_ten(self):
        self.ten = None

A = SieuNhan('do')
A.in_ten

A.ten = 'xanh'
A.in_ten

del A.in_ten
A.in_ten
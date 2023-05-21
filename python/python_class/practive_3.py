class SieuNhan:
    suc_manh = 50
    def __init__(self, ten) -> None:
        self.ten = ten

    @classmethod
    def cap_nhat_suc_manh(cls, smanh):
        cls.suc_manh = smanh
    
    @staticmethod
    def bien_hinh():
        print('bien hinh')

A = SieuNhan('a')

print(SieuNhan.suc_manh)
print(A.suc_manh)

SieuNhan.cap_nhat_suc_manh(40)

print(SieuNhan.suc_manh)
print(A.suc_manh)

A.cap_nhat_suc_manh(44)
print(SieuNhan.suc_manh)
print(A.suc_manh)

A.bien_hinh()
SieuNhan.bien_hinh()
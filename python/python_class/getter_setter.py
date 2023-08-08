class SieuNhan:
    suc_manh = 50

    def __init__(self, ten) -> None:
        self.ten = ten

    @property  # getter # trở thành một thuộc tính (property~thuoc tinh)
    def in_ten(self):
        print('ten toi la', self.ten)

    @in_ten.setter  # Bản chất là một phương thức, không thể gán ngang cho một giá trị -> setter
    def in_ten(self, ten_moi):
        self.ten = ten_moi

    @in_ten.deleter  # Nếu bạn muốn dùng xong xóa
    def in_ten(self):
        self.ten = None


A = SieuNhan('do')
A.in_ten

A.in_ten = 'xanh'
A.in_ten

del A.in_ten
A.in_ten

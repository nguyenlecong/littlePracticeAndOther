def UCLN(a,b):
    if a>b:
        i = b
    else:
        i = a
    
    while a%i!=0 or b%i!=0:
        i -= 1
    
    return i

class PHANSO():
    def __init__(self, tuso, mauso) -> None:
        self.tuso = tuso
        self.mauso = mauso
        self.ktra = True
        if self.mauso == 0:
            print('mau so khong phu hop')
            self.ktra = False
    def in_phanso(self):
        if not self.ktra:
            return
        
        print(self.tuso,'/',self.mauso)
    def rutgon(self):
        if not self.ktra:
            return
        
        x = UCLN(self.tuso, self.mauso)
        self.tuso//=x
        self.mauso//=x

ps = PHANSO(10,0)
ps.in_phanso()
ps.rutgon()
ps.in_phanso()
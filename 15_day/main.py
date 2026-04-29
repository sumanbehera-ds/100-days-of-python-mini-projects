class complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    def __add__(self,other):
        return complex(self.real + other.real ,self.imag+other.imag)
    def __mul__(self,other):
        real_part =(self.real*other.real)-(self.imag*other.imag)
        imag_part = (self.imag*self.real)+(other.real*other.imag) 
        return complex(real_part,imag_part)
    def __str__(self):
        return (f"no:::{self.real},{self.imag}i")
a = complex(4,6)
b = complex(6,8)
c = a+b
d = a*b
print(c)
print(d)
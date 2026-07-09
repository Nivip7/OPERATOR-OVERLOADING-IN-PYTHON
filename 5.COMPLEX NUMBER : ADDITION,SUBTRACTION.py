class Complex:
    def __init__(self, r, i):
        self.r, self.i = r, i
    def __add__(self, o):
        return Complex(self.r + o.r, self.i + o.i)
    def __sub__(self, o):
        return Complex(self.r - o.r, self.i - o.i)
    def __str__(self):
        return str(self.r) + " + " + str(self.i) + "i"

c1 = Complex(float(input("R1: ")), float(input("I1: ")))
c2 = Complex(float(input("R2: ")), float(input("I2: ")))
print("Add:", c1 + c2)
print("Sub:", c1 - c2)


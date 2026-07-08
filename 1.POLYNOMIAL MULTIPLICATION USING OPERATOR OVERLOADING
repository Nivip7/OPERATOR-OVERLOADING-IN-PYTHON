class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = coeffs

    def __mul__(self, other):
        result = [0] * (len(self.coeffs) + len(other.coeffs) - 1)

        for i in range(len(self.coeffs)):
            for j in range(len(other.coeffs)):
                result[i + j] += self.coeffs[i] * other.coeffs[j]

        return Polynomial(result)

    def __str__(self):
        return str(self.coeffs)

poly1=list(map(int,input("Enter a polynomial: ").split()))
poly2=list(map(int,input("Enter a polynomial: ").split()))
p1 = Polynomial(poly1)
p2 = Polynomial(poly2)
result = p1 * p2

print("Polynomial multiplication:", p1 * p2)

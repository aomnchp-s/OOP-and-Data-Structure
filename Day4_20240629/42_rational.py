from math import gcd as _gcd

class Rational:
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self):
        gcd = _gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __add__(self, other):
        if isinstance(other, Rational):
            numerator = self.numerator * other.denominator + other.numerator * self.denominator
            denominator = self.denominator * other.denominator
            return Rational(numerator, denominator)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Rational):
            numerator = self.numerator * other.denominator - other.numerator * self.denominator
            denominator = self.denominator * other.denominator
            return Rational(numerator, denominator)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Rational):
            numerator = self.numerator * other.numerator
            denominator = self.denominator * other.denominator
            return Rational(numerator, denominator)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Rational):
            if other.numerator == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            numerator = self.numerator * other.denominator
            denominator = self.denominator * other.numerator
            return Rational(numerator, denominator)
        return NotImplemented

    def __float__(self):
        return self.numerator / self.denominator

    def __int__(self):
        return self.numerator // self.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __lt__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator < other.numerator * self.denominator
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator <= other.numerator * self.denominator
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator > other.numerator * self.denominator
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator >= other.numerator * self.denominator
        return NotImplemented

    def __getitem__(self, index):
        if index == 0:
            return self.numerator
        elif index == 1:
            return self.denominator
        else:
            raise IndexError("Index out of range. Use 0 for numerator and 1 for denominator.")

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    r1 = Rational(3, 4)
    r2 = Rational(2, 3)

    print("R1:", r1)
    print("R2:", r2)

    print("R1 + R2 =", r1 + r2)
    print("R1 - R2 =", r1 - r2)
    print("R1 * R2 =", r1 * r2)
    print("R1 / R2 =", r1 / r2)

    print("Float R1:", float(r1))
    print("Int R1:", int(r1))

    print("R1 < R2:", r1 < r2)
    print("R1 <= R2:", r1 <= r2)
    print("R1 > R2:", r1 > r2)
    print("R1 >= R2:", r1 >= r2)

    print("R1 numerator:", r1[0])
    print("R1 denominator:", r1[1])

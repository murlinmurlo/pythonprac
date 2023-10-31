
class Rectangle:
    rectcnt = 0

    def __init__(self, c1, c2, c3, c4):
        self.x1 = c1
        self.y1 = c2
        self.x2 = c3
        self.y2 = c4

        Rectangle.rectcnt += 1
        setattr(self, f"rect_{Rectangle.rectcnt}", Rectangle.rectcnt)

    def __str__(self):
        return f"({self.x1},{self.y1})({self.x1},{self.y2})({self.x2},{self.y2})({self.x2},{self.y1})"

    def area(self):
        return abs((self.x2 - self.x1) * (self.y2 - self.y1))

    def __eq__(self, other):
        return self.area() == other.area()

    def ___lt__(self, other):
        return self.area() < other.area()

    def __mul__(self, number):
        return Rectangle(self.x1 * number, self.y1 * number, self.x2 * number, self.y2 * number)

    __rmul__ = __mul__
    

r1 = Rectangle(1, 2, 3, 4)
r2 = Rectangle(1, 2, 3, 5)
r3 = Rectangle(1, 2, 3, 4)

print(r1.__rmul__(2))

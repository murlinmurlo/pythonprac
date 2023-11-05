class Triangle:
    def __init__(self, point1, point2, point3):
        self.point1 = tuple(point1)
        self.point2 = tuple(point2)
        self.point3 = tuple(point3)
    
    def __abs__(self):
        x1, y1 = self.point1
        x2, y2 = self.point2
        x3, y3 = self.point3
        return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2)
    
    def __bool__(self):
        return abs(self) != 0
    
    def __lt__(self, other):
        return abs(self) < abs(other)
    
    def __contains__(self, other):
        return (self.point1 in other and
                self.point2 in other and
                self.point3 in other)
    
    def __and__(self, other):
        return bool(self) and bool(other)



import sys
s = sys.stdin.read()
exec(s)

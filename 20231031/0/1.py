class Rectangle:

    def __int__(self, c1, c2, c3, c4):
        Rectangle.x1 = c1
        Rectangle.y2 = c2
        Rectangle.x2 = c3
        Rectangle.y2 = c4

    def __str__(self):
        return f"({x1},{y1})({x1},{y2})({x2},{y2})({x2},{y1})"

r = Rectangle()
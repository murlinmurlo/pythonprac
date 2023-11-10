class InvalidInput(Exception):
    pass

class BadTriangle(Exception):
    pass

def triangleSquare(inStr):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(inStr)
    except:
        raise InvalidInput("Invalid input")

    sides = [
        (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1),
        (x3 - x2) * (y1 - y2) - (x1 - x2) * (y3 - y2),
        (x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3),
    ]
    area = abs((x1 - x2) * (y1 - y3) - (x1 - x3) * (y1 - y2)) / 2
    if any(side == 0 for side in sides):
        raise BadTriangle("Not a triangle")
    elif not area:
        raise BadTriangle
    return area

    s = abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2
    return round(s, 2)

while True:
    inStr = input()
    try:
        s = triangleSquare(inStr)
        print(s)
        break
    except InvalidInput as e:
        print(e)
    except BadTriangle as e:
        print(e)

def sub(x, y):
    if '__sub__' in dir(x) and '__sub__' in dir(y):
        return x - y
    else:
        return type(x)([i for i in x if i not in y])

print(sub(*eval(input())))

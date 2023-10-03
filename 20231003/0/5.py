def adders(n):
    res = []
    for i in range(n):
        def adder(x, j = i):
            return x + i
        res.append(adder)
    return res

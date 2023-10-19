M, N = eval(input())
print([i for i in range(M, N) if not any([(i / k).is_integer() for k in range(2, i)]) and i != 1])

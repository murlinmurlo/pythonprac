matr, res = [], []
count = 0
while s := input():
    matr.append([int(i) for i in s.split(",")])
    count += 1
count //= 2
for i in range(count):
    tmp = []
    for j in range(count):
        tmp.append(0)
        for k in range(count, count * 2):
            tmp[j] += matr[i][k - count] * matr[k][j]
    res.append(tmp)

for i in range(count):
    print(*(res[i]), sep=",")
    

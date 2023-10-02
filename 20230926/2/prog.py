a = list(eval(input()))
n = len(a)
f = 1
while (f):
    f= 0
    for i in range(0, n-1):
        if a[i]**2%100 > a[i+1]**2%100:
            a[i], a[i+1] = a[i+1], a[i]
            f = 1
print(a)  

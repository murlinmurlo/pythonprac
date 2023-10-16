from fractions import Fraction

def check(k, x):
    s = len(k) - 1
    ans = Fraction("0")
    for i in range(s + 1):
        ans += k[-(i + 1)]*(x ** i)
    return ans

a = list(map(Fraction, input().split(',')))
s, el, a_s, a_k = a[0], a[1], int(a[2]), []

for i in range(3, 3 + a_s + 1):
    a_k.append(a[i])
b_s = int(a[4 + a_s])
b_k = []
for i in range(5 + a_s, 6 + a_s + b_s):
    b_k.append(a[i])

print(False if check(b_k, s) == 0 else check(a_k, s) / check(b_k, s) == el)


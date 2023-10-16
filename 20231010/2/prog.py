from math import *

def scale(a, b, c, d, x):
    return (x-a) * (d - c) / (b - a) + c

W, H, a, b, f = input().split()

W, H, a, b = map(int, (W, H, a, b))
f = eval('lambda x:' + f)

s = [[' '] * W for i in range(H)]
y = []

for i in range(W):
    y.append(f(scale(0, W-1, a, b, i)))

p = 0
for i in range(W):
    w = int(scale(min(y), max(y), H - 1, 0, y[i]))
    s[w][i] = "*"

    if i > 0:
        l, r = min(p, w) + 1, max(p, w)
        median = (r - l) // 2

        for j in range(l, r):
            if j <= median:
                s[j][i - 1] = "*"
            else:
                s[j][i] = "*"

    p = w

print("\n".join("".join(g) for g in s))


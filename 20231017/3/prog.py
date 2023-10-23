from collections import Counter

W = int(input())
c = Counter()

while True:
    s = input().lower()
    if not s:
        break
    
    words = ''.join(c if c.isalpha() else ' ' for c in s).split()
    c.update(w for w in words if len(w) == W)

if c:
    p = [w for w in c if c[w] == max(c.values(), default=0)]
    p.sort()
    print(*p)

import sys
class Omnibus:
    attrs = {}

    def __setattr__(self, name, m):
        c = self.attrs.setdefault(name, [0, []])
        c[0] += 1
        if self not in c[1]:
            c[1].append(self)

    def __getattr__(self, name):
        c = self.attrs.get(name)
        if c and self in c[1]:
            return c[0]

    def __delattr__(self, name):
        c = self.attrs.get(name)
        if c and self in c[1]:
            c[0] -= 1
            c[1].remove(self)

s = sys.stdin.read()
exec(s)



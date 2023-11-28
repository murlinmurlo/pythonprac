C = type("C", (), {"var": 100500, "__init__" : lambda self, x: setattr(self, "var", x)})
c = C(123)
print(c.var)

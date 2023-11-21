import pickle

#print(pickle.dumps(["QWERTY", 100500]*8, protocol = 0))

class C:
    def __init__(self, i):
        self.var = i
c = C(2)
print(pickle.dumps(c))

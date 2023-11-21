import pickle


class SerCls():
    def __init__(self, lst, dct, num, st):
        self.lst = lst
        self.dct = dct
        self.num = num
        self.st = st
        
ser = SerCls([1, 2, 3], {"4": 4, "5": 5}, 6, "7")
serialized = pickle.dumps(ser)
del ser
ser1 = pickle.loads(serialized)

print(ser1.lst) 
print(ser1.dct)  
print(ser1.num)  
print(ser1.st) 






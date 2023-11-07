class A(Exception):
    pass

class B(A):
    pass

class C(B):
    pass

for E in [A, B, C]:
    try:
        raise E
    except B:
        print('B')
    except C:
        print('C')
    
    except A:
        print('A')

obj = C()
print(obj)  

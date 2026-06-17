class A:
    def f1(self):
        print('this is f1')
    def f2(self):
        print("this is f2")
        
# class B(A):
#     def f3(self):
#         print('this is f3')
#     def f4(self):
#         print("this is f4`")

class B:
    def f3(self):
        print('this is f3')
    def f4(self):
        print("this is f4`")
        
class C(B,A):
    def f5(self):
        print('this is f5')
        
# obj1 = B()
# obj1.f1()

obj2 = C()
obj2.f3()

class A1:
    def __init__(self):
        print("in a init")
    def f1(self):
        print('f1 works')
class B2(A1):
    def __init__(self):
        super().__init__()
        print("In b init")
    def f2(self):
        self.f1()
        print('f2 works')    
       
test = B2()
test.f2()

class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        super().__init__()
        print("B")

class C(A):
    def __init__(self):
        super().__init__()
        print("C")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("D")

obj = D()
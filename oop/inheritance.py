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
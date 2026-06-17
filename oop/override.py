class A:
    def show(self):
        print("in A show")

class B(A):
    def show(self):
        print("in B show")
        super().show()
obj = B()
obj.show()
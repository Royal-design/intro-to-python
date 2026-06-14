class Abc:
    def __new__(cls):
        print('constructor called')
        return super(Abc, cls).__new__(cls)
    def __init__(self):
        print("running")
    def show(self):
        print("show")

obj1 = Abc()
obj1.show()

obj2 =Abc.__new__(Abc)
obj2.__init__()
obj2.show()
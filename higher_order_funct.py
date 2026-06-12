def square(x):
    return x**2

def cube(x):
    return x**3
def add(x,y):
    return x+y
    
def operate(values, operation):
    if operation == add:
        total = 0
        for i in values:
            total = add(total, i)
        print(total)
    else:
        for i in values:
            result = operation(i)
            print(result)
   

operate([1,2,3,4,5], square)
operate([1,2,3,4,5], cube)
operate([1,2,8], add)
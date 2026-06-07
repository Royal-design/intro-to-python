def calc(a,b, sign):
    if sign == '+': print(f"the sum of {a} and {b} is {a+b}")
    elif sign == '-': print(f"the difference of {a} and {b} is {a-b}")
    elif sign == '*': print(f"the product of {a} and {b} is {a*b}")
    elif sign == '/': print(f"the quotient of {a} and {b} is {a/b}")
    else: print('Invalid operator')
    
calc(10,5,'+')
calc(10,5,'-')
calc(10,5,'*')
calc(10,5,'/')
calc(10,5,'^')


def calc(a, b=2):
    return f'the sum of {a} and {b} is {a+b}'
print(calc(10))
print(calc(10,5))

print('------------------------')

def calc(x, *args):
    sum = x
    for value in args:
        sum += value
    print(sum)
    
calc(10,5,2,3,4)

def person(name, **kwargs):
    print(f"Hello {name}")
    print(kwargs)
    print(kwargs.items())
    for k, v in kwargs.items():
        print(k, " : ", v)
        
person(name='Emmy', age=27, job='Dev')

    
    


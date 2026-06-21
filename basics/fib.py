# fibbonanacci Iteration

# def fib(n):
#     a=0
#     b=1
    
#     if n ==1:
#         print(a)
#     else:
#         print(a)
#         print(b)
        
#         for i in range(2, n):
#             c=a+b
#             a=b
#             b=c
#             print(c)
            
# fib(6)

# fibbonanacci final result

def fib(n):
    a = 0
    b = 1

    if n == 1:
        print(a)
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            
        print(b)

fib(2)
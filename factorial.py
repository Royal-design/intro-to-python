def factorial(value):
    res=1
    for i in range(1, value+1):
        res = res * i
    return res

print(factorial(0))
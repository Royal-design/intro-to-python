from functools import reduce


num = [1,2,3,4,5,6,7,8,9,10]
# even = []

# for i in num:
#     if i%2 == 0:
#         even.append(i)

def is_even(n):
    return n%2 == 0

def is_odd(n):
    return n%2 != 0
    
even = list(filter(is_even, num))
odd = list(filter(is_odd, num))
print(even)
print(odd)

# with lambda
even = list(filter(lambda x: x%2 == 0, num))
odd = list(filter(lambda x: x%2 != 0, num))
print("even: ", even)
print("even: ", odd)

# double
double = list(map(lambda n: n*2, even))
print("double: ", double)

# reduce

total = reduce(lambda x,y: x+y, double)
print("total: ", total)


# 
val = [2,3,4]
print("double: ", list(map(lambda x: x*2, val)))
print("reduce: ", reduce(lambda x,y:x+y, val))
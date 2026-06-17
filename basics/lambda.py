from functools import reduce


square = lambda x: x**2
add = lambda x,y: x+y
print(add(5,5))
print(square(5))

data = [2,4,6,7,8,8,9,10]
sum = (reduce(lambda x,y: x+y, data))
print(sum)
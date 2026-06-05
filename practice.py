tup = (1, 2, 3, 4, 5)
print(type(tup))

name = {
    "first_name": "John",
    "last_name": "Doe",
}

print(type(name))

items = [1,2,3,4,5]
items[1] = "two"
print(items)

first, second, *rest = tup
print(first, second, rest)
confirm = 1 in tup
print(confirm)

# Set
set = {1,2,2,3,4,5}
print(set)

print(2 in set)

set.add(6)
print(set)

print('........................................................')
setA = {1, 3, 5, 6, 7, 9}
setB = {1, 2, 3, 4, 5, 6}
setC = {1,3,5}

print(setA.intersection(setB))
print(setA.union(setB))
print(setA.difference(setB))
print(setB-setA)
print(setA.issubset(setB))
print(setC.issubset(setA))
print(setA | setB)



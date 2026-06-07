# List
listA = [1,2,3,4,5]
print(listA)
listA.append(6)
print(listA)

c = listA.remove(2)
listA.insert(4,21)
print(listA)

print(listA.index(4))
print(listA[2])
print(listA[1:4])


# tuple
tup = (1, 2, 3, 4, 5)
print(type(tup))


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

name1 = {"Ade"}
name2 = {"john"}
print(name1 & name2)

def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))

testA = {2,4,5}
testB = {3,21}

print(testA.union(testB))

# Dictionary

dictA = {1:'Ade', 2:'John', 3:'Doe'}
dictA.update({4:'Smith'})
print(dictA)

dictA.pop(1)
print(dictA)
print(dictA.get(2))

dictB = {};
dictB['name'] = 'Alice'
dictB['age'] = 25
print(dictB)
dictB.update({'name':'Bob'})
print(dictB)
dictB['name'] = 'Charlie'
print(dictB)

keys = ['first_name', 'last_name', 'age']
values = ['John', 'Doe', 25]
dictC = dict(zip(keys, values))
print(dictC)

def get_dict(name, age):
    introduction = f"Hello, {name}!"
    return {'name': name, 'age': age, 'introduction': introduction}

print(get_dict('Alice', 25))

del dictC['age']
print(dictC)

# variable storage
a = 10
b=a
print(id(a))
print(id(b))

# python types

a =10
print(type(a))

pi = 3.14
print(type(pi))

c = 7+4j
print(type(c))
print(c.imag)
print(c.real)

print(complex(8,10))

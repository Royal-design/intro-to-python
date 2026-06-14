data= ['apple', 'banana', 'cherry', 'date', 'elderberry']
    
for item in data:
    print(item)
       
for i in range(5):
    print(f"The value of i is {i}")
    
for value in range(9):
    if value % 3 != 0:
        print(value)
print('------------------------')

for value in range(10):
    if value % 2 == 0:
        continue
    print(value)
    
print('------------------------')
for value in range(10):
    if value == 4:
        break
    print(value)
  
print('------------------------')
for value in range(10):
    if value % 3 == 0:
        continue
    if value == 8:
        break
    print(value)
    
    for value in range(20):
        if value % 3 == 0:
            continue
        if value == 8:
            break
        print(f'I love you in {value}')
    
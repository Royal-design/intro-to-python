import sys
from time import sleep


sys.setrecursionlimit(5)
print(sys.getrecursionlimit())

count =1

def greet():
    global count
    print("Hello", count)
    count+=1
    sleep(0.5)
    greet()

greet()



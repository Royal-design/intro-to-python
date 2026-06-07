a = 10

def something():
    print("inside: ", a)

something()
print("outside: ", a)

print("-------------")


def something2():
    a= 30
    print("inside: ", a)

something2()
print("outside: ", a)
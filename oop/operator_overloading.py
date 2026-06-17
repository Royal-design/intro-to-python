a =5
b=6
# c=7

c = int.__add__(a,b)
d=a.__add__(b)
print(c, d)

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def __str__(self):
        return f"{self.name} has {self.balance} in his account"
    def __add__(self, other):
        return Account("combined", self.balance + other.balance)
    def __gt__(self, other):
        return self.balance > other.balance
        
user1 = Account("John", 1000)
user2 = Account("Jane", 2000)

# combined = Account.__add__(user1, user2)
combined = user1 + user2
print(combined)

print(user1)
print(user2)

if user1 > user2:
    print("user1 is greater than user2")
else:
    print("user1 is not greater than user2")
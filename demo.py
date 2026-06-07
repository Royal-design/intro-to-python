def calc(a,b, sign):
    if sign == '+': print(f"the sum of {a} and {b} is {a+b}")
    elif sign == '-': print(f"the difference of {a} and {b} is {a-b}")
    elif sign == '*': print(f"the product of {a} and {b} is {a*b}")
    elif sign == '/': print(f"the quotient of {a} and {b} is {a/b}")
    else: print('Invalid operator')
    
calc(10,5,'+')
calc(10,5,'-')
calc(10,5,'*')
calc(10,5,'/')
calc(10,5,'^')

# a = input("Enter a number: ")
# b = input("Enter another number: ")
# a, b = b, a
# print(a,b)

is_true = True

if is_true:
    print("true")
else:
    print("false")

# odd or even number
def get_number_type(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
    
print(get_number_type(10))
print(get_number_type(11))

def vote_eligibility(age):
    if age >=18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."
    
print(vote_eligibility(18))
print(vote_eligibility(17))


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

age = 20
is_active = True

if age >=18:
    print('You are an adult')
    if is_active:
        print('You are active')
    else:
        print('you are not active')
else:
    print('You are a minor')

score = 71
if score >= 80:
    print('You have grade A+')
elif score >= 70:
    print('You have grade A')
elif score >= 60:
    print('You have grade B')
elif score >= 50:
    print('You have grade C')
else:
    print('You have failed')
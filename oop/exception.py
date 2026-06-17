
try:
    # a = int(input("enter the numerator"))
    # b = int(input("enter the denominator"))
    a =20
    b=2
    result = a/b
    print("result: ", result)
except ZeroDivisionError as z:
    print("Zero Division Error occurred", z)
except ValueError as v:
    print("Value Error occurred", v)
except Exception as e:
    print("Exception occurred", e)
finally:
    print("finally block")


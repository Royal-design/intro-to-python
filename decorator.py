# def log_decorator(func):
#     def wrapper(x,y):
#         print("print ", x, " ",  y)
#         result = func(x,y)
#         print("result ", result)
#         return result
#     return wrapper

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("values ", args)
        result = func(*args, **kwargs)
        print("result ", result)
        return result
    return wrapper

def greater_first(func):
    def wrapper(x,y):
        if x < y:
            x,y = y,x
        return func(x,y)
    return wrapper

@log_decorator
def divide(x,y):
    return x/y

@log_decorator
def subtract(x,y):
    return x-y

sub = greater_first(subtract)
divide = greater_first(divide)

print(divide(2,10))
print(sub(2,8))
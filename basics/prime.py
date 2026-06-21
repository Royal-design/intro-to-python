# num = 7

# for n in range(2, num):
#     if num % n == 0:
#         print(f"{num} is not prime")
#         break
#     else:
#         print(f"{num} is prime")
#         break

# for n in range(3):
#     if n >1:
#         for i in range(2, int(n**0.5)+1):
#             if n % i == 0:
#                 print(f"{n} is not prime")
#                 break
#         else:
#             print(f"{n} is prime")
                
for n in range(1, 10):
    if n <= 1:
        print(f"{n} is not prime")
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                print(f"{n} is not prime")
                break
        else:
            print(f"{n} is prime")
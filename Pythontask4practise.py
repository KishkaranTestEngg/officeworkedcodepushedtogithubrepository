# python task 4
from itertools import count

# def function_even_number():
#     my_list = [10, 501, 22, 37, 100, 999, 87, 351]
#
#     for i in my_list:
#         if i % 2 == 0:
#             print(f"The number is an even number: {i}")
# function_even_number()

# def function_odd_number():
#     mylist =[10,501, 22, 37, 100,999,87,351 ]
#
#     for i in mylist:
#         if i % 2 != 0:
#             print(i)
#          print(f"The number is odd number: {i}")
# function_odd_number()


#functions to print a prime number in a list

numbers = [10, 501, 22, 37, 100, 999, 87, 351]
prime_numbers = []

for num in numbers:
    if num > 1:
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
            if count == 2:
           prime_numbers.append(num)

 print(prime_numbers)

num = 6
for i in range(2, num):
    if num % i == 0:
        print("Not a prime number")
        break
else:
    print("Prime number")





# A basic function program

def welcome_function():
    print('welcome to function learning in python')

welcome_function()

# function program add two number

def add_numbers():
    a=34
    b=67
    c=a+b
    print(f"After adding two numbers, the sum is = {c}")
add_numbers()

# function program with argument adding

def add_numbers_argument(a,b,c):
    return a+b+c
print(add_numbers_argument(1,2,3))

# function with closure function

def first_function():
    print('first function ')
first_function()
def second_function(a):
    return a
print(second_function(2)) # Second function called

first_function()

# function with callback value

def addition_of_two_numbers(a,b):
    return a+b
def subtraction_of_two_numbers(a,b):
    return a-b
def result_of_the_numbers(x, y):
    return x+y
print(result_of_the_numbers(3,4))
print(addition_of_two_numbers(3,73))
print(subtraction_of_two_numbers(15,85))



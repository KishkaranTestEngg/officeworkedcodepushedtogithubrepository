# Using list to find maximum value in the list

# numbers =[45, 76, 3, 235, 54]
#
# print("The greatest number in the list ",max(numbers))


#Using list to find minimum value in the list

# numbers =[345,5678,5,34343,56]
#
# print("The smallest values in the list",min(numbers))

# using the list now by loops to print greatest value

# numbers =[345,5678,5,34343,56]
#
# greatest=numbers[0]
#
# for num in numbers:

# Program to find smallest value in the list using the Loop concept

# numbers =[345,5678,5,34343,56]
#
# smallest=numbers[0]
#
# for num in numbers:
#     if num<smallest:
#         smallest=num
#
# print("The smallest value in the list is",smallest)


# check using the while loops the greatest value

# numbers =[345,5678,5,34343,56]
#
# greatest = numbers[0]
#
# i=1
#
# while i<len(numbers):
#     if numbers[i] > greatest:
#         greatest = numbers[i]
#     i=i+1
# print("The greatest number in the list is",greatest)


# checking the greatest number using the for loop

numbers = [345, 5678, 5, 34343, 56]

greatest=numbers[0]

for num in numbers:
  if num>greatest:
      greatest=num
print("The greatest number in the list",greatest)

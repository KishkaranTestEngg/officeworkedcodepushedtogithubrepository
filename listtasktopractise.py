#  First program list task 1


numbers = [10, 501, 22, 37, 100, 999, 87, 351]

even = []
odd = []

for n in numbers:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print(even)
print(odd)

# Second program list task 2

numbers = [10, 501, 22, 37, 100, 999, 87, 351]

primes = []

for n in numbers:
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        if n > 1:
            primes.append(n)

print(primes)
print(len(primes))

# Third program for the list task

numbers = [10, 501, 22, 37, 100, 999, 87, 351]


def is_happy(n):
    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))

    return n == 1

happy_numbers = []

for num in numbers:
    if is_happy(num):
        happy_numbers.append(num)

print("Happy numbers:", happy_numbers)
print("Count:", len(happy_numbers))

# Fourth program for the list task

num = int(input("Enter a number: "))

last_digit = num % 10

while num >= 10:
    num = num // 10

first_digit = num

print("Sum:", first_digit + last_digit)


# Fifth program for the list task using coin combination problem

target = 10
coins = [1, 2, 5, 10]

count = 0

for c1 in range(target + 1):  # ₹1 coins
    for c2 in range(target // 2 + 1):  # ₹2 coins
        for c5 in range(target // 5 + 1):  # ₹5 coins
            for c10 in range(target // 10 + 1):  # ₹10 coins

                total = (c1 * 1) + (c2 * 2) + (c5 * 5) + (c10 * 10)

                if total == target:
                    print(f"₹1:{c1}, ₹2:{c2}, ₹5:{c5}, ₹10:{c10}")
                    count += 1

print("Total ways:", count)

# In list of 3 need to find the duplicate one

# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# list3 = [5, 4, 8, 9]
#
# duplicates = list(set(list1) & set(list2) & set(list3))
#
# print(duplicates)

list1= ['kishore','kish', 'tamil','sathish']
list2= ['kish','tamil','spencer','kishore']
list3= ['Arasan','sathish', 'tamil', 'kish']

duplicates = list(set(list1) & set(list2) & set(list3))
print(duplicates)

# In a list a set is used to remove the duplicate ones in common three of them.

# 7 task is to find the non-repeating elements in the list

numbers = [10, 20, 30, 10, 40, 20, 50]

non_repeating = []

for num in numbers:
    if numbers.count(num) == 1:
        non_repeating.append(num)

print("After checking the list non repeating numbers are =",non_repeating)


# Task 8 to find the sorted list

nums = [4, 5, 6, 7, 0, 1, 2]

minimum = nums[0]

for num in nums:
    if num < minimum:
        minimum = num

print("Minimum element is:", minimum)

# Concept of sorted list is to find the finding the minimum element in a rotated sorted list.

# task 9  triplet program

nums = [10, 20, 30, 9]
target = 59

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            if nums[i] + nums[j] + nums[k] == target:
                print("Triplet found:", nums[i], nums[j], nums[k])
                exit()

print("No triplet found")

# A triplet means a program that finds three numbers in a group of 3 elements from a list


# task 10 to find the sun of a sublist

nums = [4, 2, -3, 1, 6]

for i in range(len(nums)):
    total = 0
    for j in range(i, len(nums)):
        total += nums[j]

        if total == 0:
            print("Sub-list found:", nums[i:j + 1])

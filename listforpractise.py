
# list are mutable in nature
# list is a data type in python which contains an array of elements of any other data type separated by ',' .
# lists item are printed in the order they are created
# lists are declared using '[]'.


my_list=["ashok",2,"kumar",78]
print(type,(my_list))

# printing the two list values

my_list1=["ashok","kish"]
my_list2=["kumar", "karan"]

my_list3=my_list1+my_list2

print((my_list3))

# how to find the length of a list

my_length_of_list=["Hellow welcome to learning the python list"]
total_length=len(my_length_of_list)
print(total_length)   # why 1 is coming as a string length what is mistake done here.

# Using indexing fetching the items in the list

# my_cars=['polo','indica', 'safari','swift','wagronr','zen']
#
# print(type,(my_cars[0]))
# print(my_cars[3],(my_cars[1]))

my_car_brands=['tata','suzuki','skoda','kia','volvo']

print(my_car_brands[3]) # printing the 3 indexed position
print(my_car_brands[4],my_car_brands[1])  # combining and printing the two indexed position values.

# for fetching and printing each item at a time


# for fetching and printing each item at a time using indexing

for i in range(len(my_car_brands)):
    if i >= 2:
        break
    print(my_car_brands[i])

total_length_card_brands = len(my_car_brands)
print(my_car_brands)

for i in range(len(my_car_brands)):
    if my_car_brands[i] =='tata' or my_car_brands[i] =='suzuki':
        continue
    print(my_car_brands[i]) # leaving tata and suzuki and printing rest of things

#  append () is used for adding item at the end of list

my_car_brands.append("ford")
print(my_car_brands) # added a item at the end.
my_car_brands.append("landrover")
print(my_car_brands) # added a item at the end.

# extend () is used to combine the list into one

my_car_brands.extend(["fiat","maruthi"])
print(my_car_brands)  #Used to combine and add two values in the list.

# insert() is used to insert item at a particular index

my_car_brands.insert(2,'skoda')
print(my_car_brands)  # At a particular index a new value got added.

my_car_brands.insert(8,'suzuki')
print(my_car_brands)


# pop(6) is used to remove item from a list in sixth index position

my_car_brands.pop(8)
print(my_car_brands)

# remove () will remove item from list

my_car_brands.remove('tata')
print(my_car_brands)

# clear() is used for emptying a list

my_car_brands.clear()
print(my_car_brands)

# count for practice

my_car_brands.count('suzuki')
print(my_car_brands)




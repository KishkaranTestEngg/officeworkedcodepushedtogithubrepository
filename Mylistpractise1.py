
# #To print all the added bike values in list
my_bike_list =['kawasaki', 'hero', 'suzuki', 'bmw']
print(my_bike_list)

# # second print using the  indexing position
#
# print(my_bike_list[2]) # So second index position suzuki
#
# finding the length of the list

# length_of_the_list = len(my_bike_list) # store it in a variable and call it again
# print(length_of_the_list)

# # To print two items in a single print
#
# print(my_bike_list[1],my_bike_list[3])
#
# # # for fetching and printing each item at a time
# # for i in my_bike_list:
# #     print(i)
# #
# # # for fetching and printing each item at a time using indexing
# # for i in range(length_of_the_list):  # for i in range(6):
# #   print(my_bike_list[i])
#
# break is used to finish looping
# for i in range(length_of_the_list):
#      if i >= 1:  # So when 2 index position comes the loop stops here
#         break
# print(my_bike_list[i])


# continue is used to skip iteration

# for i in range(length_of_the_list):
#     if my_bike_list[i] == 'suzuki':
#         continue
#     print(my_bike_list[i])

# Append we use to add a item at end of the list

# my_bike_list.append('bajaj')
# print(my_bike_list)

# # extend if we have two bile list then this command is used to combine them
# my_bike_list_2 =['lml', 'yamaha', 'ather']
# print(my_bike_list_2)

# # now using the extend will merge my-bike-list 1 and 2
#
# my_bike_list.extend(my_bike_list_2)
# print(my_bike_list)

# # insert() is used to insert item at a particular index
# my_bike_list.insert(3,'lancer')
# print(my_bike_list)

# pop() is used to remove item from a list # pop(6) is used to remove item from a list in 0 index position
my_bike_list.pop(0)
print(my_bike_list)


# remove used to remove a item by value

my_bike_list.remove('bmw')
print(my_bike_list)

# clear is user for clearing the list

my_bike_list.clear()
print(my_bike_list)


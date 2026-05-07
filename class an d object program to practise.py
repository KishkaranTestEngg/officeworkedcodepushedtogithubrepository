class MyClass:
    student_name = "Richard"
    Age_of_student = 35


# # Create an object
# student = MyClass()
# # This is using the f strings
# print(f"The student name {student.student_name} and Age of student {student.Age_of_student}")


# class Cars:
#     Tata_brand = 'indica'
#     Ford_brand = 'icon'
# # creating an object for the class
# c1=Cars()
# # with object printed there values
# print(c1.Tata_brand)
# print(c1.Ford_brand)


# class Animal:
#     def sound(self):
#         print("Animal makes sound")
#
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")
#
# d= Dog()
# d.sound()
# d.bark()


# class Dog:
#     def sound(self):
#         print("Bark")
#
# class Cat:
#     def sound(self):
#         print("Meow")
#
# animal = Dog()
# animal.sound()
#
# animal1 = Cat()
# animal1.sound()


# class Employee:
#     # Constructor
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     # Method (no return, only print)
#     def calculate_salary(self):
#         print(f"Name: {self.name}, Salary: {self.salary}")
#
# # Create objects
# e = Employee(name="Richard", salary=35)
# e1 = Employee(name="kish", salary=30)
#
# # Call methods
# e.calculate_salary()
# print("___________")
# e1.calculate_salary()

# class Mydetails:
#     def __init__(self, name, age, qualification, designation , address):
#         self.name = name
#         self.age = age
#         self.qualification = qualification
#         self.designation = designation
#         self.address = address
#
#     def print_my_details(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Qualification:", self.qualification)
#         print("Designation:", self.designation)
#         print("Address:", self.address)
#
# md=Mydetails ("kishore","35", "ME","tester", "160/54 big street chennai")
# md.print_my_details()


# class Savingsaccount:
#     def __init__(self, name, account_no, account_type, account_balance):
#         self.name = name
#         self.account_no = account_no
#         self.account_type = account_type
#         self.account_balance = account_balance
#     def print_savings_account(self):
#         print("Name:", self.name)
#         print("Account No:", self.account_no)
#         print("Account Type:", self.account_type)
#         print("Account Balance:", self.account_balance)
#
# class Interestratecalculation:
#     def __init__(self,daily_balance, rate, no_of_days):
#         self.daily_balance = daily_balance
#         self.rate = rate
#         self.no_of_days = no_of_days
#
#     def print_interest_rate_calculation(self):
#         interest_rate_calculation = (self.daily_balance* self.rate * self.no_of_days) / 36500
#         return interest_rate_calculation
#
# sa= Savingsaccount('kishore',1025489, 'savings',55000, )
# ic= Interestratecalculation( daily_balance=55000, rate=3.5, no_of_days=30 )
#
# sa.print_savings_account()
# print("After interest calculated pwe month=",ic.print_interest_rate_calculation()) # after that print the method


class Bike:
    def __init__(self,bike_name, bike_type, company_name, engine_cc ,No_of_revolutions_per_second,color):
        self.bike_name = bike_name
        self.bike_type = bike_type
        self.company_name = company_name
        self.engine_cc = engine_cc
        self.No_of_revolutions_per_second = No_of_revolutions_per_second
        self.color = color
    def calculate_engine_rpm(self):
        print("Bike name:", self.bike_name)
        print("Bike type:", self.bike_type)
        print("Company name:", self.company_name)
        print("Engine CC:", self.engine_cc)
        print("No of revolutions:", self.No_of_revolutions_per_second)
        print("color:", self.color)
        self.engine_rpm = (self.engine_cc *self.No_of_revolutions_per_second ) / 100
        return self.engine_rpm

bk =Bike("splendor","commuter","hero",100, 1000,"blue")
print("Engine rpm per second of splendor bike =", bk.calculate_engine_rpm())
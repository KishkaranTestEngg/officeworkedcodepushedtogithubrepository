
# class is a blueprint where objects are created
# Clas has attributes and methods

# class Office:
#     def def_ceo(self):
#         print("CEO means the Chief Executive Officer")
#
#     def def_hr(self):
#         print("HR means Human Resource responsible for recruiting people")
#
#
# frj = Office()
# frj.def_ceo()
# frj.def_hr()

class Guvi:

    def Guvi_courses_offered(self, AI, Machinelearning , datascience, Cybersecurity):
       self.AI= AI
       self.Machinelearning
       self.datascience
       self.Cybersecurity

    def Guvi_course_offered(self)
       print("First course detail",self.AI)
       print("Second course detail",self.Machinelearning)
       print("Third course detail",self.datascience)
       print("Fourth course detail", self.Cybersecurity)

    gco= Guvi()






class addition:  # creating a class
    def add_two_number(self):  # And creating a function for it
     a=15
     b=45
     c=a+b
     print(f"After adding two numbers =+{c}")

adj= addition()  # creating a class object and calling them.
adj.add_two_number()


# creating class and objects with parameter values

class studentdetails:
      def __init__(self,name, age, rollno, standard):
          self.name=name
          self.age=age
          self.rollno=rollno

      def student_details(self):
          print('student name', self.name)
          print('student age', self.age)
          print('student roll no', self.rollno)

sdb = studentdetails("Kishorekaran", 22, "947", 11)
sdb1= studentdetails("kumar", 23, "947", 10)
sdb.student_details()
sdb1.student_details()


class carmaker():
    def __init__(self,carname,carcompamyname,typeofcar,runningtype):
        self.carname=carname
        self.carcompamyname=carcompamyname
        self.typeofcar=typeofcar
        self.runningtype=runningtype

    def car_maker_name(self):
        print("The carmaker name =",self.carname)
        print("The carcompanyname =",self.carcompamyname)
        print("The type of car =",self.typeofcar)
        print("The running type =",self.runningtype)



cmk = carmaker(carname="ford ikon", carcompamyname="ford",typeofcar="sedan", runningtype="petrol")
cmk1= carmaker(carname="indica",carcompamyname="tata",typeofcar="hatchback",runningtype="diesel")

cmk.car_maker_name()
print("_______")
cmk1.car_maker_name()

class typesofbike():
    def __init__(self,bikename,bikecompamyname,typeofbike,runningtype):
        self.bikename=bikename
        self.bikecompamyname=bikecompamyname
        self.typeofbike=typeofbike
        self.runningtype=runningtype

    def bike_maker_name(self):
         print("The bikemaker name =",self.bikename)
         print("The bikecompamyname =",self.bikecompamyname)
         print("The typesofbike =",self.typeofbike)
         print("The running type =",self.runningtype)

bk =typesofbike("pulsar","Bajaj","sports","petrol")
bk1 =typesofbike("splendor","hero","commuter","CNG")
bk.bike_maker_name()
print("_______")
bk1.bike_maker_name()


class Student:

   def display(self):
      print("Student Name : Anil")
      print("Course : MCA")
      print("Roll Number : 101")

s1 = Student()
s1.display()


#=============================== Program With Attributes  ====================

class BBD_Student:
   name = "Vinay"
   course = "MCA"
   roll = 101

   def display(BBD):
      print("Name :", BBD.name)
      print("Course : ", BBD.course)
      print("Roll Number : ", BBD.roll)
s2 = BBD_Student()  
s2.display()
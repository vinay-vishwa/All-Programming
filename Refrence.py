class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def __eq__(self, other):
        return self.name == other.name and self.marks == other.marks

s1 = Student("Vinay",90)
s2 = Student("Vikas",95)
s3 = s1
print("s1 is s2:",s1 is s2)
print("s1==s3:",s1==s3)
    
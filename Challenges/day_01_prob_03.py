def Student(name ="Unknown",age =18,*args,**kwargs):
    print("Name :",name)
    print("Age : ",age)
    print("Extra value:",args)
    print("Other value:",kwargs)
print()
Student()
Student("Aman",21)
Student("Ravi",age=22)
Student("Priya",20,"python","java",city="lucknow",course="MCA")
    
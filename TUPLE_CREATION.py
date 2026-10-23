''' Tuple Creation'''

number =  (10,20,30,40,50)
print("Tuple : ",number)

''' TUPLE  TRAVERSAL '''

print("Elements of Tuple: ")

for x in number:
    print(x)

'''Tuple Camparison ''' 

squares = tuple(x * x for x in number)

print("Squares :",squares)

'''                               ZIP                                '''


names = ("Amit", "Ravi", "Neha")
marks = (58,90,88)
student = tuple(zip(names,marks))

print("After ZIP() :",student)

'''          Invers Zip using ZIP(*)       '''

n,m = zip(*student)
print("Names : ",n)
print("Marks :",m)

import math

a = int(input("Enter a :- "))
b = int(input("Enter b :- "))
c = int(input("Enter c :- "))

d = (b * b) - (4 * a * b * c)
D = math.sqrt(abs(d))
r = (-b + D) / (2*a)
r1 = (-b - D) / (2 *a)
print("first root :- ",r)
print("Second Root :_",r1)

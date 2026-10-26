from functools import reduce
numbers = [1,2,3,4,5,6]
squares = list(map(lambda x: x*x,numbers))
even =list(filter(lambda x: x % 2 == 0,numbers))
total = reduce(lambda x,y: x + y,numbers)
print("Original List :",numbers)
print("Squares ",squares)
print("Even Numbers ",even)
print("Sum " , total)
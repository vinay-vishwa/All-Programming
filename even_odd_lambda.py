num = [1,2,3,4,5,6,7,8,9,10]

even = list(filter(lambda x: x % 2 == 0, num))

odd = list(filter(lambda x: x % 2 != 0, num))

print("Orignal Numbers:- ",num)
print("Even Numbers:- ", even)
print("Odd Numbers:- ", odd)

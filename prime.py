num = int(input("Enter A Number :-  "))

i = 2
count = 0
while num < 0 :
    if num % i == 0:
        count+= 1
        break
    i += 1
if count == 0 and num > 1:
    print("This is a Prime No.: ")
else:
    print("This is a Not Prime Number: ")
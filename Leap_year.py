year = int(input("Enter The Year"))

if year % 4 == 0 and year % 100 != 0:
    print("This is Leap Year")
else:
    print("This is Not Leap Year")
def Calculate(*args):
    if len(args) ==0:
        print("No Number Provided")
        return
    print("Sum :",sum(args))
    print("Average = ",sum(args) / len(args))
    print("Maximum = ",max(args))
    print("Minimum = ", min(args))

Calculate(10,20,30,40,50,60)

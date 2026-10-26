def Fibonacci(n) :
    if n <= 1:
        return n
    return Fibonacci(n - 1) + Fibonacci(n - 2)
n = int(input("Enter the Number of Terms : "))
if n <= 0:
    print("Enter a positive Number")
else:
    print("Fibonocci Series:")
    for i in range(n):
        print(Fibonacci(i), end=" ")
        
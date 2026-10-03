nums = int(input("Enter a  Number of rowa : "))

for i in range(nums):
     print(" " * (nums - i), end=" ")
     for j in range(i + 1):
          print(f"{i} C {j}", end=" ")
print()

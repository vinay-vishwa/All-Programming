class Nums:
    def __init__(self,value):
       self.value = value

    def __add__(self,other):
      return self.value + other.value

    def __sub__(self,other):
      return self.value - other.value

    def __mul__(self, other):
       return self.value * other.value

n1 = Nums(20)
n2 = Nums(10)

print("Addition", n1 + n2)
print("Subtraction", n1 - n2)
print("Multiply", n1 * n2)
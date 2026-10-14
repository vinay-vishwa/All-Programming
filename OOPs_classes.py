class Dog:
    def __init__(self,Name,Age):
        self.Name = Name
        self.Age = Age

    def bark(self):
        return f"{self.Name} Says Woof!"

my_dog  = Dog("Tommy",4)
print(my_dog.bark())
print(f"{my_dog.Name} is {my_dog.Age} Years Old")

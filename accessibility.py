class myclass:
    a = 5 
    __b = 10
    
    def Sum(self,i):
        myclass.__b += i

       
obj =myclass()
print(obj.a)
obj.Sum(2)
obj.Sum(5)
print(obj._myclass__b) 
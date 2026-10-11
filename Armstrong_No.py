nums =[1,23,23,45,65,7,6,875,3,4,554]

for n in nums:
    s = sum(int(d)**len(str(n)) for d in str(n))
    print(f"{n} >>{'armstrong' if s==n else 'not armstrong'}")
    
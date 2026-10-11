nums = [121,334,333,434,5050,123,909]

for n in nums:
    if str(n) == str(n)[::-1]:
        print(f"{n} is palindrom No.")
    else:
        print(f"{n} is not palindrom No.")
        
def twoSum(nums, Target):
    seen ={}
    for i , num in enumerate(nums):
        complement = Target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

nums = [2,7,11,15]
Target = 9
result = twoSum(nums, Target)
print(result)


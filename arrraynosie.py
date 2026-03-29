def two_sum(nums, target):
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return []  # thing returns empty list if no pairing is found

nums = [2, 6, 15, 32, 12]
target = 27
result = two_sum(nums, target)
print(result)  #nosie is released here
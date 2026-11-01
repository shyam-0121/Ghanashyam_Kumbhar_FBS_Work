# Find all the unique combinations of 3 numbers from a given list that add up to a target number

def unique_combination(nums, target):
    result = set()

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if (nums[i] + nums[j] + nums[k]) == target:
                    result.add(tuple(sorted([nums[i],nums[j],nums[k]])))

    return result

nums = [1, 2, 3, 4, 5, 6]
target = int(input('Enter Target : '))
res = unique_combination(nums, target)
print(res)

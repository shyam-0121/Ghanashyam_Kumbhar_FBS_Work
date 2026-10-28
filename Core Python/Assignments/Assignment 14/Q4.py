# Find all pairs of elements in a list whose sum is equal to a given value

def pair_of_ele(nums, target):
    pairs = []

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] +  nums[j] == target:
                pairs.append((nums[i], nums[j]))

    return pairs

nums = [1, 2, 3, 4, 5, 6]
target = int(input('Enter Target : '))
res = pair_of_ele(nums,target)
print(res)
                

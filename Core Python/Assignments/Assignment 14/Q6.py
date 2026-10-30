# Find the two numbers whose product is maximum among all pairs in a given list (use the Python set)

def two_pairs_product(nums):
    nums = list(set(nums))

    max_product = nums[0] * nums[1]
    best = nums[0],nums[1]

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            product = nums[i] * nums[j]

            if product > max_product:
                max_product = nums[i] * nums[j]
                best = ([nums[i], nums[j]])

    return best, max_product

nums = [3, 5, 2, 9, 4]
best,max_product = two_pairs_product(nums)
print(best)
print(max_product)

nums = [3,3,4,4,5,3]
def testing(nums):
    for i in range(0, len(nums), 2):
        if i == len(nums) - 1: 
            return nums[i]
        if nums[i] != nums[i + 1]:
            return nums[i]


print(testing(nums))
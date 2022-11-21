"""Given a non-empty array of integers every element appears twice expect for one find it"""

def singleNumber(nums):
    """find the single number in the array"""
    if len(nums) == 1:
        return nums[0]
    nums = sorted(nums)
    for i in range(0, len(nums), 2):
        if i == len(nums) - 1:
            return nums[i]
        if nums[i] != nums[i + 1]:
            return nums[i]
    return 0

print(singleNumber([2, 2, 3, 3, 4, 4, 1, 5, 5]))


"""Given an array  containing n distinct numbers taken from 0, 1, 2, ..., n, 
find the one that is missing from the array."""

def findTheMissingNumber(nums):
    """find the missing number"""
    if len(nums) == 0:
        return 0
    start = 0
    end = len(nums) - 1
    while start < end:
        mid = (start + end) // 2
        if nums[mid] > mid:
            end = mid
        else:
            start = mid + 1
    return start
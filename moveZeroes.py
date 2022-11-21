"""Move zeroes to the end of the list."""

def move_zeroes(nums):
    """move zeroes to the end of the list"""
    if not nums:
        return 0
    start = 0
    end = 0
    while end < len(nums):
        # if the number is not zero, move it to the start
        if nums[end] != 0: 
            nums[start] = nums[end] # move the number to the start
            start += 1
        end += 1
    while start < len(nums): # fill the rest of the list with zeroes
        nums[start] = 0
        start += 1
    return nums

print(move_zeroes([0,9,0,7,8,4,8,2,8,8,0,0,0]))
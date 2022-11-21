
def containsNearbyDuplicate(nums):
    for i in range(0, len(nums), 2):
        if i == len(nums) - 1: 
            return False
        if nums[i] == nums[i + 1]:
            return True

print(containsNearbyDuplicate([3,1,4,8,5,3]))
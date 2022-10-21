"""Container with most water"""

def maximum_area(height):
    max_area = 0 # initialize max_area
    left = 0
    right = len(height) - 1 
    while left < right: # while left and right are not the same
        max_area = max(max_area, min(height[left], height[right]) * (right - left)) 
        # max of current max_area and min of left and right * difference of left and right  
        if height[left] < height[right]: # if left is less than right
            left += 1
        else:
            right -= 1
    return max_area



print(maximum_area([5,4,2,1,4])==16)

#|
#| |     |
#| |     |
#| | |   |
#| | | | |




print(maximum_area([1,8,6,2,5,4,8,3,7]) == 49)
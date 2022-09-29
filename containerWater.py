"""Container with most water"""

def maximum_area(height):
    max_area = 1
    left = 0
    right = len(height) - 1
    while left < right:
        max_area = max(max_area, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area



print(maximum_area([5,9,2,1,4]))
print(maximum_area([1,8,6,2,5,4,8,3,7]) == 49)
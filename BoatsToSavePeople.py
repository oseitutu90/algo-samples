"""Boats to save people"""

def num_rescue_boats(people, limit):
    """Return the minimum number of boats to save people"""
    people.sort() # sort the list
    # lowest weight in front and highest weight in the back
    boats = 0
    i = 0
    j = len(people) - 1 # set j to the last index of the list
    while i <= j:
        boats += 1 # 
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
    return boats


print(num_rescue_boats([1, 2], 3) == 1)
print(num_rescue_boats([3, 2, 2, 1], 3) == 3)
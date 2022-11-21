"""Boats to save people"""

def numRescueBoats(people, limit):
    """Return the minimum number of boats to save people"""
    people.sort() # sort the list
    # lowest weight in front and highest weight in the back
    boats = 0
    i = 0
    j = len(people) - 1 # set j to the last index of the list
    while i <= j:
        boats += 1 # increase boat counts .
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
    return boats


print(numRescueBoats([1, 2], 3) == 1)
print(numRescueBoats([3, 2, 2, 1], 3) == 3)
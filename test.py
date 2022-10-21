"""first and last element in a sorted list"""

def findFirstAndLastElement(alist, item):
    """Find the first and last element in a sorted list"""
    first_index = 0
    last_index = 1
    while first_index < len(alist):
        if alist[first_index] == item:
            break
        first_index += 1
    while last_index < len(alist):
        if alist[-last_index] == item:
            break
        last_index += 1         
    return [first_index, len(alist) - last_index]

testlist = [0, 1, 2, 8, 13, 17, 13, 32, 42, 13]
print(findFirstAndLastElement(testlist, 13))
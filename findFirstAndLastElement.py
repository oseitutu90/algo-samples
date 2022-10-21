"""Find the last and first elenment in a sorted list"""
import json


def findFirstAndLastElement(alist, item):
    """Find the first and last element in a sorted list"""
    first_index = alist.index(item)
    last_index = len(alist) - alist[::-1].index(item) - 1 # reverse the list and find the index
    ans = [first_index, last_index]
    ans = json.dumps({"first_index": first_index, "last_index": last_index})
    return ans
    
testlist = [0, 1, 2, 8, 13, 17, 13, 32, 42,13]
print(findFirstAndLastElement(testlist, 13))

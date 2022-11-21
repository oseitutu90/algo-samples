"""You n versions of a software, numbered from 1 to n. 
You want to find the first bad one, which causes all the following ones to be bad. 
You are given an API bool isBadVersion(version) which will return whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API."""

def isBadVersion(version):
    """return whether version is bad"""
    if version >= 3:
        return True
    return False

def firstBadVersion(n):
    """find the first bad version"""
    if n == 1:
        return 1
    start = 1
    end = n
    while start < end: # while start and end are not the same
        mid = (start + end) // 2
        if isBadVersion(mid):
            end = mid # move the end to the middle
        else:
            start = mid + 1 # move the start to the middle + 1
    return start

print(firstBadVersion(5))


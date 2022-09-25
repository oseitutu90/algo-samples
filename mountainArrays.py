"""Mountain Arrays"""

def mountain_arrays(arr):
    if len(arr) < 3: # if array is less than 3 elements, it is not a mountain
        return False
    i = 0
    while i < len(arr) - 1 and arr[i] < arr[i + 1]: # while the array is increasing
        i += 1
        if i == 0 or i == len(arr) - 1: # if the array is increasing and the first or last element is reached,
             #it is not a mountain
            return False
    while i < len(arr) - 1 and arr[i] > arr[i + 1]: # pylint: disable=C0326
        i += 1
    return i == len(arr) - 1 # at the end of the array should be equal to the length of the array


print(mountain_arrays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(mountain_arrays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
print(mountain_arrays([1,2,5]))


# modifiy this and find the highest peak
def mountain_arrays_peak(arr):
    if len(arr) < 3:
        return False   # if array is less than 3 elements, it is not a mountain
    i = 0
    max_peak = 0 # set max peak to 0
    while i < len(arr) - 1 and arr[i] < arr[i + 1]: # while the array is increasing
        i += 1
        if i == 0 or i == len(arr) - 1:
            return False
        if arr[i] > max_peak:
            max_peak = arr[i]
    while i < len(arr) - 1 and arr[i] > arr[i + 1]: #whie the array is decreasing
        i += 1
        if arr[i] > max_peak:
            max_peak = arr[i]
    return [i == len(arr) - 1, max_peak]


print(mountain_arrays_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
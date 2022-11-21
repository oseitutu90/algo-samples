"""Mininmum number of swaps to sort an array"""

def minimum_swaps(arr):
    swaps=0
    for i in range(len(arr)):
        while arr[i] != i+1:
            temp = arr[i]
            arr[i] = arr[temp-1]
            arr[temp-1] = temp
            swaps += 1
    return swaps

print(minimum_swaps([4, 3, 1, 2]) == 3)
print(minimum_swaps([2, 3, 4, 1, 5]) == 3)
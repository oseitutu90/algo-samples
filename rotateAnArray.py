""""A left rotation operation on an array shifts each of the array's elements 1 unit to the left.
For example, if  left rotations are performed on array , then the array would become . 
Note that the lowest index item moves to the highest index in a rotation.
This is called a circular array.Given an array  of  integers and a number, , 
perform  left rotations on the array. Return the updated array to be printed as
a single line of space-separated integers."""



def rotLeft(a, d):
    """Return the rotated array."""
    return a[d:] + a[:d]

print(rotLeft([1,2,3,4,5],4) == [5,1,2,3,4])
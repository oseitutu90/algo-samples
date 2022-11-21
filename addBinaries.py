"""add binary numbers"""

def addBinaries(a, b):
    """add binary numbers"""
    a = int(a, 2)
    b = int(b, 2)
    return bin(a + b)[2:]
print(addBinaries("11", "1"))
print(addBinaries("1010", "1011"))
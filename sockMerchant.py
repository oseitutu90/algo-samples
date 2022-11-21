""""There is a large pile of socks that must be paired by color. 
Given an array of integers representing the color of each sock, 
determine how many pairs of socks with matching colors there are."""

def sock_merchant(n, ar):
    """Return the number of matching pairs of socks that John can sell."""
    pairs = 0
    ar.sort()
    i = 0
    while i < n - 1:
        if ar[i] == ar[i + 1]:
            pairs+=1 
            i += 2
        else:
            i += 1
    return pairs



print(sock_merchant(7,[1,2,1,2,1,3,2]))
# [1,1,1,2,2,2,3]

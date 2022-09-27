"""find the longest substring"""

def longest_substring(str):
    """find the longest substring"""
    if len(str) == 0:
        return 0
    if len(str) == 1:
        return 1
    longest = 1
    current = 1
    for i in range(1, len(str)):
        if str[i] == str[i-1]:
            current += 1
        else:
            if current > longest:
                longest = current
            current = 1
    if current > longest:
        longest = current
    return longest

print(longest_substring("abcabcbb"))
print(longest_substring("bbbbb"))
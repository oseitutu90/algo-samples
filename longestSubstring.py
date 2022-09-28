"""find the longest substring"""
def length_of_longest_substring(s):
    """longest contiguous substring"""
    length_of_sub = 0
    longest_sub_str = ""
    for i in range(len(s)):
        if s[i] not in longest_sub_str:
            longest_sub_str += s[i]
            length_of_sub = max(length_of_sub, len(longest_sub_str))
        else:
            longest_sub_str = longest_sub_str[longest_sub_str.index(s[i]) + 1:] + s[i]
    return length_of_sub
   
print(length_of_longest_substring("01234567893"))
print(length_of_longest_substring("pwwkew") == 3)

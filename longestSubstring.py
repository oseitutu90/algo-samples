"""find the longest substring"""
def length_of_longest_substring(s):
    """longest contiguous substring"""
    length_of_longest_substring = 0
    longest_sub_string = ""
    for i in range(len(s)):
        if s[i] not in longest_sub_string:
            longest_sub_string += s[i]
            length_of_longest_substring = max(length_of_longest_substring, len(longest_sub_string))
        else:
            longest_sub_string = longest_sub_string[longest_sub_string.index(s[i]) + 1:] + s[i] 
            # slice from the index of the first occurence of s[i] + 1 to the end of the string and add s[i] to the end
    return length_of_longest_substring
   
print(length_of_longest_substring("01234567893"))
print(length_of_longest_substring("pwwkew") == 3)

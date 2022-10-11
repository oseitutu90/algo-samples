"""find the longest substring"""
def length_of_longest_substring(s):
    """longest contiguous substring"""
    if not s:
        return 0
    start = 0
    end = 0
    max_len = 0
    # use a set to store the characters in the current substring
    char_set = set() 
    while end < len(s):
        if s[end] not in char_set:
            # if the character is not in the set, add it to the set
            char_set.add(s[end])
            end += 1
            max_len = max(max_len, end - start)
        else:
        # if the character is in the set, remove the character at the start
            char_set.remove(s[start])
            start += 1
    return max_len

   
print(length_of_longest_substring("01234567893"))
print(length_of_longest_substring("pwwkew")==3)

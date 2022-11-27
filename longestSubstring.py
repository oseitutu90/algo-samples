"""find the longest real word substring"""
# optimization required 
import enchant


def length_of_longest_substring(s):
    """find the longest real word substring"""
    if s == "":
        return 0
    else:
        max = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if checkWord(s[i:j]) and len(s[i:j]) > max:
                print(s[i:j])
                max = len(s[i:j])
    return max


def checkWord(word):
    d = enchant.Dict("en_US")
    if d.check(word):
        return True
    else:
        return False
 
 
 
print(length_of_longest_substring("Mannerism"))

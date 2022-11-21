"""Longest Palinndrime by concatenating two letter words"""
"""longestPalindrome(["lc","cl","gg"] == "lcggcl" """

def longestPalindrome(words):
    """Longest Palinndrime by concatenating two letter words"""
    words = sorted(words, key=len, reverse=True) # sort by length
    for word in words:
        for i in range(len(word)):
            if word[i:] == word[i:][::-1]:
                return word
    return ""

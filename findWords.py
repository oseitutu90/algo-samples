"""build words from alphabet set"""
import enchant

def build_words(alphabet, words):
    """build words from alphabet set"""
    # use a set to store the characters in the current substring
    alphabet_set = set(alphabet) 
    # use a set to store the words in the current substring
    words_set = set() 
    for word in words:
        word_set = set(word)
        if word_set.issubset(alphabet_set):
            
            words_set.add(word)
    return words_set

print(build_words("tahhatatahga"))



def checkWord(words):
    d = enchant.Dict("en_US")
    if d.check(words):
        return True
    else:
        return False
    
    
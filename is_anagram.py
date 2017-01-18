def is_anagram(w1,w2):
    '''
    takes two words as strings `w1` and `w2` as input and returns true if the two
    are anagrams, otherwise returns false
    '''

    if len(w1) != len(w2):
        return false

    dict1, dict2 = {},{}
    for char in w1:
        dict1[char] = dict1.get(char,0) + 1

    for char in w2:
        dict2[char] = dict2.get(char,0) + 1

    return dict1==dict2

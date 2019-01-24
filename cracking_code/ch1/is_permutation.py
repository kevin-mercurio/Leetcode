import unittest

def is_permutation(word1, word2):

    if len(word1)!=len(word2):
        return False
    
    counter = {}
    for char in word1:
        counter[char] = counter.get(char,0) + 1
        
    for char in word2:
        if char not in counter:
            return False
        else:
            if counter[char] == 0:
                return False
            counter[char] -= 1
            
    return True

class Test(unittest.testcase):

    dataT = []


    dataF:

    def test_permutation(self):

        for case in dataT:
            actual = 



if __name__ == '__main__':
    unittest.main()

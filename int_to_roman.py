"""
>>> to_roman(476)
'CDLXXVI'
"""


def to_roman(num):
    """convert an integer into a roman numeral"""
    #if 0 or negative, return False
    if num <= 0:
        return 'enter an integer >0 '

    #r_dict = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'X':10, 'I':1}

    
    



if __name__ == '__main__':
    import doctest
    doctest.testmod()

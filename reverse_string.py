"""
>>> rev_str('test')
'tset'
"""

def rev_str(in_str):

    str_list = list(in_str)
    leftmark = 0
    rightmark = len(in_str) - 1

    while leftmark < rightmark:
        str_list[leftmark], str_list[rightmark] = str_list[rightmark], str_list[leftmark]
        leftmark  += 1
        rightmark -= 1
    return ''.join(str_list)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

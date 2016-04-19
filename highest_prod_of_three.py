""""
>>> high_three([-999, -89, -100, 1000, 0,9,5,1,10])
99900000

>>> high_three([123,-100])
False
"""

def high_three(in_list):

    if len(in_list) < 3:
        return False 

    highest = max(in_list[0], in_list[1])
    lowest = min(in_list[0], in_list[1])
    lowest_2prod = (in_list[0]*in_list[1])
    highest_2prod = (in_list[0]*in_list[1])
    highest_3prod = (in_list[0]*in_list[1]*in_list[2])

    for current in in_list[2:]:
        highest_3prod = max(current*highest_2prod, current*lowest_2prod, highest_3prod)
    
        highest_2prod = max(current*highest, current*lowest, highest_2prod)
        lowest_2prod = min(current*highest, current*lowest, lowest_2prod)

        highest = max(highest, current)
        lowest = min(lowest, current)


    return highest_3prod

if __name__ == '__main__':
    import doctest
    doctest.testmod()

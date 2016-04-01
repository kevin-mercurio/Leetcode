"""
>>> check_par('()()')
True

>>> check_par('))')
False
"""


def check_par(in_str):
    """ check if parantheses are properly balanced"""
    char_list = list(in_str)
    par_stack = []
    for char in char_list:
        if char == '(':
            par_stack.append('(')
        elif char == ')' and len(par_stack) > 0:
            par_stack.pop()
        elif char == ')' and len(par_stack) == 0:
            return False
    return len(par_stack) == 0


if __name__ == '__main__':
    check_par('((()))')
    import doctest
    doctest.testmod()

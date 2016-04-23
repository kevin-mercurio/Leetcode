"""
>>> check_par('()()')
True

>>> check_par('))')
False

>>> check_par('[]{{([sdfsdf])}}')
True
"""


def check_par(in_str):
    """ check if parantheses are properly balanced"""
    char_list = list(in_str)
    par_stack = []
    for char in char_list:
        if char in ['(', '[', '{']:
            par_stack.append(char)
        elif char == ')' and len(par_stack) > 0:
            if par_stack[-1] == '(':
                par_stack.pop()
            else:
                return False
        elif char == ']'and len(par_stack) > 0:
            if par_stack[-1] == '[':
                par_stack.pop()
            else:
                return False
        elif char == '}'and len(par_stack) > 0:
            if par_stack[-1] == '{':
                par_stack.pop()
            else:
                return False

        elif char in [')', ']', '}'] and len(par_stack) == 0:
            return False
    return len(par_stack) == 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()

def find_closing(sentence='the quick (colorful (red)) fox jumps over the lazy (sleeping) dog',start=10):
        
    chars = list(sentence)
    stack_ = []
    if chars[start] != '(':
        return 'start location is not an opening parenthesis'

    #loop over the characters (this implementation creates an extra list of O(n)
    for idx, char in enumerate(chars[start:]):
        if char == '(':
            stack_.append(char)
        elif char == ')':
            stack_.pop()

        if len(stack_) == 0:
            #we closed the starting parenthesis
            return idx+start

    # if we never close it, still return a message
    return 'no closing paren found for opening paren at position {}'.format(start)

def find_closing_while(sentence='the quick (colorful (red)) fox jumps over the lazy (sleeping) dog',start=10):
        
    chars = list(sentence)
    stack_ = []
    if chars[start] != '(':
        return 'start location is not an opening parenthesis'

    i = start
    # using the while loop means we don't create another copy of the list
    while i < len(chars)-1:
        if chars[i] == '(':
            stack_.append(chars[i])
        elif chars[i] == ')':
            stack_.pop()
        if len(stack_) == 0:
            #we closed the starting parenthesis
            return i
        #increment
        i+=1

    return 'no closing paren found for opening paren at position {}'.format(start)


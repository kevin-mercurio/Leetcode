def get_pangram_letters(in_str):

    charlist = list(in_str)
    charset = set(['a','b','c','d','e','f','g','h','i',
                  'j','k','l','m','n','o','p','q','r',
                  's','t','u','v','w','x','y','z'])

    for char in charlist:
        if char in charset:
            charset.discard(char)

    print(charset)


if __name__ == '__main__':
    in_str = 'these are the elements in the string zz'
    get_pangram_letters(in_str)

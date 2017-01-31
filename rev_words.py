def rev_words_in_str(instr):
        
    in_list = instr.split()

    i,j = 0,len(in_list)-1

    while i < j:
        in_list[i], in_list[j] = in_list[j], in_list[i]
        i+=1
        j-=1

    return ' '.join(in_list)




def movie_check(flight_length, movie_lengths):
    #want to run through the list only one time at most
    #run through it and make a dict, then run through it again
    #and see if flight_length - movie_length is in the dict and return true
    t_dict = {}
    for i, t in enumerate(movie_lengths):
        if flight_length - t in t_dict.values():
            return True
        else:
            t_dict[i] = t
    return False


if __name__ == '__main__':
    print movie_check(240, [120,180,27,60, 45, 180])

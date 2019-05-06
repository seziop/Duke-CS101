def combine(first, flen, second, slen):
    return first[:flen]+second[(len(second)-slen):]
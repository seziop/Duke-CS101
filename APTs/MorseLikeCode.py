def transform(library, w):
    for x in library:
        s = x.split()
        if w == s[1]:
            return s[0]
    return "?"


def decrypt(library, message):
    ret = ""
    for w in message.split():
        char = transform(library, w)
        ret = ret + char
    return ret



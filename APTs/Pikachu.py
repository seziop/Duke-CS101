def check(word):
    syllables = ['pi','ka','chu']
    while len(word) > 0:
        if word[:2] in syllables:
            word = word[2:]
        elif word[:3] in syllables:
            word = word[3:]
        else:
            return 'NO'
    if len(word) == 0:
        return 'YES'
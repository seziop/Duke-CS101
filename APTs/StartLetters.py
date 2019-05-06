def howManyLetters(phrase):
    phrase = phrase.lower()
    phraseSplit = phrase.split()
    firstChar = []
    for i in phraseSplit:
        char = i[0]
        firstChar.append(char)
    import collections
    dictChar = collections.Counter(firstChar)
    return len(dictChar)
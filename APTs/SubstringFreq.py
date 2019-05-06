def frequency(text, n):
    words = text.split()
    substrings = []
    for word in words:
        endlim = len(word) - n
        for i in range(endlim + 1):
            substrings.append(word[i:i + n])

    d = {}
    for substring in substrings:
        if substring not in d:
            d[substring] = 0
        d[substring] += 1

    dItems = d.items()
    dItems = sorted(dItems, key=lambda x: x[1], reverse=True)

    maxVal = dItems[0][1]
    finalList = [v[0] for v in dItems if v[1] == maxVal]
    finalList = sorted(finalList)

    return finalList

def order(preferences, size, yarn):
    totalPrefYarn = 0
    dInitial = {}
    dFinal = {}
    for element in yarn:
        elementName = element.split()[0]
        elementAmt = int(element.split()[1])
        if elementName in preferences:
            totalPrefYarn += elementAmt
            dInitial[elementName] = elementAmt
    if totalPrefYarn < size:
        return []
    sizeReq = size
    while sizeReq > 0:
        for colour in preferences:
            if colour in dInitial and dInitial[colour] != 0:
                if colour not in dFinal:
                    dFinal[colour] = 0
                dFinal[colour] += 1
                dInitial[colour] -= 1
                sizeReq -= 1
                if sizeReq == 0:
                    break
    finalList = []
    for k, v in dFinal.items():
        string = k + ' ' + str(v)
        finalList.append(string)
    finalList.sort()
    return finalList
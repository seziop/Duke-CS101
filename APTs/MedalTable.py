def generate(results):
    d = {}
    for element in results:
        elementSplit = element.split()
        for index in range(3):
            country = elementSplit[index]
            if country not in d:
                d[country] = [0,0,0]
            d[country][index] += 1
    ret = []
    for key in d:
        retElementList = [key, str(d[key][0]), str(d[key][1]), str(d[key][2])]
        retValue = " ".join(retElementList)
        ret.append(retValue)
    ret = sorted(ret, key = lambda x: x.split()[0])
    ret = sorted(ret, key=lambda x: int(x.split()[3]), reverse = True)
    ret = sorted(ret, key=lambda x: int(x.split()[2]), reverse = True)
    ret = sorted(ret, key=lambda x: int(x.split()[1]), reverse = True)
    return ret
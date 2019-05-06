def freqs(data):
    d = {}
    for element in data:
        if element not in d:
            d[element] = 0
        d[element] += 1
    ret = d.items()
    ret = sorted(ret, key= lambda x: x[0])
    retList = [v[1] for v in ret]
    return retList
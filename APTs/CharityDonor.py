def nameDonor(contributions):
    import operator
    d = {}
    for x in contributions:
        data = x.split(":")
        if data[0] not in d:
            d[data[0]] = 0
        d[data[0]] += float(data[1])

    x = sorted(d.items())
    y = sorted(x, key=operator.itemgetter(1), reverse=True)
    return y[0][0]
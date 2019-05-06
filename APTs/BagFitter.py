def bags(strength, food):
    import collections
    dictFood = collections.Counter(food)
    numBags = 0
    for i in dictFood:
        itemBags = 0
        frequency = dictFood.get(i)
        if frequency % strength == 0:
            itemBags = frequency//strength
        else:
            itemBags = (frequency//strength)+1
        numBags += itemBags
    return numBags
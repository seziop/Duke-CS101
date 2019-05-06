'''
Shivansh S. Mehta (CS101-Duke Fall 2018)
NetID: sm682

RECOMMENDER PROJECT

RecommenderEngine.py | FILE 1 of 5 for this project
'''

def averages(items, ratings):
    '''
    This function calculates the average ratings for items. 
    A two-tuple is returned, where the first element is a string and the second element is a float.
    '''
    ratingsDict = {}
    for itemElement in items:
        indexVal = items.index(itemElement)
        ratingsList = []
        for i in ratings:
            ratingsVal = ratings[i][indexVal]
            if ratingsVal != 0:
                ratingsList.append(ratingsVal)
        if len(ratingsList) == 0:
            ratingsElementVal = 0.0
        else:
            ratingsElementVal = sum(ratingsList)/len(ratingsList)
        ratingsDict[itemElement] = ratingsElementVal
    ret = ratingsDict.items()
    ret = sorted(ret, key = lambda x : x[0])
    ret = sorted(ret, key = lambda x : x[1], reverse = True)
    return ret

def similarities(name, ratings):
    '''
    This function calculates how similar the rater called name is to all other raters.
    A two-tuple is returned, where the first element is a string and the second element is an integer.
    '''
    rateList1 = ratings[name]
    rateLen = len(rateList1)
    simDict = {}
    for rater2 in ratings:
        if rater2 != name:
            rateList2 = ratings[rater2]
            simList = []
            for index in range(0,rateLen):
                simVal = rateList1[index]*rateList2[index]
                simList.append(simVal)
            similarity = sum(simList)
            simDict[rater2] = int(similarity)
    ret = simDict.items()
    ret = sorted(ret, key = lambda x : x[0])
    ret = sorted(ret, key = lambda x : x[1], reverse = True)
    return ret
 
def recommendations(name, items, ratings, size):
    '''
    This function calculates the weighted average ratings and makes recommendations 
    based on the parameters and weighted average. A two-tuple is returned, where 
    the first element is a string and the second element is a float.
    '''
    simTupList = similarities(name, ratings) 
    names = [v[0] for v in simTupList[0:size]]
    simTupList = [v for v in simTupList if v[0] in names]
    simDict = dict(simTupList)
    
    rateTupList = list(ratings.items())
    rateTupList = [v for v in rateTupList if v[0] in names]
    rateDict = dict(rateTupList)
    
    for i in names:
        similarity = simDict[i]
        ratingsList = rateDict[i]
        for index in range(0,len(ratingsList)):
            ratingsList[index] = ratingsList[index]*similarity
        rateDict[i] = ratingsList
    
    return averages(items, rateDict)


if __name__ == '__main__':
    pass
    
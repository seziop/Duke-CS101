'''
Shivansh S. Mehta (CS101-Duke Fall 2018)
NetID: sm682

RECOMMENDER PROJECT

RecommenderMaker.py | FILE 5 of 5 for this project
'''

import RecommenderEngine
import MovieReader

def makerecs(name, items, ratings, size, top):
    '''
    This function calculates the top recommendations and returns a two-tuple consisting of two lists. 
    The first list is the top items rated by the rater called name (string).
    The second list is the top items not seen/rated by name (string)
    '''
    recs = dict(RecommenderEngine.recommendations(name, items, ratings, size))
    print(recs)
    ratedByName = ratings[name]
    dictlist1 = {}
    dictlist2 = {}
    for key in recs:
        index = items.index(key)
        if ratings[name][index] == 0:
            dictlist2[key] = recs[key]
        else:
            dictlist1[key] = recs[key]
    
    #Organizing List1
    list1 = dictlist1.items()
    list1 = sorted(list1, key = lambda x: x[0])
    list1 = sorted(list1, key = lambda x: x[1], reverse = True)[:top]
    
    #Organizing List2
    list2 = dictlist2.items()
    list2 = sorted(list2, key = lambda x: x[0])
    list2 = sorted(list2, key = lambda x: x[1], reverse = True)[:top]

    return (list1, list2)

if __name__ == '__main__':
    # Top 5 Movies for Student1001
    
    items,ratings = MovieReader.getdata()
    name = "student1001"
    size = 2
    top = 5
    print(makerecs(name,items,ratings,size,top))

    
    # Example Run from the Assignment Overview
    
    '''
    name = "student1367"
    items = ['127 Hours', 'The Godfather', '50 First Dates', 'A Beautiful Mind', 'A Nightmare on Elm Street', 'Alice in Wonderland', 'Anchorman: The Legend of Ron Burgundy', 'Austin Powers in Goldmember', 'Avatar', 'Black Swan']
    ratings = {'student1367':[0, 3, -5, 0, 0, 1, 5, 1, 3, 0],'student1046': [0, 0, 0, 3, 0, 0, 0, 0, 3, 5], 'student1206': [-5, 0, 1, 0, 3, 0, 5, 3, 3, 0],'student1103': [-3, 3, -3, 5, 0, 0, 5, 3, 5, 5]}
    size = 2
    top = 3
    print(makerecs(name,items,ratings,size,top))
    '''    




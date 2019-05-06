'''
Shivansh S. Mehta (CS101-Duke Fall 2018)
NetID: sm682

RECOMMENDER PROJECT

TestRecommender.py | FILE 2 of 5 for this project
'''

def driver():
    '''
    Tests averages, similarities, recommendations functions from RecommenderEngine against provided values
    '''

    import SmallDukeEatsReader 
    import RecommenderEngine

    items,ratings = SmallDukeEatsReader.getdata()
    #print("items = ",items)
    #print("ratings = ", ratings)
    
    # Testing averages
    retAvg = [('DivinityCafe', 4.0), ('TheCommons', 3.0), ('Tandoor', 2.4285714285714284), ('IlForno', 1.8), ('FarmStead', 1.4), ('LoopPizzaGrill', 1.0), ('TheSkillet', 0.0), ('PandaExpress', -0.2), ('McDonalds', -0.3333333333333333)]
    retAvgTest = RecommenderEngine.averages(items,ratings)
    
    if retAvgTest == retAvg:
        print("averages works")
    else:
        print("average NOT working")
    
    
    # Testing similarities
    retSim = [('Wei', 1), ('Sly one', -1), ('Melanie', -2), ('Sarah Lee', -6), ('J J', -14), ('Harry', -24), ('Nana Grace', -29)]
    retSimTest = RecommenderEngine.similarities("Sung-Hoon",ratings)
    
    if retSimTest == retSim:
        print("similarities works")
    else:
        print("similarities NOT working")
        
        
    # Testing recommendations
    retRec = [('Tandoor', 149.5), ('TheCommons', 128.0), ('DivinityCafe', 123.33333333333333), ('FarmStead', 69.5), ('TheSkillet', 66.0), ('LoopPizzaGrill', 62.0),  ('IlForno', 33.0), ('McDonalds', -69.5),  ('PandaExpress', -165.0)]
    retRecTest = RecommenderEngine.recommendations("Sarah Lee",items,ratings,3)
    
    if retRecTest == retRec:
        print("recommendations works")
    else:
        print("recommendations NOT working")
    

if __name__ == '__main__':
    driver()
'''
Shivansh S. Mehta (CS101-Duke Fall 2018)
NetID: sm682

RECOMMENDER PROJECT

MovieReader.py | FILE 3 of 5 for this project
'''


def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''
    st = open("data/movies.txt").readlines()
    listOfMovies = []
    listOfNames = []
    retDict = {}
    for line in st:
        elements = line.split(',')
        name = elements[0]
        movie = elements[1]
        if name not in listOfNames:
            listOfNames.append(name)
        if movie not in listOfMovies:
            listOfMovies.append(movie)
    listOfMovies = sorted(listOfMovies)
    length = len(listOfMovies)
    
    for name in listOfNames:
        retVal = [None]*length
        for line in st:
            line = line.split(',')
            if line[0] == name:
                movie = line[1]
                index = listOfMovies.index(movie)
                retVal[index] = int(line[2])
        for index in range(0,len(retVal)):
            if retVal[index] == None:
                retVal[index] = 0
        retDict[name] = retVal
    
    return (listOfMovies,retDict)

if __name__ == '__main__':
    pass
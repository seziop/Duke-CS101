'''
Shivansh S. Mehta (CS101-Duke Fall 2018)
NetID: sm682

RECOMMENDER PROJECT

BookReader.py | FILE 4 of 5 for this project
'''


def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''
    st = open("data/books.txt").readlines()
    listOfBooks = []
    retDict = {}
    
    # Making a List of Books
    
    stSplit = st[1].split(',')[1:]
    listOfBooks = [v for v in stSplit if stSplit.index(v)%2 == 0]

    # Making the Rating Dictionary
    
    for line in st:
        line = line.split(',')
        name = line[0]
        retVal = [None]*len(listOfBooks)
        for book in listOfBooks:
            lineIndex = line.index(book)
            rating = int(line[lineIndex+1])
            BookIndex = listOfBooks.index(book)
            retVal[BookIndex] = rating
            for index in range(0,len(retVal)):
                if retVal[index] == None:
                    retVal[index] = 0
        retDict[name] = retVal
    
    return (listOfBooks,retDict)

if __name__ == '__main__':
    pass
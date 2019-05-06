import csv
import collections

with open('Copy of Top 1000 Songs - Sheet1.csv') as csvfile:
    spamreader = csv.reader(csvfile)

    artists = []
    for row in spamreader:
        art = row[2]
        artists.append(art)
    print(artists)
    counter = collections.Counter(artists)
    x = list(counter.values())
    y = list(counter.keys())
    for num in range(5):
        maxIndex = -1
        maxVal = 0
        index = 0
        for i in x:
            index += 1
            if i > maxVal:
                maxVal = i
                maxIndex = index
        print(maxVal)
        x.remove(x[maxIndex])
        y.remove(y[maxIndex])


    '''
    
    for i in range(9):
        print(counter[i])
        
    '''
import random


def chapterNumber():
    val = input('What kind of Questions? a = all, c = consumer, p = producer or input chapter num (2-15) > ')
    if val == 'a':
        return random.randint(2, 15)
    if val == 'c':
        return random.randint(2, 10)
    if val == 'p':
        return random.randint(11, 15)
    else:
        return int(val)


def questionNumber(chapterNumber):
    d = {2: 17, 3: 20, 4: 14, 5: 10, 6: 16, 7: 13, 8: 11, 9: 9, 10: 16, 11: 13, 12: 10, 13: 11, 14: 12, 15: 9}
    questionRange = d[chapterNumber]
    questionNum = random.randint(1, questionRange)
    return questionNum


def run():
    bule = True
    while bule == True:
        bool = input('Want Random Question? >')
        if bool == 'y':
            bule = True
        else:
            bule = False
            return False
        chapterNum = chapterNumber()
        questionNum = questionNumber(chapterNum)
        toPrint = str(chapterNum) + '.' + str(questionNum)
        print(toPrint)
    return True


if __name__ == '__main__':
    run()


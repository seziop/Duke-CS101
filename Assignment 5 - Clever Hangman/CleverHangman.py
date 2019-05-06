'''
Shivansh S. Mehta (CS101-Duke Fall 2018)
NetID: sm682

CLEVER HANGMAN PROJECT

CleverHangman.py | FILE 1 of 1 for this project
    
'''
DEBUG = False
import random

def handleUserInputDebugMode():
    '''
    This function asks the user if they would like to play the game DEBUG mode. 
    CleverHangman will print extra information to the console if the user plays in DEBUG mode
    '''
    
    DEBUGModeInput = input('Which mode do you want: (d)ebug or (p)lay: ')
    if DEBUGModeInput == 'd':
        return True
    if DEBUGModeInput == 'p':
        return False


def handleUserInputWordLength():
    '''
    This function asks the user, how long secretWord should be and returns the int input
    '''
    wordLengthInput = input("How many letters in the word you'll guess: ")
    return int(wordLengthInput)

  
def handleUserInputDifficulty():
    '''
    This function asks the user if they would like to play the game in (h)ard or (e)asy mode, then returns the 
    corresponding number of misses allowed for the game. 
    '''
    printVal = "you'll get 12 misses unless you enter 'h' for 'hard to guess" + '\n'
    printVal += "How many misses do you want? Hard has 8 and Easy has 12"
    print(printVal) 
    difficulty = input('(h)ard or (e)asy> ')
    print()
    if difficulty == 'h':
        return 8
    if difficulty == 'e':
        return 12


def getWord(words, length):
    '''
    Selects the secret word that the user must guess. 
    This is done by randomly selecting a word from words that is of length length.
    '''
    import random
    wordsFiltered = []
    for i in words:
        if (len(i)) == length:
            wordsFiltered = wordsFiltered
            wordsFiltered.append(i)
    optionOfIndices = len(wordsFiltered)
    chosenIndex = random.randint(0, optionOfIndices-1)
    secretWord = wordsFiltered[chosenIndex]
    if DEBUG:
        print("(word is " + secretWord + ")")
        print("# possible words: " + str(len(wordsFiltered)))
    return secretWord
    

def createDisplayString(lettersGuessed, misses, hangmanWord):
    '''
    Creates the string that will be displayed to the user, using the information in the parameters.
    '''
    answer = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in lettersGuessed:
        alphabet = alphabet.replace(char,' ')
    for letter in hangmanWord:
        answer = answer + letter + ' '
    return "letters not yet guessed:" + ' ' + alphabet + '\n'+ "misses remaining =" + ' ' + str(misses) + '\n' + answer.strip()
    pass 


def handleUserInputLetterGuess(lettersGuessed, displayString):
    '''
    Prints displayString, then asks the user to input a letter to guess.
    This function handles the user input of the new letter guessed and checks if it is a repeated letter.
    '''
    
    print(displayString)
    inputX = input("letter> ")
    while inputX in lettersGuessed:
        print("you already guessed that")
        inputX = input("letter> ")
        continue
    if inputX not in lettersGuessed:
        return str(inputX)


def updateHangmanWord(guessedLetter, secretWord, hangmanWord):
    '''
    Updates hangmanWord according to whether guessedLetter is in secretWord and where in secretWord guessedLetter is in.
    '''
    if (guessedLetter not in hangmanWord):
        if (guessedLetter in secretWord):
            indexPositions = []
            index = -1
            for i in secretWord:
                index += 1
                if i == guessedLetter:
                    indexPositions.append(index)
            for index in indexPositions:
                hangmanWord[index] = guessedLetter    
    return hangmanWord


def createTemplate(currentTemplate, letterGuess, word):
    '''
    This function will create a new template for the secret word that the user will see.
    Will modify currentTemplate to reflect letterGuess
    '''
    currentTemplate = list(currentTemplate)
    if (letterGuess not in currentTemplate):
        if (letterGuess in word):
            indexPositions = []
            index = -1
            for i in word:
                index += 1
                if i == letterGuess:
                    indexPositions.append(index)
            for index in indexPositions:
                currentTemplate[index] = letterGuess
    currentTemplate = ''.join(currentTemplate)
    return currentTemplate

def getNewWordList(currentTemplate, letterGuess, wordList):
    '''
    This function constructs a dictionary of strings as the key to lists as the value. 
    It does this by calling createTemplate on every word in wordList with currentTemplate and letterGuess.
    '''
    global DEBUG
    dictionaryX = {}
    for word in wordList:
        temp = createTemplate(currentTemplate, letterGuess, word)
        if temp not in dictionaryX:
            dictionaryX[temp] = [word]
        else:
            dictionaryX[temp].append(word)
    if DEBUG:
        mylist = []
        for k,v in dictionaryX.items():
            mylist.append(k + " : " + str(len(v)))
            sortList = sorted(mylist)
        for itemList in sortList:
            print(itemList)
    if DEBUG:
        print("# keys = " + str(len(dictionaryX.items())))
    dictItems = dictionaryX.items()
    sortDictItems= sorted(dictItems, key = lambda x: len(x[1]), reverse = True)
    return sortDictItems[0]


def processUserGuess(guessedLetter, secretWord, hangmanWord, misses):
    '''
    Uses the information in the parameters to update the user's progress in the hangman game.
    '''
    index0 = updateHangmanWord(guessedLetter, secretWord, hangmanWord)
    index2 = guessedLetter in secretWord
    if index2 == False:
        misses -= 1
    index1 = misses
    return [index0, index1, index2]


def runGame(filename):
    '''
    This function sets up the game, runs each round, and prints a final message on whether or not the user won.
    True is returned if the user won the game. If the user lost the game, False is returned.
    '''
    
    global DEBUG
    file = open(filename)
    
    words = []
    for line in file:
        line = line.strip()
        words.append(line)
    
    DEBUG = handleUserInputDebugMode()
    
    length = int(handleUserInputWordLength())
    print("you'll get 12 misses unless you enter 'h' for 'hard to guess'")
    misses = handleUserInputDifficulty()
    
    previousTemplate = []
    for i in range(length):
        previousTemplate.append('_')
    
    wordList = [x for x in words if len(x) == length]
    secretWord= getWord(wordList,length)
    hangmanWord = previousTemplate
    lettersGuessed = []
    nextTemplate = ''.join(hangmanWord)
    hangmanWord = previousTemplate
    
    GUESSES = 0
    MISSES = 0
    
    while misses > 0 and hangmanWord.count('_') != 0:
        count = hangmanWord.count('_')       
        displayString = createDisplayString(lettersGuessed, misses, hangmanWord)
        guessedLetter = handleUserInputLetterGuess(lettersGuessed, displayString)      
        newWordList = getNewWordList(nextTemplate, guessedLetter, wordList)
        wordList = newWordList[1]
        lettersGuessed.append(guessedLetter)      
        countNum = hangmanWord.count('_')
        hangmanWord = list(newWordList[0])
        nextTemplate = newWordList[0]
        secretWord= getWord(wordList, length)
        if countNum == count:
            misses -= 1
            GUESSES += 1
            MISSES += 1
            LETTER = guessedLetter
            if hangmanWord.count('_') != 0:
                print("you missed:" + " " + LETTER + " " + "not in word")
        if countNum != count:
            GUESSES += 1
            continue
        processUserGuess(guessedLetter, secretWord, hangmanWord, misses) 
    
    if misses == 0:
        print("you're hung!!" + "\n" + "word is" + " " + secretWord)
        print("you made" + " " + str(GUESSES) + " " + "guesses" + " " + "with" + " " + str(MISSES) + " " + "misses")
        return False
    
    if hangmanWord.count('_') == 0:
        print("you guessed the word: " + secretWord)
        print("you made" + " " + str(GUESSES) + " " + "guesses" + " " + "with" + " " + str(MISSES) + " " + "misses")
        return True

if __name__ == "__main__":
    '''
    Running CleverHangman.py should start the game, which is done by calling runGame, therefore, we have provided you this code below.
    '''
    runGame('lowerwords.txt')

'''
Shivansh S. Mehta (CS101-Duke Fall 2018)
NetID: sm682

HANGMAN PROJECT

Hangman.py | FILE 1 of 1 for this project

Description:
        You must create a Hangman game that allows the user to play and guess a secret word.  
        See the assignment description for details.
    
'''

def handleUserInputDifficulty():
    '''
    This function asks the user if they would like to play the game in (h)ard or (e)asy mode, then returns the 
    corresponding number of misses allowed for the game. 
    '''
    print( "How many misses do you want? Hard has 8 and Easy has 12")
    difficulty = input('(h)ard or (e)asy> ')
    if difficulty == 'h':
        print('you have 8 misses to guess word' + '\n')
        return 8
    if difficulty == 'e':
        print('you have 12 misses to guess word' + '\n')
        return 12
        
def getWord(words, length):
    '''
    Selects the secret word that the user must guess. 
    This is done by randomly selecting a word from words that is of length length.
    '''
    import random
    wordsFiltered = []
    for i in words:
        if (len(i)-1) == length:
            wordsFiltered = wordsFiltered
            wordsFiltered.append(i)
    optionOfIndices = len(wordsFiltered)
    chosenIndex = random.randint(0, optionOfIndices)
    secretWord = wordsFiltered[chosenIndex]
    return secretWord[:-1]


def createDisplayString(lettersGuessed, misses, hangmanWord):
    '''
    Creates the string that will be displayed to the user, using the information in the parameters.
    '''
    sorting = lettersGuessed.sort()
    displayString = 'letters you\'ve guessed:  ' + ' '.join(lettersGuessed) + '\n'
    displayString += 'misses remaining = ' + str(misses) + '\n'
    displayString += ' '.join(hangmanWord) + '\n'
    return displayString


def handleUserInputLetterGuess(lettersGuessed, displayString):
    '''
    Prints displayString, then asks the user to input a letter to guess.
    This function handles the user input of the new letter guessed and checks if it is a repeated letter.
    '''
    
    print(displayString)
    bool = ''
    while bool != 'TRUE':
        letter = input('letter> ')
        if letter not in lettersGuessed:
            bool == 'TRUE'
            return letter
        else:
            print('you already guessed that' + '\n')

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
    import random
    
    f = open(filename)
    words = []
    
    for i in f:
        words.append(i)
        
    length = random.randint(5,10)
    secWord = (getWord(words, length))
    secretWord = []
    
    for i in secWord:
        secretWord.append(i)
        
    misses = handleUserInputDifficulty()
    initialMisses = misses
    hangmanWord = []
    numDashes = len(secretWord)
    
    for i in range(numDashes):
        hangmanWord.append('_')
    
    lettersGuessed = []
    
    while misses > 0:
        displayString = createDisplayString(lettersGuessed, misses, hangmanWord)
        guessedLetter = handleUserInputLetterGuess(lettersGuessed, displayString)
        val = processUserGuess(guessedLetter, secretWord, hangmanWord, misses)
        misses = val[1]
        hangmanWord = val[0]
        if val[2] == False:
            print("you missed: " + guessedLetter + " not in word" + '\n')
        lettersGuessed.append(guessedLetter)
        if '_' not in hangmanWord:
            break
    
    guessesMade = len(lettersGuessed)
    numMisses = initialMisses - misses
    
    if '_' not in hangmanWord:
        dis = "you guessed the word: " + ''.join(secretWord) + '\n'
        dis += "you made " + str(guessesMade) + " guesses with " +  str(numMisses) + " misses" + '\n'        
        print(dis)
        return True
    if misses == 0:
        dis = "you/'re hung!!" + '\n'
        dis += "word is " + ''.join(secretWord) + '\n'
        dis += "you made " + str(guessesMade) + " guesses with " +  str(numMisses) + " misses" + '\n'
        print(dis)
        return False


if __name__ == "__main__":
    '''
    Running Hangman.py should start the game, which is done by calling runGame, therefore, we have provided you this code below.
    '''
    runGame('lowerwords.txt')

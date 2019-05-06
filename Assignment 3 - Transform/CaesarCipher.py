'''
Shivansh S. Mehta (CS101-Duke Fall 2018)
NetID: sm682

TRANSFORM PROJECT

CaesarCipher.py | FILE 2 of 2 for this project

General Guidance:
    1. This file contains functions setShift, encrypt and findShift that correspond to the Caesar Cipher.
    2. The text files twain-csr.txt and decryptme-csr-uncsr.txt are associated to this file.
        
'''

'''
We use the following code to create variable shift with an arbitrary value, define lower and upper case alphabets and correspondingly 
assign an arbitrary value to shifted lower and upper. The rational for this is to set these as global variables which apply to all functions and 
remain constant unless they are selectively changed.

'''

shift = 3
lower_alph = "abcdefghijklmnopqrstuvwxyz"
upper_alph = lower_alph.upper()
shifted_lower = lower_alph[3:] + lower_alph[:3]
shifted_upper = upper_alph[3:] + upper_alph[:3]

def setShift(factor):
    
    '''
    As a part of setShift, we first call the global variables we previously defined. This way we can call and change the values which we do
    by assigning shift to the parameter from the function setShift and correspondingly set a formula for shifted_lower and shifted_upper
    '''
    
    global shift, shifted_lower, shifted_upper
    shift = factor
    shifted_lower = lower_alph[shift:] + lower_alph[:shift]
    shifted_upper = upper_alph[shift:] + upper_alph[:shift]
        
def encrypt(w):
    
    '''
    The encrypt function has a string (w) parameter. We first create an empty string wNew and then translate the value of each character one by one.
    This is done by finding the index position for the char in either the upper or lower alphabet and then correspondingly pulling the new alphabet 
    from the shifted_lower or shifted_upper string. Note: We need to run setShift everytime before calling encrypt otherwise, our arbitrarily defined
    values at the start would be used.
    
    We now add each character one by one to the accumulator variable wNew which is finally returned as the new word. Note: if a char is not in
    lower or upper alph, it is set to remain the same: for example '-' or other symbols/numbers.
    
    '''
    wNew = ''
    for char in w:
        if char in lower_alph:
            location = lower_alph.index(char)
            newChar = shifted_lower[location]
        elif char in upper_alph:
            location = upper_alph.index(char)
            newChar = shifted_upper[location]
        elif char not in lower_alph or upper_alph:
            newChar = char
        wNew += newChar
    return wNew

def findShift(st):
    
    '''
    The findShift func uses a string of words as the parameter to find its shift 'factor'. We do this by importing os.path (a python module that uses
    standard conventions of tracing the paths of files) and then opening the lowerword.txt file. This is literally just a list of valid words. In the
    real world, I imagine using a dictionary database for a similar purpose. We define new accumulator variables maxValid and shiftStore and then
    check to see the max number of valid words in each of the 26 possible decryptions. The shift factor with the max num of valid words is stored in 
    shiftStore and return after subtracting from 26.    
    '''
    import os.path
    file = os.path.join("data","lowerwords.txt")
    f = open(file)
    lowerwords = set(f.read().split())
    f.close()
    MaxValid = 0
    shiftScore = 0
    for i in range(26):
        setShift(i)
        newWord = [encrypt(w.lower()) for w in st.split()]
        intersection = list(set(newWord) & set(lowerwords))
        if len(intersection) >= MaxValid:
            MaxValid = len(intersection)
            shiftScore = i
    return 26-shiftScore

if __name__ == '__main__':
    
    '''
    The following are test cases for encrypt using Caesar cipher. I tested a diverse range of values values and cross referenced them manually
    '''
    
    setShift(1)
    print(encrypt('abc'))
    setShift(12)
    print(encrypt('HaPpY'))
    setShift(12)
    print(encrypt('Pacify'))
    setShift(12)
    print(encrypt('existence'))
    setShift(12)
    print(encrypt('WORM'))
    setShift(12)
    print(encrypt('bOUNDARY'))
    setShift(12)
    print(encrypt('C-O-A-T!'))
    setShift(12)
    print(encrypt('h.o.s.p.i.t.a.b.l.e'))    
    setShift(12)
    print(encrypt('no^tiFY'))

    '''
    The following is a test of the findShift func. I used the first lines of the wikipedia page on Caesar Cipher, encrypted it using an arbitrary
    shift factor (here it is 10) and then used the findShift to find that factor and print the decrypted string alongside the original
    '''

    setShift(10)
    ew = encrypt("In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques.")
    setShift(26 - findShift(ew))
    w = encrypt(ew)
    print(ew,w)

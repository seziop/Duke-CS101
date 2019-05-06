'''
Shivansh S. Mehta (CS101-Duke Fall 2018)
NetID: sm682

TRANSFORM PROJECT

PigLatin.py | FILE 1 of 2 for this project

General Guidance:
    1. This file contains functions encrypt(w) and decrypt(w) for Piglatin along with func noVowels which was used to streamline my other functions.
    2. The two text files: twain-pig.txt and twain-pig-upg.txt correspond to the transform functon from this file.
    
'''



def noVowel(s):
    
    '''
    noVowel is simply a boolean based function that checks if a character contains no vowels or not. The logic is reversed such that it returns true
    if there is no vowel and false when there is a vowel. I made this to optimize my encrypt and decrypt functions when checking if there is
    a vowel or not.  
    '''
    
    for char in s:
        if char.lower() in 'aeiouAEIOUyY':
            return False
    return True


def encrypt(w):
    
    '''
     The encrypt function contains two larger sections. Initially only the latter section was defined but after trying out multiple iterations,
     I realized that often the presence of '--' (double dash) would confuse the code and result in a different finally decrypted message. 
     Hence, I created this first section that fixes that problem.
    '''
    vowels = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
    vowelsPlusY = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U', 'y', 'Y']
    
    '''
    The following is the first section of the defined function. It effectively identifies a double dash in a word and splits the word into subwords
    based on the location of the double dashes. These subwords are translated to piglatin one by one following the provided conventions of the cryptic
    language. For example: we check if the first char is a vowel and if so, add an '-way'. Once each subword is translated, we keep appending the subwords
    to an empty list and finally rejoin is with the initial double dashes.
    '''
    if '--' in w:
        newSubword = []
        subwords = w.split('--')
        for subword in subwords:
            if len(subword) == 0:
                subwords.remove(subword)
        for subword in subwords:
            if subword[0] in vowels:
                newSubword.append(subword+'-way')
            elif subword[0] == 'q' and subword[1] in vowels:
                newSubword.append(subword[2:]+'-'+'q'+subword[1]+'ay')
            elif noVowel(w):
                newSubword.append(subword + '-way')
            else:
                x = 9999999
                for i in vowelsPlusY:
                    y = subword.find(i)
                    if y < x and y > 0:
                        x = y
                newSubword.append(subword[x:] + '-' + subword[:x] + 'ay')
        return '--'.join(newSubword)

    else:
        
        '''
        The following the second section which is more straightforward. We simply take a word, check it against the conventions of piglatin and 
        translate it    
        '''
        
        if w[0] in vowels:
            return w+'-way'
        elif w[0] == 'q' and w[1] in vowels:
            return w[2:]+'-'+'q'+w[1]+'ay'
        elif noVowel(w):
            return w + '-way'
        else:
            x = 9999999
            for i in vowelsPlusY:
                y = w.find(i)
                if y < x and y > 0:
                    x = y
            return w[x:] + '-' + w[:x] + 'ay'
    
    
def decrypt(w):
    vowels = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
    
    '''
    The first section of the decrypt, similar to that of encrypt, breaks a double dashed word and treats the subwords independently before rejoining them.
    This way we get a much more accurate decryption and avoid issues with the original '--' being misidentified as the dashes used commonly in piglatinized
    words. For decryption we try to reverse the translation conditions, for example if the word ends with '-way', we simply remove that part of the word.
    This is done with a series of if and elif statements.
    '''
    
    if '--' in w:
        newSubword = []
        subwords = w.split('--')
        for subword in subwords:
            if len(subword) == 0:
                subwords.remove(subword)
        for subword in subwords:
            if subword[-4:] == '-way':   
                newSubword.append(subword[:-4])
            elif subword[-2:] == 'ay' and subword[-3] not in vowels:
                dash = subword.find('-')
                newSubword.append(subword[(dash+1):-2] + subword[:dash])
            elif subword[-4:] == 'quay' or 'Quay':
                newSubword.append(subword[-4:-2] + subword[:-5])
        return '--'.join(newSubword)
    else:
        
        '''
        As with encryption, this second part is more straightforward and treats the words as is before returning a decrypted string.
        Note: There are discrepancies between the original text and the final decrypted message namely the behaviour around 'W + Vowel' words
        like 'would' or 'with' which often translated to 'ould' or 'ith'.        
        '''
        if w[-4:] == '-way':   
            return w[:-4]
        elif w[-2:] == 'ay' and w[-3] not in vowels:
            dash = w.find('-')
            return w[(dash+1):-2] + w[:dash]
        elif w[-4:] == 'quay' or 'Quay':
            return w[-4:-2] + w[:-5] 
        
        
if __name__ == '__main__':
    
    '''
    Encryption Tests: Here we test our encryption function by using words with different translation methods. I have also used some unique cases
    like 'one--two--three' which appeared in the twain text and I debugged my code to word with such situations.
    '''
    
    print(encrypt("oasis"))
    print(encrypt("umbrella"))
    print(encrypt("AWOL"))
    print(encrypt("computer"))
    print(encrypt("yesterday"))
    print(encrypt("strength"))
    print(encrypt("rhythm"))
    print(encrypt('"always!"'))
    print(encrypt("quiz"))
    print(encrypt("queue"))
    print(encrypt("quay"))
    print(encrypt("one--two--three"))
    print(encrypt('three-git!'''))
    
    '''
    Decryption Tests: To test the capabilities of the code, I first ran the encryption tests and then copied the output in a decrypt call.
    This way, I can cross-reference if the resultant output is same as the original encrypt parameter.
    '''
    
    print(decrypt("or-fay--I-way"))
    print(decrypt("oasis-way"))
    print(decrypt("umbrella-way"))
    print(decrypt("anchor-way"))
    print(decrypt("AWOL-way"))
    print(decrypt("omputer-cay"))
    print(decrypt("esterday-yay"))
    print(decrypt("ength-stray"))
    print(decrypt("ythm-rhay"))
    print(decrypt('always!"-"ay'))
    print(decrypt("iz-quay"))
    print(decrypt("eue-quay"))
    print(decrypt("ay-quay"))
    print(decrypt("one-way--o-tway--ee-thray"))
    print(decrypt('ee-git!-thray'))
   
    '''
    'W' tests: The following are some examples of how when encrypted and subsequently decrypted some w+vowel words do not translate well. 
    '''
    
    w = encrypt("wand")
    print(w)
    print(decrypt(w))
    
    w = encrypt("weasel")
    print(w)
    print(decrypt(w))
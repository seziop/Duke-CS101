'''
Shivansh S. Mehta (CS101-Duke Fall 2018)
NetID: sm682

TOTEM POLE PROJECT

General Guidance for the Underlying Code:
    1. I have used '#' comments for labeling the sections and functions
    2. I have used triple quotations for descriptions
    3. There are 5 head parts: Hair, Forehead (with messages), Eyes, Nose and Mouth
    4. Total Head Parts = 22 excluding selfie band
    5. Fixed Heads with description = 3; Fixed Heads with Parameters = 3
    
Enjoy :)

'''

#SECTION ONE: Parts of the head- Hair, Forehead, Eyes, Nose, Mouth, Selfie Band

#___________ Part One: Hair_______________________


def hair_frizzy(): # Hair Style One: Frizzy (Named because of the use of curly brackets)
    h1 = r"012345678901234567"
    h1 = r" {{}}{{}}{{}}{{}} " + "\n"
    h1+= r" {{}}{{}}{{}}{{}} "
    return h1



def hair_straight_long(): # Hair Style Two: Straight Long (Long in this sense is three lines of code)
    h2 = r"012345678901234567"
    h2 = r" |||||||||||||||| " + "\n"
    h2+= r" |||||||||||||||| " + "\n"
    h2+= r" |||||||||||||||| "
    return h2

def hair_curly_short(): # Hair Style Three: Curly Short (Named because of the use of o's)
    h3 = r"012345678901234567"
    h3 = r" oooooooooooooooo " + "\n"
    h3+= r" oooooooooooooooo "
    return h3

def hair_right_combed(): # Hair Style Four: Side Combed towards the Right
    h4 = r"012345678901234567"
    h4 = r" //////////////// " + "\n"
    h4+= r" //////////////// "
    return h4

def hair_left_combed(): # Hair Style Five: Side Combed towards the Left
    h5 = r"012345678901234567"
    h5 = r" \\\\\\\\\\\\\\\\ " + "\n"
    h5+= r" \\\\\\\\\\\\\\\\ "
    return h5


#___________ Part Two: Forehead_______________________

'''
Note:
    This forehead body part is distinct from the selfie band. On the instructions page, I found 
    the use of "ola" on the selfie band nice and so I thought I could communicate messages through 
    these heads. I have used rather basic messages like the golden line in CS, "Hello World" 
    as well as the age old Duke Chant "Go to Hell UNC" (Shortened as Carolina makes it longer than 
    18 characters). Some of the foreheads do not use messages and are simple designs

'''

def forehead_hello_world(): # Forehead One: Hello World (The Classic line)
    f1 = r"012345678901234567"
    f1 = r" ---------------- " + "\n"
    f1+= r" | Hello  World | " + "\n"
    f1+= r" ---------------- "
    return f1

def forehead_cross_lines(): # Forehead Two: Crosses and Lines (This is just a simple design)
    f2 = r"012345678901234567"
    f2 = r" ---------------- " + "\n"
    f2+= r" |-|x|-|xx|-|x|-| " + "\n"
    f2+= r" ---------------- "
    return f2

def forehead_colons(): # Forehead Three: Colons (Simple Design)
    f3 = r"012345678901234567"
    f3 = r" ---------------- " + "\n"
    f3+= r" |::::::::::::::| " + "\n"
    f3+= r" ---------------- "
    return f3

def forehead_love_duke(): # Forehead Four: I thought a simple I love Duke message with the fixed friendly face would be nice
    f4 = r"012345678901234567"
    f4 = r" ---------------- " + "\n"
    f4+= r" |   I <3 Duke  | " + "\n"
    f4+= r" ---------------- "
    return f4

def forehead_duke_chant(): # Forehead Five: The age old Duke Chant- Go to Hell Carolina
    f5 = r"012345678901234567"
    f5 = r" ---------------- " + "\n"
    f5+= r" |Go to Hell UNC| " + "\n"
    f5+= r" ---------------- "
    return f5

#___________ Part Three: Eyes_________________________

def eyes_glasses(): # Eyes One: Glasses (linear shape)
    e1 = r"012345678901234567"
    e1 = r" |  ___    ___  | " + "\n"
    e1+= r" | |___|--|___| | " + "\n"
    e1+= r" |              | "
    return e1

def eyes_round_staring(): # Eyes Two: Round Staring (Circular Shape)
    e2 = r"012345678901234567"
    e2 = r" /     \  /     \ " + "\n"
    e2+= r"    O   ||   O    " + "\n"
    e2+= r" \_____/  \_____/ "
    return e2

def eyes_looking_up(): # Eyes Three: Looking Up (Circular Shape)
    e3 = r"012345678901234567"
    e3 = r" /  O  \  /  O  \ " + "\n"
    e3+= r"        ||        " + "\n"
    e3+= r" \_____/  \_____/ "
    return e3

def eyes_looking_right(): # Eyes Four: Looking Right (Circular Shape)
    e4 = r"012345678901234567"
    e4 = r" /     \  /     \ " + "\n"
    e4+= r"      O ||     O  " + "\n"
    e4+= r" \_____/  \_____/ "
    return e4

def eyes_looking_left(): # Eyes Four: Looking Left (Circular Shape)
    e5 = r"012345678901234567"
    e5 = r" /     \  /     \ " + "\n"
    e5+= r"  O     || O      " + "\n"
    e5+= r" \_____/  \_____/ "
    return e5

def eyes_looking_down(): # Eyes Four: Looking Down (Circular Shape)
    e6 = r"012345678901234567"
    e6 = r" /     \  /     \ " + "\n"
    e6+= r"        ||        " + "\n"
    e6+= r" \__O__/  \__O__/ "
    return e6

#___________ Part Four: Nose_______________________

def nose_standard(): # Nose One: Standard Triangle Shaped
    n1 = r"012345678901234567"
    n1 = r" |      /\      | " + "\n"
    n1+= r" |     /__\     | "
    return n1

def nose_rightward_facing(): # Nose Two: Rightward Facing straight shape
    n2 = r"012345678901234567"
    n2 = r" |       \      | " + "\n"
    n2+= r" |      __\     | "
    return n2

def nose_leftward_facing(): # Nose Three: Leftward Facing straight shape
    n3 = r"012345678901234567"
    n3 = r" |      /       | " + "\n"
    n3+= r" |     /__      | "
    return n3

#___________ Part Five: Mouth_______________________

def mouth_standard_smile(): # Mouth One: Standard Smile
    m1 = r"012345678901234567"
    m1 = r" |    \____/    | " + "\n"
    m1+= r" |              | " + "\n"
    m1+= r" +--------------+ " 
    return m1

def mouth_expanded_long(): # Mouth Two: Expanded Long
    m2 = r"012345678901234567"
    m2 = r" |     ____     | " + "\n"
    m2+= r" |    (    )    | " + "\n"
    m2+= r" |    (____)    | " + "\n"
    m2+= r" +--------------+ " 
    return m2

def mouth_standard_neutral(): # Mouth Three: Standard Neutral
    m3 = r"012345678901234567"
    m3 = r" |   ________   | " + "\n"
    m3+= r" |              | " + "\n"
    m3+= r" +--------------+ " 
    return m3

#___________ Part Six: Selfie Band_______________________

'''
The selfie band has my netid, sm682, on it and is distinct from the forehead design. 
On the selfie totem: The selfie band goes on top of the forehead 
'''

def selfie_band(): # Selfie Band with my NetID
    s1 = r"012345678901234567"
    s1 = r" +--------------+ " + "\n"
    s1+= r" |sm682    sm682| " + "\n"
    s1+= r" +--------------+ "
    return s1

# SECTION TWO: Function Definitions

#________________Totem Fixed Definition______________________

# Fixed heads with Description

def head_cameron_crazy():
    print(hair_straight_long())
    print(forehead_duke_chant())
    print(eyes_round_staring())
    print(nose_standard())
    print(mouth_standard_neutral())

'''
Fixed Head (with Description) includes standard straight long hair with staring eyes. 
I used a standard nose and  a neutral mouth trying to imitate an aggressive look that works
with the Go to Hell Carolina look. Hence I named it the "Cameron Crazy"
'''
    
def head_friendly_face():
    print(hair_frizzy())
    print(forehead_hello_world())
    print(eyes_looking_up())
    print(nose_rightward_facing())
    print(mouth_standard_smile())
    
'''
Fixed Head (with Description) Two is a friendly warm welcoming head. I have used frizzy hair,
with the "Hello World" forehead and a confused looking combination of looking up eyes and 
smiling mouth 
'''
    
def head_left_faced():
    print(hair_left_combed())
    print(forehead_cross_lines())
    print(eyes_looking_left())
    print(nose_leftward_facing())
    print(mouth_expanded_long())
    
'''
Fixed Head (with Description) Three is a left oriented head meaning that I have used left combed hair,
the eyes are looking to the left and the nose is also leftward oriented. To make this head's nose 
different from the other 2 fixed heads with description, I have used the expanded mouth. The forehead
portays a simple design made of crosses and lines. 
'''
    
# Fixed heads with Parameters

def head_with_eyes(eyefunc):
    print(hair_straight_long())
    print(forehead_duke_chant())
    print(eyefunc)
    print(nose_standard())
    print(mouth_expanded_long())
    
'''
Fixed Head (with Parameter) One has an input-based eyefunc. I have used straight long hair in this case
with a standard nose as well as an expanded mouth. The forehead includes the go to hell carolina chant.
The programmer can pick and choose any mouth style they want into the parameter of this function.
'''

def head_with_nose(nosefunc):
    print(hair_frizzy())
    print(forehead_hello_world())
    print(eyes_looking_up())
    print(nosefunc)
    print(mouth_standard_smile())
    
'''
Fixed Head (with Parameter) Two has an input-based nosefunc. Here, I used frizzy hair, with the eyes 
looking up and a standard smiling mouth. Hence, I would call this head the parametric equivalent to the 
"friendly face" head we previously defined. The programmer can pick and choose any nose style they 
want into the parameter of this function.
'''

def head_with_mouth(mouthfunc):
    print(hair_right_combed())
    print(forehead_cross_lines())
    print(eyes_looking_right())
    print(nose_rightward_facing())
    print(mouthfunc)
    
'''
Fixed Head (with Parameter) Three is the last of the fixed heads but this one has an input-based mouthfunc.
I tried to imitate the leftward fixed head we previously defined but mirrored it to the right instead.
Hence, this head has right combed hair, right facing eyes and nose with the cross and lines forehead.
However, the programmer can pick and choose any mouth style they want into the parameter of this function.
'''

# Totem Fixed Final Definition

def totem_fixed():
    head_cameron_crazy() #The Cameron Crazy Fixed Head with description
    head_with_nose(nose_leftward_facing()) #nosefunc parametric with the leftward facing nose
    head_with_mouth(mouth_expanded_long()) #mouthfunc parametric with the expanded mouth

'''
For the final Totem Fixed Function, I have used three of the six fixed heads we previously defined. I used
the cameron crazy (fixed with description) head because its a must to have that on the final output ;)
I have also used two parametric heads with the nose and mouth parts that looked good respectively. Changing
the nose or mouth type in the parentheses below would result in a different head.
'''

#________________Totem Selfie Definition______________________

'''
For the Totem Selfie, I tried to make the format a bit more sophisticated by taking it a step further from 
the parametric fixed head by making the selfie head completely parametric.

Step one was to define a parametric head where the selfie band remains constant but every other part 
of the head can be input manually
'''

def selfie(hair ,forehead ,eyes ,nose ,mouth ):
    print (hair)
    print (selfie_band())
    print (forehead)
    print (eyes) 
    print (nose)
    print (mouth)
    
'''
Step Two is replicating the above defined parametric selfie head three times with arbitrary parts

For the first I used: Curly Hair, Hello World Forehead, Staring Eyes, Standard Nose and Neutral Mouth
For the Second, frizzy hair, cross and lines forehead, eyes looking up, right nose and a smile
Finally, I used straight hair, I love Duke forehead, glasses, left nose and expanded mouth

'''
    
def totem_selfie():
    selfie(hair_curly_short() ,forehead_hello_world() ,eyes_round_staring() ,nose_standard(), mouth_standard_neutral())
    selfie(hair_frizzy() ,forehead_cross_lines() ,eyes_looking_up() ,nose_rightward_facing(),mouth_standard_smile())
    selfie(hair_straight_long() ,forehead_love_duke() ,eyes_glasses() ,nose_leftward_facing(), mouth_expanded_long())
    
#________________Totem Random Definition______________________

'''
The final defining section of this assignment was Totem Random. Instead of directly using the methods
outlined in the instructions. I first went through the process of coding it myself. After a lot of trial
and error, it worked and so as you can see below, my code would look slightly different from what is
expected. The final outcome is the same and the defining functions are also the same.

Step One: Import the Random Module
'''

import random

'''
Step Two: Here, I used the random integer generator and assigned each result to a type of a head part
Example, I have 5 hair types which I assigned 1-5 respectively and when one calls random_hair, one of the
five types is returned randomly. This same process is repeated for every part of the head.
'''

def random_hair():
    x1 = random.randint(1,5)
    if x1 == 1:
        return hair_frizzy()
    if x1 == 2:
        return hair_straight_long()
    if x1 == 3:
        return hair_curly_short()
    if x1 == 4:
        return hair_right_combed()
    if x1 == 5:
        return hair_left_combed()
    
def random_forehead():
    x2 = random.randint(1,5)
    if x2 == 1:
        return forehead_hello_world()
    if x2 == 2:
        return forehead_cross_lines()
    if x2 == 3:
        return forehead_colons()
    if x2 == 4:
        return forehead_love_duke()
    if x2 == 5:
        return forehead_duke_chant()
    
def random_eyes():
    x3 = random.randint(1,6)
    if x3 == 1:
        return eyes_glasses()
    if x3 == 2:
        return eyes_round_staring()
    if x3 == 3:
        return eyes_looking_up()
    if x3 == 4:
        return eyes_looking_right()
    if x3 == 5:
        return eyes_looking_left()
    if x3 == 6:
        return eyes_looking_down()
    
def random_nose():
    x4 = random.randint(1,3)
    if x4 == 1:
        return nose_standard()
    if x4 == 2:
        return nose_rightward_facing()
    if x4 == 3:
        return nose_rightward_facing()

def random_mouth():
    x5 = random.randint(1,3)
    if x5 == 1:
        return mouth_standard_smile()
    if x5 == 2:
        return mouth_expanded_long()
    if x5 == 3:
        return mouth_standard_neutral()

'''
Step Three: I defined a random head with random parts function specifically to call each random part
and print it together as a head. You will see that this function is then immediately called by the
random head function just below. While it may seem redundant, a limitation to my method is that
if I call these parts in the "Random Head" function and replicate that thrice, I get the same head
printed three times. Instead by separating it into two, the code is forced to restart the randomizing
process for every time I call a random head. 
'''
def random_head_with_random_parts():
    print (random_hair())
    print (random_forehead())
    print (random_eyes())
    print (random_nose())
    print (random_mouth())

def random_head():
    random_head_with_random_parts()

'''
Step Four: Call the above defined random head function thrice
'''

def totem_random():
    random_head()
    random_head()
    random_head()
    
    
#________________MAIN______________________

if __name__ == '__main__':

    print("\nfixed totem\n")
    totem_fixed()
    
    print("\nself totem\n")
    totem_selfie()
    
    print("\nrandom totem\n")
    totem_random()
    

'''
Shivansh S. Mehta (CS101-Duke Fall 2018)
NetID: sm682

TURTLE PROJECT

DrawRandom.py | FILE 3 of 3 for this project

General Guidance:
    1. This file, once run, asks the viewer for the number of elements and then outputs that number of random sized and randomly positioned suns.
    2. I have imported the "drawOneSun" function from the TurtleShapes.py file
    3. Note: Sometimes, depending on the size and location, some resulting suns might be completely overlapped by another one and hence it is 
        important to keep a track of the number as they are appearing.
                
'''
# First we import the turtle and random module as well as the drawOneSun function from TurtleShapes

import turtle, random
from TurtleShapes import drawOneSun

def createTurtle():
    '''
    The createTurtle function aims to randomly generate a turtle at a random location. We first define the turtle and mark its speed at the fastest.
    Now, we use the randint feature as well as the Wiidth/Height of the widow to create a random location in the window.    
    '''
    turt = turtle.Turtle()
    turt.penup()
    turt.hideturtle()
    turt.speed(0)
    
    x = random.randint(-WIDTH//2, WIDTH//2)
    y = random.randint(-HEIGHT//2, HEIGHT//2)
    '''
    Since x is a random x coordinate and y is a random y coordinate, we can set turtle position to (x,y) which will be random
    '''
    
    turt.setposition(x,y)

    return turt

def randomSize():
    '''
    Now we define a random size. For the sake of simplicity and in order to not overlap a sizeable portion of the window, I am setting this pseudo random
    size to be between 5 and 100 units for the radius of the circle of the sun.   
    '''
    return random.randint(5,100)

def drawRandom(num):
    '''
    We have a random turtle at a random location and a random size which can be input as the parameters of drawOneSun when we call the function.
    Using a for loop and range being the num (inputted by the user), we can iterate this process num times.
    '''
    for i in range(num):
        randturt = createTurtle()
        drawOneSun(randturt,randomSize())

if __name__ == '__main__':
    
    '''
    The main section, defines the window, calculates the width and height of the window for use in CreateTurtle and then sets num to the answer
    to the question raised to the users. All this info will be used when we call the function drawRandom(num)
    '''
    
    sky = turtle.Screen()
    WIDTH = sky.window_width()
    HEIGHT = sky.window_height()
    num = input("number of elements> ")
    num = int(num)
    drawRandom(num)
    sky.exitonclick()
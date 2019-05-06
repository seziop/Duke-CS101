'''
Shivansh S. Mehta (CS101-Duke Fall 2018)
NetID: sm682

TURTLE PROJECT

DrawRow.py | FILE 2 of 3 for this project

General Guidance:
    1. The program replicates our predefined sun across 10 rows of 10 elements each with descending sizes
    2. The "drawOneSun" function has been imported from File 1 (TurtleShapes)
    2. While this fulfils the requirements of the assessment, I tried my best to reduce the time it takes for the turtle to draw the suns by using 10 
        different turtles simultaneously but was ultimately unsuccessful as it took me over 4 hrs to try debugging that idea and 
        it was not feasible within the assignment's timeframe.
    3. I decided to have the suns not overlapping and hence spread across a larger width and height of the window. Therefore,
        please render the turtle run window fullscreen, grab some popcorn, sit back and relax for the best viewing experience
        
'''

# First, we import the turtle module and the required function call from File One

import turtle
from TurtleShapes import drawOneSun

def drawRow(num,size, ycoord, turtle):
    """
    The drawRow function simply replicates the shape in a row by using a 'for' loop with the range being the number of elements per row.
    We first define the x-coordinate as -width but with each iteration, x variable's value is changed by adding 7 times the radius of the circle of sun
    We use seven because the shape itself spans 6 times the radius and to not overlap and leave some spacing, I used the (1+6) factor
    """
    x = -WIDTH
    for i in range(num):
        turt.setx(x)
        turt.sety(ycoord)
        drawOneSun(turt, size)
        x = x + (7*size)
        
        
def drawRowsOfRows(turtle, drawOneX):
    """
    The drawRowsOfRows function is required by the assignment and has the two prescribed parameters: turtle name and shape identifier. If drawOneX parameter
    is 'drawOneSun', it activates the if statement and replicates the sun by first using the above defined drawRow function and then reiterating
    that for 10 loops but with decreasing size (I used 20 and the 2i factor arbitrarily as it fit the window nicely) and changing y coordinate 
    in a the same way that x was changed above    
    """
    ycoord = 350
    if drawOneX == 'drawOneSun':
        for i in range(10):
            size =  20- (2*i)
            drawRow(10,size,ycoord, turtle) 
            ycoord = ycoord - (6*(size)) 

if __name__ == '__main__':
   
    """
    In this main function region, I have defined the window and a turtle, set its speed to the fastest and called for the drawRowsOfRows function.    
    """
    sky = turtle.Screen()
    turt = turtle.Turtle()
    turt.penup()
    turt.speed(0)
    turt.hideturtle()
    WIDTH = (sky.window_width())-50
    drawRowsOfRows(turt,'drawOneSun')
    sky.exitonclick()

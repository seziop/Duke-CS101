'''
Shivansh S. Mehta (CS101-Duke Fall 2018)
NetID: sm682

TURTLE PROJECT

TurtleShapes.py | FILE 1 of 3 for this project

General Guidance:
    1. After playing around with the example shapes, I decided to take a challenge and make something more complicated.
    2. Hence, I defined a function "drawOneSun" which uses two recurring shapes: a) Asymmetric Diamonds b) Circles
    3. The turtle is named in "jimmy" in honor of my roomate letting me work on this project late at night and the window is titled
        "sky" as it fits well with sun.
    
'''
# First, we import the turtle module

import turtle

def drawOneSun(turtle, size):
    """
    My chosen shape is effectively made up of two sections, the rays and the concentric circles. Each of these regions were independently defined
    and then called together
    """
    
    def drawRays(turtle, size):
        """
        The drawRays function defines the emerging rays from the center of the sun. Such a complex shape was not required by the assignment
        but I tried to challenge myself in order to understand how turtle module works as second nature. Now, I will try to explain you my steps:
        
        A for loop with variable 'i' is used. This is for each iteration of the rays, however two rays are paired into one iteration as I used
        two different colours. The source of the color codes is https://trinket.io/docs/colors. Each ray covers 10 degrees and therefore there are 36 
        total rays with alternating color. Each ray consists of a triangle with length "size" and then another adjouned triangle that is scaled 2x.
        Thus, its side length is 2*size and its central angle is half that of first's. I had to plan all of this out and use a paper to map the 
        geometry before translating the turtle's steps into code.
        """
        
        for i in range(18):
            turtle.color('#FF4500')
            turtle.begin_fill()
            turtle.right(10)
            turtle.forward(size)
            turtle.left(15)
            turtle.forward(2 * size)
            turtle.left(170)
            turtle.forward(2 * size)
            turtle.left(15)
            turtle.forward(size)
            turtle.left(170)
            turtle.left(10)
            turtle.end_fill()

            turtle.color('#800080')
            turtle.begin_fill()
            turtle.right(10)
            turtle.forward(size)
            turtle.left(15)
            turtle.forward(2 * size)
            turtle.left(170)
            turtle.forward(2 * size)
            turtle.left(15)
            turtle.forward(size)
            turtle.left(170)
            turtle.left(10)
            turtle.end_fill()

    def drawCircle(turtle, size):
        
        """
        The drawCircle function defines the concentric circles of the sun. There are five circles with five colours respectively and I used a mix
        of for loop and if statements to realize the shape.
        """
        for i in range(5):
            if i == 0:
                turtle.color('#FFFF00')
                turtle.penup()
                turtle.begin_fill()
                turtle.right(90)
                turtle.forward(size / 5 * (5 - 0))
                turtle.left(90)
                turtle.pendown()
                turtle.begin_fill()
                turtle.circle(size / 5 * (5 - 0))
                turtle.penup()
                turtle.left(90)
                turtle.forward(size / 5 * (5 - 0))
                turtle.right(90)
                turtle.end_fill()
                turtle.pendown()

            elif i == 1:
                turtle.color('#FFA500')
                turtle.penup()
                turtle.begin_fill()
                turtle.right(90)
                turtle.forward(size / 5 * (5 - 1))
                turtle.left(90)
                turtle.pendown()
                turtle.begin_fill()
                turtle.circle(size / 5 * (5 - 1))
                turtle.penup()
                turtle.left(90)
                turtle.forward(size / 5 * (5 - 1))
                turtle.right(90)
                turtle.end_fill()
                turtle.pendown()

            elif i == 2:
                turtle.color('#FF8C00')
                turtle.penup()
                turtle.begin_fill()
                turtle.right(90)
                turtle.forward(size / 5 * (5 - 2))
                turtle.left(90)
                turtle.pendown()
                turtle.begin_fill()
                turtle.circle(size / 5 * (5 - 2))
                turtle.penup()
                turtle.left(90)
                turtle.forward(size / 5 * (5 - 2))
                turtle.right(90)
                turtle.end_fill()
                turtle.pendown()

            elif i == 3:
                turtle.color('#D2691E')
                turtle.penup()
                turtle.begin_fill()
                turtle.right(90)
                turtle.forward(size / 5 * (5 - 3))
                turtle.left(90)
                turtle.pendown()
                turtle.begin_fill()
                turtle.circle(size / 5 * (5 - 3))
                turtle.penup()
                turtle.left(90)
                turtle.forward(size / 5 * (5 - 3))
                turtle.right(90)
                turtle.end_fill()
                turtle.pendown()

            elif i == 4:
                turtle.color('#B22222')
                turtle.penup()
                turtle.begin_fill()
                turtle.right(90)
                turtle.forward(size / 5 * (5 - 4))
                turtle.left(90)
                turtle.pendown()
                turtle.begin_fill()
                turtle.circle(size / 5 * (5 - 4))
                turtle.penup()
                turtle.left(90)
                turtle.forward(size / 5 * (5 - 4))
                turtle.right(90)
                turtle.end_fill()
                turtle.pendown()
                turtle.up()

    """
    Finally, now I simply call the above function definitions
    """
    
    drawRays(turtle, size)
    drawCircle(turtle, size)


if __name__ == '__main__':

    """
    In the main sections, I have defined the window and the turtle, called the defined function once, changed the location of the turtle and then
    called it again but with a smaller size
    """

    sky = turtle.Screen()
    jimmy = turtle.Turtle()
    jimmy.speed(0)
    jimmy.left(180)
    jimmy.forward(100*3)
    jimmy.right(180)
    drawOneSun(jimmy, 100)
    jimmy.forward(100 * 6)
    drawOneSun(jimmy, 100 / 2)
    sky.exitonclick()
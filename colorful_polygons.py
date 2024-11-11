import turtle
import random

#set up the screen
ws = turtle.Screen()
ws.bgcolor("#ffcccc")
ws.title("Colorful Polygons")

#set up the turtle
vlad = turtle.Turtle()
vlad.speed(0)
vlad.pensize(5)
vlad.shape("turtle")


#draw a polygon with a specified number of sides and side length
def draw_shape(sides, length):
    angle = 360 / sides
    
    for i in range(sides): #Repeat for the number of sides
        vlad.forward(length)
        vlad.left(angle)


#choose a color based on the number of sides
def choose_color(sides):
    colors = ("#f2ccff", "#ccccff", "#ccffff", "#ccffcc", "#ffffcc")
    return colors[sides % len(colors)] 
    '''accesses the color at the index given by the result of the modulo operation. 
    It ensures that no matter the numner of sides, 
    the color selection will always stay within the bounds of the colors list. 
    If sides = 5 and len(colors) = 6, then 5 % 6 = 5. 
    So, the function will return the color at index 5'''


#draw colorful polygons with different numbers of sides at random locations
def draw_colorful_polygons():

    for sides in range(3, 13): #Loop to draw polygons from triangle to dodecagon (12 sides)
        color = choose_color(sides)
        vlad.color(color)

        ## Move turtle to a random location on the screen
        vlad.penup()
        vlad.goto(random.randint(-300, 300), random.randint(-300, 300)) #Move turtle to a random position within the screen bounds (-300 to 300) for x and y
        vlad.pendown()

        # Draw polygon with 'sides' number of sides and length 80
        draw_shape(sides, 80)
        

#call the function to start drawing polygons
draw_colorful_polygons()

#complete the drawing and keep the window open
turtle.done()
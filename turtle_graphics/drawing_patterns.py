import turtle

# create drawing space
def create_window():
    window = turtle.Screen()
    window.bgcolor("red")

# shapes
def draw_square(a_turtle):
    for i in range(1,5):
        a_turtle.forward(100)
        a_turtle.right(90)


def draw_diamond(a_turtle):
    a_turtle.forward(100)
    a_turtle.right(45)
    a_turtle.forward(100)
    a_turtle.right(135)
    a_turtle.forward(100)
    a_turtle.right(45)
    a_turtle.forward(100)
    a_turtle.right(135)

# create shape
def draw_shape():
    # create instance of Turtle
    charlie = turtle.Turtle()
    charlie.shape("turtle")
    charlie.color("yellow")
    charlie.speed(2)

    for i in range(1, 73):
        # set shape Turtle instance should draw
        draw_diamond(charlie)
        # modify angle of direction
        charlie.right(5)

    charlie.right(68)
    charlie.forward(400)

def draw():
    create_window()
    draw_shape()

draw()

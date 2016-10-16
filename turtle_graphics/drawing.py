import turtle

def create_window():
    # create drawing space
    window = turtle.Screen()

    # drawing window settings
    window.bgcolor("red")

def draw_square():

    # create turtle instance
    charlie = turtle.Turtle()
    charlie.shape("turtle")
    charlie.color("yellow")
    charlie.speed(2)

    # draw turtle movement path
    counter = 0
    while counter < 4:
        charlie.forward(100)
        charlie.right(90)
        counter += 1

def draw_circle():
    # create turtle instance
    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color("blue")

    # draw turtle movement path
    angie.circle(100)

def draw_triangle():
    # create turtle instance
    tara = turtle.Turtle()

    tara.shape("turtle")
    tara.color("green")

    # draw turtle movement path
    counter = 0
    while counter < 3:
        tara.forward(100)
        tara.right(120)
        counter += 1

def draw():
    create_window()
    draw_square()
    draw_circle()
    draw_triangle()

draw()

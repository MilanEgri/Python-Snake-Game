from turtle import Turtle
import gc
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.init()
    def init(self):

        self.turtles = []
        self.positions = []

        for i in range(3):
            turtle = Turtle()
            turtle.shape("square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(20 - (i * 20), 0)
            self.positions.append(turtle.position())
            self.turtles.append(turtle)
    def reset(self):
        for turtle in self.turtles:
            turtle.reset()
        self.init()
    def move(self):
        new_positions = self.positions[:-1]
        self.turtles[0].forward(MOVE_DISTANCE)
        self.positions = [list(self.turtles[0].position())] + new_positions
        for i in range(len(self.positions)):
            self.turtles[i].goto(self.positions[i][0], self.positions[i][1])

    def grow(self):
        turtle = Turtle()
        turtle.shape("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(self.turtles[0].position()[0], self.turtles[0].position()[1])
        self.turtles.insert(1,turtle)
        self.turtles[0].forward(MOVE_DISTANCE)
        self.positions = [list(self.turtles[0].position())] + self.positions
        for i in range(len(self.positions)):
            self.turtles[i].goto(self.positions[i][0], self.positions[i][1])

    def turn_left(self):
        self.turtles[0].left(90)

    def turn_right(self):
        self.turtles[0].right(90)

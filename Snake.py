from turtle import Turtle
MOVE_DISTANCE = 20

class Snake:
    turtles = []
    positions = []

    for i in range(3):
        turtle = Turtle()
        turtle.shape("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(20 - (i * 20), 0)
        positions.append(turtle.position())
        turtles.append(turtle)

    def move(self):
        new_positions = self.positions[:-1]
        self.turtles[0].forward(MOVE_DISTANCE)
        self.positions = [list(self.turtles[0].position())] + new_positions
        for i in range(len(self.positions)):
            self.turtles[i].goto(self.positions[i][0], self.positions[i][1])

from turtle import Turtle,Screen

screen = Screen()

screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")

turtles =[]
positions = []
def init_game():
    for i in range(3):
        turtle = Turtle()
        turtle.shape("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(20-(i*20),0)
        positions.append(turtle.position())
        turtles.append(turtle)
init_game()


screen.exitonclick()
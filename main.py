from turtle import Screen
import time
import Snake
screen = Screen()
snake = Snake.Snake()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


speed = 7





is_game_on = True
while is_game_on:
    screen.update()
    snake.move()
    time.sleep(1-(speed/10))

screen.exitonclick()
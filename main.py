from turtle import Screen
import time
from Snake import Snake
from Food import Food

screen = Screen()
snake = Snake()
food = Food()
SPEED = 9
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


screen.listen()
screen.onkey(snake.turn_left,"a")
screen.onkey(snake.turn_right,"d")
screen.onkey(snake.turn_left,"Left")
screen.onkey(snake.turn_right,"Right")

is_game_on = True
while is_game_on:
    snake.move()
    time.sleep(1-(SPEED/10))
    if snake.turtles[0].distance(food) < 15:
        food.respawn()
        snake.grow()
    screen.update()

screen.exitonclick()
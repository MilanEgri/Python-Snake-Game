from turtle import Screen
import time
import Snake
screen = Screen()
snake = Snake.Snake()
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
    screen.update()
    snake.move()
    time.sleep(1-(SPEED/10))

screen.exitonclick()
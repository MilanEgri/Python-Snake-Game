from turtle import Screen
import time
from Snake import Snake
from Food import Food
from Score import Score
screen = Screen()
snake = Snake()
scoreboard = Score()
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


screen.onkeypress(screen.bye, "Escape")

is_game_on = True
def restart_game():
    scoreboard.restart()
    snake.reset()
    food.respawn()
while is_game_on:
    snake.move()
    time.sleep(1-(SPEED/10))
    if snake.turtles[0].distance(food) < 15:
        food.respawn()
        snake.grow()
        scoreboard.getScore()

    if snake.turtles[0].xcor() > 280 or snake.turtles[0].xcor() < -280 or snake.turtles[0].ycor() > 280 or snake.turtles[0].ycor() < -280:
        restart_game()
    for segment in snake.turtles[1:]:
        if snake.turtles[0].distance(segment) <10:
            restart_game()
            break
    screen.update()


import turtle

class Score(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 25, 'bold'))

    def getScore(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 25, 'bold'))
    def restart(self):
        self.score =0
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 25, 'bold'))

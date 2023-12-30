import turtle

class Score(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.record =0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.displayScore()

    def getScore(self):
        self.score += 1
        if self.score > self.record:
            self.record =  self.score
        self.displayScore()
    def restart(self):
        self.score =0
        self.displayScore()
    def displayScore(self):
        self.clear()
        self.goto(-280, 265)
        self.write(f"Score: {self.score}", align="left", font=("Arial", 25, 'bold'))

        self.goto(280, 265)
        self.write(f"Record: {self.record}", align="right", font=("Arial", 25, 'bold'))

        self.goto(0, 275)
        self.write("Press Escape to Exit Game", align="center", font=("Arial", 10, 'normal'))


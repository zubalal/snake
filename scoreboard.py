from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_count = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: {self.score_count}', False, align=ALIGNMENT, font=FONT)

    def score(self):
        self.score_count += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", False, align=ALIGNMENT, font=("Arial", 20, "normal"))



from turtle import Turtle

FONT = ("Courier", 40, "bold")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-120, 230)
        self.write(f"{self.l_score}", align=ALIGN, font=FONT)
        self.goto(120, 230)
        self.write(f"{self.r_score}", align=ALIGN, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

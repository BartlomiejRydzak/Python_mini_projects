from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.up()
        self.color("white")
        self.ht()
        self.r_score = 0
        self.l_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.r_score, align='center', font=('Arial', 80, 'normal') )
        self.goto(100, 180)
        self.write(self.l_score, align='center', font=('Arial', 80, 'normal') )

    def add_r(self):
        self.r_score += 1
        self.update()

    def add_l(self):
        self.l_score += 1
        self.update()
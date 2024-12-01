from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 0
        self.ht()
        self.up()
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", align='center', font=FONT)

    def over(self):
        self.goto(0, 0)
        self.write("Game over", align='center', font=FONT)

    def update(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align='center', font=FONT)

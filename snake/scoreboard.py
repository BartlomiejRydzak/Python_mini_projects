from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.up()
        self.ht()
        self.goto(0, 260)
        self.update()
        

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} High score {self.highscore}", align="center", font=("Arial",24, "normal"))

    # def over(self):
    #     self.goto(0, 0)
    #     self.write("Game over", align="center", font=("Arial",24, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.highscore))
        self.score = -1
        self.update()
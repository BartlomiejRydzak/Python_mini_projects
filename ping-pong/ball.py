from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.up()
        self.x = 10
        self.y = 10
        self.move_speed = 0.05

    def move(self):
        self.goto(self.xcor() + self.x, self.ycor() + self.y )

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1

    def restart(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.05

    def speedup(self):
        self.move_speed *= 0.9
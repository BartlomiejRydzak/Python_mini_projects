from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.up()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_f(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)

        self.forward(MOVE_DISTANCE)

    def move_b(self):
        if self.ycor() > -FINISH_LINE_Y:
            self.backward(MOVE_DISTANCE)
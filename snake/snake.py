from turtle import Turtle

MOVE_DISTANSE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]
        

    def create_snake(self):
        for _ in range(3):
            self.extend((len(self.snakes)*(-20), 0))

    def move(self):
        for i in range(len(self.snakes)-1, 0, -1):
            next = self.snakes[i-1]
            self.snakes[i].goto(next.xcor(), next.ycor())
        self.head.forward(MOVE_DISTANSE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def extend(self, position):
        new = Turtle(shape="square")
        new.color("white")
        new.up()
        new.goto(position)
        self.snakes.append(new)

    def erase(self):
        for snake in self.snakes:
            snake.goto(1000, 1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]

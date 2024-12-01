from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.create_cars()

    def create_cars(self):
        for i in range(20):
            new = Turtle()
            new.shape("square")
            new.shapesize(stretch_wid=1, stretch_len=2)
            new.color(random.choice(COLORS))
            new.up()
            new.goto(50 + 30*i, random.randint(-280, 280))
            new.setheading(180)
            self.cars.append(new)
        

    def go(self):
        for car in self. cars:
            car.forward(self.speed)
            if car.xcor() < -310:
                car.goto(300, random.randint(-280, 280))

    def dist(self, p):
        for car in self.cars:
            if car.distance(p) < 20:
                return True
            
    def speed_up(self):
        self.speed += MOVE_INCREMENT
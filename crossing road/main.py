import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car = CarManager()
score = Scoreboard()

screen.onkey(player.move_f, "Up")
screen.onkey(player.move_b, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.go()

    if car.dist(player):
        score.over()
        game_is_on = False

    if player.ycor() > 280:
        car.speed_up()
        score.update()

screen.exitonclick()
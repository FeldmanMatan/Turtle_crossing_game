import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

scoreboard = Scoreboard()

# cars = []

player = Player()
car_manager = CarManager()


screen.listen()
screen.onkey(player.go_up, "Up")


# def create_car(level):
#     num_of_new_car = random.randint(0, 1)
#     for i in range(0, num_of_new_car):
#         new_car = CarManager(level)
#         cars.append(new_car)


# def move_all_car():
#     for car in cars:
#         car.move()


def squish():
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            return False
    return True


def end_if_level():
    if player.end_level is True:
        scoreboard.increase_level()
        for car in car_manager.all_cars:
            car.car_speed()


game_is_on = True

while game_is_on:
    car_manager.create_cars()
    car_manager.move_cars()
    game_is_on = squish()
    if player.is_at_finish_line():
        scoreboard.increase_level()
        car_manager.increase_car_speed()
    # end_if_level()
    time.sleep(0.1)
    screen.update()








screen.exitonclick()

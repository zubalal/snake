from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed(0)
        self.new_food()

    def new_food(self):
        x_random = random.randint(-290, 290)
        y_random = random.randint(-290, 290)
        self.goto(x_random, y_random)









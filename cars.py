from turtle import Turtle
import random

COLORS = ["red", "blue", "green", "orange", "pink", "yellow"]


class Cars(Turtle):
    def __init__(self, x_position, y_position,speed):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.speed(0)
        self.goto(x_position,y_position)
        self.dx = speed

    def is_off_screen(self):
        return self.xcor() < -300
    def hide(self):
        self.hideturtle()



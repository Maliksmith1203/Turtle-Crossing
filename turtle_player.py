from turtle import Turtle


class Turtle_player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.goto(0, -280)
        self.right(270)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def player_off_screen(self):
        return self.ycor() > 300

    def player_reset(self):
        self.goto(0,-280)

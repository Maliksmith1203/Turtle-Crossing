from turtle import Turtle


class Text_screen(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-280, 270)
        self.write(f"Level:{self.level}", align='left', font=("Courier", 15, "bold"))

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level:{self.level}", align='left', font=("Courier", 15, "bold"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center", font=("Courier",20,"bold"))
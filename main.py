from turtle import Screen
from turtle_player import Turtle_player
from cars import Cars
from text_screen import Text_screen
import time
import random

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


# Initialize player, text screen, and other variables
player = Turtle_player()
screen_text = Text_screen()
screen.onkey(fun=player.go_up, key="Up")
num_obstacles = 25
obstacles = []
obstacle_speed = [-2, -3, -2.5, -3.5, -2.2]
existing_positions = []
level = 1

# Game loop
while True:
    time.sleep(0.1)
    screen.update()

    # Remove off-screen obstacles
    obstacles = [obstacle for obstacle in obstacles if not obstacle.is_off_screen()]
    existing_positions = [obstacle.ycor() for obstacle in obstacles]

    if player.player_off_screen():
        # Player advances to the next level
        screen_text.update_level()
        player.player_reset()
        level += 1
        increase_speed_list = [i * 1.2 for i in obstacle_speed]
        obstacle_speed = increase_speed_list

        # Increase obstacle speed for existing obstacles
        for obstacle in obstacles:
            obstacle.dx *= 1.2

    for obstacle in obstacles:
        if player.distance(obstacle) < 20:
            # Player collision with an obstacle - end the game
            screen_text.game_over()
            screen.exitonclick()
            exit()

    # Generate new obstacles as needed
    while len(obstacles) < num_obstacles:
        x_position = 300
        while True:
            y_position = random.randint(-250, 250)
            if y_position not in existing_positions:
                existing_positions.append(y_position)
                break

        obstacle = Cars(x_position, y_position, speed=random.choice(obstacle_speed))
        obstacles.append(obstacle)

    # Move obstacles
    for obstacle in obstacles:
        obstacle.setx(obstacle.xcor() + obstacle.dx)

# This code will only exit when you manually close the window

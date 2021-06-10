from turtle import Turtle, Screen
import turtle as t
import random
# Etch Sketch project
# w = forwards
# S = backwards
# A = counter-clockwise(left)
# D = Cloclkwise(right)
# C = clear drawing

is_race_on = False
screen = Screen()
# Resizes screen
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
# Creates multiple turtles through for loop
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:


    for turtles in all_turtles:
        if turtles.xcor() > 230:
            is_race_on = False
            winning_color = turtles.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0,10)
        turtles.forward(random_distance)




screen.exitonclick()
#
# def move_forwards():
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.backward(10)
#
#
# def turn_right():
#     # Both do the same thing
#     # tim.right(10)
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
#
# def turn_left():
#     # Both do the same thing
#     # tim.left(10)
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
#
# def clear_screen():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="c", fun=clear_screen)
#
#
# tim.home()

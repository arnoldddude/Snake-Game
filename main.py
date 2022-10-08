import turtle
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from tkinter import messagebox


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_on = True
while game_on:
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        turtle.hideturtle()
        turtle.color("white")
        turtle.write("GAME OVER", align="center", font=("Courier", 30, "bold"))
        data = messagebox.askquestion(message="Do you want to continue")

        if data == "yes":
            scoreboard.reset()
            snake.reset()
            turtle.clear()
        else:
            game_on = False

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            turtle.hideturtle()
            turtle.color("white")
            turtle.write("GAME OVER", align="center", font=("Courier", 30, "bold"))
            data = messagebox.askquestion(message="Do you want to try again?")

            if data == "yes":
                scoreboard.reset()
                snake.reset()
                turtle.clear()
            else:
                game_on = False

screen.exitonclick()

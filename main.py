from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.listen()
screen.title("Welcome to Snake!")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        snake.make_snake()
        food.refresh()
        scoreboard.increase_score()

    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        scoreboard.reset_scoreboard()
        snake.reset()

    for snakes in snake.snake_list[3:len(snake.snake_list)]:
        if snake.head.distance(snakes) < 15:
            scoreboard.reset_scoreboard()
            snake.reset()


screen.exitonclick()

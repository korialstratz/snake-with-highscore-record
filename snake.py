from turtle import Turtle
SNAKE_LEN = 3
SNAKE_MOVEMENT = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_list = []
        self.game_snake()
        self.head = self.snake_list[0]

    def game_snake(self):
        for m in range(SNAKE_LEN):
            snake = Turtle()
            snake.shape("square")
            snake.color("white")
            snake.penup()
            self.snake_list.append(snake)

    def make_snake(self):
        position = self.snake_list[-1].position()
        x = position[0]
        y = position[0]
        new_snake = Turtle()
        new_snake.hideturtle()
        new_snake.shape("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(x, y)
        new_snake.showturtle()
        self.snake_list.append(new_snake)

    def move(self):
        for snake_num in range(len(self.snake_list) - 1, 0, -1):
            destination = self.snake_list[snake_num - 1].position()
            self.snake_list[snake_num].goto(destination)
        self.head.forward(SNAKE_MOVEMENT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for snakes in self.snake_list:
            snakes.goto(1000, 1000)
        self.snake_list.clear()
        self.game_snake()
        self.head = self.snake_list[0]

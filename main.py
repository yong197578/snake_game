import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
# all_snake = []
# x_position = [0, -20, -40]
# for snake in range(0,3):
#     new_snake = Turtle(shape="square")
#     new_snake.color("white")
#     new_snake.penup()
#     new_snake.goto(x=x_position[snake], y=0)
#     all_snake.append(new_snake)

# using tuples
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    #
    # for seg in segments:
    #     seg.forward(20)
    snake.move()
    # detect collision food (using distance method)
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
    #     if segment == snake.head:
    #         pass
    # # if head collides with any segment in the tail: then trigger Game over
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
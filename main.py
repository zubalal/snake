from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
game_is_on = True

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

while game_is_on:           #Цикл, позволяющий змейке двигаться вперед автоматически.
    #screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snake_head.distance(food) < 15:
        food.new_food()
        snake.extend()
        scoreboard.score()

    if snake.snake_head.xcor() > 290 or snake.snake_head.xcor() < -290:
        game_is_on = False
        scoreboard.game_over()
    if snake.snake_head.ycor() > 290 or snake.snake_head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()

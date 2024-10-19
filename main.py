import time
from turtle import Turtle, Screen
from snake import Snake
from score import Score_board
from food import Food
screen = Screen()
screen.title("Snake game")
screen.tracer(0)
msg = Turtle()
msg.hideturtle()
screen.listen()
screen.setup(800,650)
snake = Snake()
screen.onkey(snake.move_up,"Up" )
screen.onkey(snake.move_down,"Down" )
screen.onkey(snake.move_l,"Left" )
screen.onkey(snake.move_r,"Right" )
score = Score_board()

food = Food()
is_on = True
while is_on:
    screen.update()
    snake.move()
    time.sleep(.1)
    if snake.head.distance(food)<15:
        score.increse_score()
        snake.add_Segment()
        food.refresh()

    if snake.head.xcor()==400 or snake.head.ycor()==-320 or snake.head.xcor()==-400 or snake.head.ycor()==320:
        is_on=False
    for seg in snake.snake_body:
        if seg != snake.head:

          if snake.head.distance(seg) < 10:
            is_on = False
            msg.goto(-60,0)
            msg = msg.write("GAME OVER",font=("arial",20,"normal"))



screen.exitonclick()

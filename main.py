import time
from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard



def main()-> None:
    screen = Screen()
    snake = Snake()
    food = Food()
    
    game_is_on = True
    screen.setup(height = 600, width = 600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    score_board = ScoreBoard()


    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")
    while game_is_on:

        screen.update()
        time.sleep(0.5)
        snake.move()

        if snake.head.distance(food) < 15:
            food.refresh()
            score_board.increase_score()
            snake.extend_snake()
        if snake.head.xcor() >290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game_is_on = False
            score_board.game_over()
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                score_board.game_over()
                break


    screen.exitonclick()


if __name__ =="__main__":
    main()

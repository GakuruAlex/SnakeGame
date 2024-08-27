import time
from turtle import Screen
from snake import Snake



def main()-> None:
    screen = Screen()
    snake = Snake()
    game_is_on = True
    screen.setup(height = 600, width = 600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()


    screen.exitonclick()


if __name__ =="__main__":
    main()

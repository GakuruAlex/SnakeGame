import time
from turtle import Screen
from snake import build_snake

def main()-> None:
    screen = Screen()
    game_is_on = True
    screen.setup(height = 600, width = 600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    segments =build_snake()
    while game_is_on:
        screen.update()
        for segment in segments:
            segment.forward(20)
            time.sleep(1)

    screen.exitonclick()


if __name__ =="__main__":
    main()
import time
from turtle import Screen
from snake import build_snake


screen = Screen()
def main()-> None:

    game_is_on = True
    screen.setup(height = 600, width = 600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
   

    segments =build_snake().copy()
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        for seg_num in range(len(segments) - 1, 0,-1):
            new_x  = segments[seg_num - 1].xcor()
            new_y = segments[seg_num - 1].ycor()
            segments[seg_num].goto(new_x, new_y)
        segments[0].forward(20)


screen.exitonclick()


if __name__ =="__main__":
    main()

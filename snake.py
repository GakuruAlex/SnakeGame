from turtle import Screen, Turtle

screen = Screen()

screen.setup(height = 600, width = 600)
screen.bgcolor("black")
screen.title("Snake Game")

def build_snake()-> list:
    snake  = []
    snake_coord = [(0,0), (-20, 0), (-40, 0)]

    for coord in snake_coord:
        new_snake =Turtle(shape="square")
        new_snake.color("white")
        new_snake.goto(coord)
        snake.append(new_snake)
    return snake

build_snake()





screen.exitonclick()
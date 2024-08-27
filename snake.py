from turtle import  Turtle



def build_snake()-> list:
    snake  = []
    snake_starting_pos = [(0,0), (-20, 0), (-40, 0)]

    for position in snake_starting_pos:
        new_snake =Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        snake.append(new_snake)
    return snake








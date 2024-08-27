from turtle import  Turtle

class Snake:
    snake_starting_pos = [(0,0), (-20, 0), (-40, 0)]
    def build_snake(self)-> list:
        snake  = []
        

        for position in self.snake_starting_pos:
            new_snake =Turtle(shape="square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(position)
            snake.append(new_snake)
        return snake








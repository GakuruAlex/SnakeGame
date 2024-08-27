from turtle import  Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE  = 20
class Snake:

    def __init__(self):
        self.segments  = []
        self.build_snake()
        self.head = self.segments[0]

    def build_snake(self)-> list:

        for position in STARTING_POSITIONS:
            new_snake =Turtle(shape="square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(position)
            self.segments.append(new_snake)
        return self.segments
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0,-1):
            new_x  = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(90)
    def down(self):
        self.head.setheading(270)
    def left(self):
        self.head.setheading(180)
    def right(self):
        self.head.setheading(0)







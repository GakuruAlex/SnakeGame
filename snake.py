from turtle import  Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE  = 20
UP = 90
RIGHT =0
LEFT = 180
DOWN = 270
class Snake:

    def __init__(self):
        self.segments  = []
        self.build_snake()
        self.head = self.segments[0]

    def build_snake(self)-> list:
        """_Build a snake with three turtles_

        Returns:
            list: _A list of three turtle objects_
        """

        for position in STARTING_POSITIONS:
            new_snake =Turtle(shape="square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(position)
            self.segments.append(new_snake)
        return self.segments

    def move(self):
        """_Move the snake forward_
        """
        for seg_num in range(len(self.segments) - 1, 0,-1):
            new_x  = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """_Turn the snake up_
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        """_Turn the snake downwards_
        """
        if self.head.heading() != UP:
             self.head.setheading(270)
    def left(self):
        """_Turn the snake left_
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
    def right(self):
        """_Turn the snake right_
        """
        if self.head.heading() != LEFT:
            self.head.setheading(0)







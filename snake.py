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
    def add_segments(self, position):
        """_Add a segment_

        Args:
            position (_tuple_): _x, y position to add segment_

        Returns:
            _list_: _a list of turtle objects_
        """
        new_snake =Turtle(shape="square")

        new_snake.color("white")
        new_snake.shapesize(stretch_wid=0.5, stretch_len= 0.5)

        new_snake.penup()
        new_snake.goto(position)
        self.segments.append(new_snake)
        return self.segments

    def build_snake(self)-> list:
        """_Build a snake with three turtles_

        Returns:
            list: _A list of three turtle objects_
        """

        for position in STARTING_POSITIONS:
            self.add_segments(position)
    def extend_snake(self):
        """_Add a turtle to end of snake _
        """
        x_cor = self.segments[-1].xcor()
        y_cor  = self.segments[-1].ycor()
        self.add_segments((x_cor, y_cor))

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












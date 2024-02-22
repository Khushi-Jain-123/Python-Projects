from turtle import Turtle
MOVE_DISTANCE = 10
RIGHT = 0

LEFT = 180
UP = 90
DOWN = 270


class Snake:
    def __init__(self):
        self.positions = [(0, 0), (-20, 0), (-40, 0)]

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_segment(self):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_x = self.segments[-1].xcor() - 20
        new_y = self.segments[-1].ycor()
        self.positions.append((new_x, new_y))
        new_segment.goto(new_x, new_y)
        self.segments.append(new_segment)

    def create_snake(self):
        for position in self.positions:
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        # self.segments.clear()
        self.positions.clear()
        self.positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]



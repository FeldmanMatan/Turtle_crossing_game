from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()

        self.end_level = False
        self.setheading(90)
        self.goto(STARTING_POSITION)
       # self.level = 1

    def go_up(self):
        self.forward(MOVE_DISTANCE)
        #     return False
        # else:
        #     self.goto(STARTING_POSITION)
        #     return True

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        else:
            return False






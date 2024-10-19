from turtle import Turtle
LOCATION = [(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):

        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.next = self.snake_body[1]

    def create_snake(self):
          for loc in LOCATION:
              self.add(loc)

    def add(self,LOC):

            self.tim = Turtle("square")
            self.tim.penup()
            self.tim.goto(LOC)

            self.snake_body.append(self.tim)


    def add_Segment(self):
        self.add(self.snake_body[-1].position())


    def move(self):
        for seg in range(len(self.snake_body)-1,0,-1):
            x_cor = (self.snake_body[seg-1]).xcor()
            y_cor = (self.snake_body[seg-1]).ycor()
            self.snake_body[seg].goto(x_cor,y_cor)
        self.snake_body[0].forward(20)
    def move_up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)


    def move_down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)

    def move_l(self):
        if self.head.heading()!=360:
            self.head.setheading(180)

    def move_r(self):
        if self.head.heading()!=180:
            self.head.setheading(360)

from turtle import Turtle
class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(0,270)
        self.write(f"Score : {self.score}",False,"center",("arial",20,"normal"))


    def increse_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score}", False, "center", ("arial", 20, "normal"))

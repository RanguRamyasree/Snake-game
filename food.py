from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.x_value = random.randint(-270, 270)
        self.y_value = random.randint(-270, 270)
        self.goto(self.x_value, self.y_value)

    def refresh(self):
        self.clear()
        self.x_value = random.randint(-270, 270)
        self.y_value = random.randint(-270, 270)
        self.goto(self.x_value, self.y_value)

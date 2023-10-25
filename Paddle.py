from turtle import Turtle
from typing import Tuple


MOVE_STEP: int = 20


class Paddle(Turtle):
    def __init__(self, position: Tuple[int, int]):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self) -> None:
        new_y: float = self.ycor() + MOVE_STEP
        self.goto(self.xcor(), new_y)

    def down(self) -> None:
        new_y: float = self.ycor() - MOVE_STEP
        self.goto(self.xcor(), new_y)

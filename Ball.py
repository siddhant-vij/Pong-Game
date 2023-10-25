from turtle import Turtle
from typing import Tuple


MOVE_STEP: int = 10
MOVE_SPEED: float = 0.1


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xMove: int = MOVE_STEP
        self.yMove: int = MOVE_STEP
        self.moveSpeed: float = MOVE_SPEED

    def move(self) -> None:
        new_x: float = self.xcor() + self.xMove
        new_y: float = self.ycor() + self.yMove
        self.goto(new_x, new_y)

    def bounceY(self) -> None:
        self.yMove *= -1

    def bounceX(self) -> None:
        self.xMove *= -1
        self.moveSpeed *= 0.9

    def resetPosition(self) -> None:
        self.goto(0, 0)
        self.moveSpeed = MOVE_SPEED
        self.bounceX()

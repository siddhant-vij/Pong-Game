from turtle import Screen
from Paddle import Paddle
from Ball import Ball
from Scoreboard import Scoreboard
import time


def gameplay(maxScore: int) -> None:
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong Game")
    screen.tracer(0)

    p1: Paddle = Paddle((350, 0))
    p2: Paddle = Paddle((-350, 0))
    ball: Ball = Ball()
    scoreboard: Scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(p1.up, "Up")
    screen.onkey(p1.down, "Down")
    screen.onkey(p2.up, "w")
    screen.onkey(p2.down, "s")

    isGameOn: bool = True
    while isGameOn:
        time.sleep(ball.moveSpeed)
        screen.update()
        ball.move()
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounceY()
        if ball.distance(p1) < 50 and ball.xcor() > 320 or ball.distance(p2) < 50 and ball.xcor() < -320:
            ball.bounceX()
        if ball.xcor() > 380:
            ball.resetPosition()
            scoreboard.leftPoint()
        if ball.xcor() < -380:
            ball.resetPosition()
            scoreboard.rightPoint()
        if scoreboard.leftScore >= maxScore or scoreboard.rightScore >= maxScore:
            isGameOn = False
            scoreboard.gameOver()

    screen.exitonclick()


if __name__ == "__main__":
    gameplay(10)

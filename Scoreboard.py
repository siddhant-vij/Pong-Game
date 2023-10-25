from turtle import Turtle


ALIGN = "center"
FONT = ("Courier", 24, "normal")
FONT_BIG = ("Courier", 48, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.leftScore: int = 0
        self.rightScore: int = 0
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        self.clear()
        self.goto(-100, 200)
        self.write(self.leftScore, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.rightScore, align=ALIGN, font=FONT)

    def leftPoint(self) -> None:
        self.leftScore += 1
        self.update_scoreboard()

    def rightPoint(self) -> None:
        self.rightScore += 1
        self.update_scoreboard()

    def gameOver(self) -> None:
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT_BIG)

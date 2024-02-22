from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.score = 0
        with open("file.txt") as file:
            self.high_score = int(file.read())
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align="center",
                   font=("Arial", 15, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("file.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.color("Brown")
    #     self.clear()
    #     self.goto(0, 40)
    #     self.write("Game Over!!", move=False, align="center", font=("Arial", 40, "normal"))
    #     self.goto(0, -20)
    #     self.write(f"Final Score: {self.score}", move=False, align="center", font=("Arial", 30, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

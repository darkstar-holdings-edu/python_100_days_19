from turtle import Turtle, Screen
from tkinter import messagebox
import random


COLORS = ["red", "orange", "green", "blue", "purple"]
FINISH_LINE = 215


def create_turtle(color: str, starting_x: int, starting_y: int) -> None:
    t = Turtle(shape="turtle", visible=False)
    t.color(color)
    t.penup()
    t.setposition(x=-starting_x, y=starting_y)
    t.speed("fastest")


def main() -> None:
    screen = Screen()
    screen.setup(width=500, height=400)

    while True:
        try:
            user_bet = screen.textinput(
                title="Place your bets!",
                prompt=f"Which turtle will win the race?\nEnter color [{', '.join(COLORS)}]: ",
            ).lower()
        except AttributeError:
            exit(0)

        if user_bet not in COLORS:
            messagebox.showerror(title="Error!", message="Invalid Input. Try again!")
            continue

        break

    start_position = -100
    for num in range(5):
        create_turtle(color=COLORS[num], starting_x=230, starting_y=start_position)
        start_position += 50

    [t.showturtle() for t in screen.turtles()]

    winner = None
    while not winner:
        for t in screen.turtles():
            move = random.randint(0, 10)
            t.forward(move)
            if t.xcor() > FINISH_LINE:
                winner = t.pencolor()
                break

    message = "You won!" if winner == user_bet else "You lost."
    messagebox.showinfo(
        title="Result", message=f"{message} The winning turtle was {winner}."
    )


if __name__ == "__main__":
    main()

from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

MOVE_STEP = 10


def clear_screen() -> None:
    t.reset()


def move_right(step: int = MOVE_STEP) -> None:
    if t.heading() != 0:
        t.setheading(0)
    t.forward(step)


def move_left(step: int = MOVE_STEP) -> None:
    if t.heading() != 180:
        t.setheading(180)
    t.forward(step)


def move_up(step: int = MOVE_STEP) -> None:
    if t.heading() != 90:
        t.setheading(90)
    t.forward(step)


def move_down(step: int = MOVE_STEP) -> None:
    if t.heading() != 270:
        t.setheading(270)
    t.forward(step)


def main() -> None:
    screen.onkey(key="Right", fun=move_right)
    screen.onkey(key="Left", fun=move_left)
    screen.onkey(key="Up", fun=move_up)
    screen.onkey(key="Down", fun=move_down)
    screen.onkey(key="c", fun=clear_screen)
    screen.listen()

    screen.exitonclick()


if __name__ == "__main__":
    main()

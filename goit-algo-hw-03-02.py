"""Сніжинка Коха

Програма на Python, яка використовує рекурсію для створення фракталу
«сніжинка Коха» за умови, користувач має можливість вказати рівень
рекурсії."""

import turtle


def koch_curve(t, order, size_):
    """
    Generate a Koch curve of a given order and size.

    :param t: the turtle graphics object
    :param order: the order of the Koch curve
    :param size_: the size of the Koch curve
    :return: None
    """
    if order == 0:
        t.forward(size_)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size_ / 3)
            t.left(angle)


def draw_koch_curve(order: int, size=300):
    """
    Generate a Koch curve of a given order and size using turtle graphics.

    :param order: The order of the Koch curve (an integer).
    :param size: The size of the Koch curve (an integer, default is 300).
    :return: None
    """
    window = turtle.Screen()
    window.title("Koch curve")
    window.setup(size * 2, size * 2)
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.hideturtle()
    t.goto(-size / 2, size / 2 / 3**0.5)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()


if __name__ == "__main__":
    try:
        level = int(input("Enter the level of the curve: "))
    except ValueError:
        level = 3
        print(f"{level = }")
    try:
        size = float(input("Enter the length of the segment: "))
    except ValueError:
        size = 300
        print(f"{size = }")
    draw_koch_curve(level, size)

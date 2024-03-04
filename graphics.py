from tkinter import Canvas
from typing import Self


class Point:
    """
    two coordinates in space
    """

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"[{self.x}, {self.y}]"


class Line:
    """
    the union of two points
    """

    def __init__(self, p1=Point(0, 0), p2=Point(1, 1)):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Canvas, color: str):
        """
        render method
        """
        canvas.create_line(
            self.p1.x,
            self.p1.y,
            self.p2.x,
            self.p2.y,
            fill=color,
            width=2,
        )


class Cell:
    """
    Small box
    """

    def __init__(self, w=100, h=100, x=0, y=0, padding=0):
        self.width = w
        self.height = h
        self.x = x
        self.y = y
        self.visited = False
        self.padding = padding
        self.walls = [True, True, True, True]

    @property
    def center(self) -> Point:
        return Point(self.x + self.width / 2, self.y + self.height / 2)

    def render(self, canvas: Canvas):
        points: list[Point] = [
            Point(self.x + self.padding, self.y + self.padding),
            Point(self.x + self.width - self.padding, self.y + self.padding),
            Point(
                self.x + self.width - self.padding, self.y + self.height - self.padding
            ),
            Point(self.x + self.padding, self.y + self.height - self.padding),
        ]

        for i in range(4):
            if self.walls[i]:
                Line(points[i], points[(i + 1) % 4]).draw(canvas, "white")

    def draw_move(self, canvas: Canvas, to_cell: Self, undo=False):
        Line(self.center, to_cell.center).draw(canvas, "red" if undo else "blue")

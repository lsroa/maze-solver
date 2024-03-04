from tkinter import BOTH, Tk, Canvas

from graphics import Cell

from enum import Enum


class State(Enum):
    QUIT = 0
    RUNNING = 1


class Window:
    state: State = State.RUNNING

    def __init__(self, w=400, h=400):
        self.__root = Tk()
        self.__root.title("Maze solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self._canvas = Canvas(self.__root, width=w, height=h)
        self._canvas.pack(fill=BOTH, expand=1)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def close(self):
        self.state = State.QUIT

    def draw_cell(self, cell: Cell):
        cell.render(self._canvas)

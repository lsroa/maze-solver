from random import choice, seed as sd
from time import sleep

from graphics import Cell, Point
from window import Window


dirs: list[tuple[int, int]] = [(0, -1), (1, 0), (0, 1), (-1, 0)]


class Maze:
    def __init__(
        self,
        origin: Point,
        rows=1,
        cols=1,
        cell_width=50,
        cell_height=50,
        window: Window | None = None,
        seed=0,
    ):
        sd(seed)
        self.cols = cols
        self.rows = rows
        self.cw = cell_width
        self.ch = cell_height
        self.origin = origin
        self._win = window
        self._cells: list[list[Cell]] = [[] for _ in range(self.cols)]
        self.create_cells()
        self._open_entrance_and_exit()
        self._break_walls(0, 0)
        self._reset_cells_visited()

    def create_cells(self):
        for j in range(self.cols):
            for i in range(self.rows):
                self._cells[j].append(
                    Cell(
                        self.cw,
                        self.ch,
                        self.cw * i + int(self.origin.x),
                        self.ch * j + int(self.origin.y),
                    )
                )

    def _open_entrance_and_exit(self):
        no_walls = [False, False, False, False]

        self._cells[0][0].walls = no_walls
        self._cells[-1][-1].walls = no_walls

    def _reset_cells_visited(self):
        for j in range(self.cols):
            for i in range(self.rows):
                self._cells[j][i].visited = False

    def _break_walls(self, i: int, j: int):
        if not self._win:
            return
        self._win.redraw()

        current: Cell = self._cells[j][i]
        current.visited = True
        # pick random posible to walk
        _dirs = dirs.copy()

        while len(_dirs) > 0:
            dir = choice(_dirs)
            _x, _y = dir
            next: tuple[int, int] = (i + _x, j + _y)

            wall_index = dirs.index(dir)
            oposite_wall = (wall_index + 2) % 4

            # if you can't move pop another direction
            if (
                (next[0] < 0 or self.rows <= next[0])
                or (next[1] < 0 or self.cols <= next[1])
                or self._cells[next[1]][next[0]].visited
            ):
                _dirs.remove(dir)
                continue

            # if we can visit break the wall pointing to that cell then recurse
            if not self._win:
                return

            # remove walls
            current.walls[wall_index] = False
            self._cells[next[1]][next[0]].walls[oposite_wall] = False
            # self._cells[next[1]][next[0]].draw_move(self._win._canvas, current)

            self._break_walls(next[0], next[1])

    def _draw_cell(self, i: int, j: int):
        if not self._win:
            return
        self._win.draw_cell(self._cells[j][i])

    def solve(self) -> bool:
        return self._solve_r(0, 0)

    def _solve_r(self, i: int, j: int) -> bool:
        if self._win:
            sleep(0.1)
            self._win.redraw()

        current: Cell = self._cells[j][i]
        current.visited = True

        if current == self._cells[-1][-1]:
            return True

        for dir in dirs:
            _x, _y = dir
            next: tuple[int, int] = (i + _x, j + _y)

            is_outside = (next[0] < 0 or self.rows <= next[0]) or (
                next[1] < 0 or self.cols <= next[1]
            )
            is_wall = current.walls[dirs.index(dir)]

            if is_outside or is_wall or self._cells[next[1]][next[0]].visited:
                continue

            if not self._win:
                return False

            current.draw_move(self._win._canvas, self._cells[next[1]][next[0]])

            if self._solve_r(next[0], next[1]):
                return True
            else:
                current.draw_move(
                    self._win._canvas, self._cells[next[1]][next[0]], True
                )

        return False

    def _animate(self):
        sleep(0.01)
        if not self._win:
            return

        for j in range(self.cols):
            for i in range(self.rows):
                self._draw_cell(i, j)
                self._win.redraw()


def main():
    w = Window(300, 300)
    m = Maze(Point(15, 15), 9, 9, 30, 30, w, 25)
    m._animate()
    m.solve()


if __name__ == "__main__":
    main()

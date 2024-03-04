import unittest
from graphics import Point
from maze import Maze


class MazeTest(unittest.TestCase):
    def test_create_cells(self):
        cols = 1
        rows = 10
        m = Maze(Point(0, 0), rows, cols)
        self.assertEqual(len(m._cells), cols)
        self.assertEqual(len(m._cells[0]), rows)


if __name__ == "__main__":
    unittest.main()

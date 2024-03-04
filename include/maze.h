#pragma once

#include "graphics.h"
#include "vector"

const Point DIRS[4] = {Point(0, -1), Point(1, 0), Point(0, 1), Point(-1, 0)};

class Maze {
  Point origin = Point(0, 0);
  int cols;
  int rows;
  std::vector<std::vector<std::shared_ptr<Cell>>> cells;

 public:
  Maze(Point origin, int c, int r, int cw = 100, int ch = 100, int padding = 0)
      : origin(origin), cols(c), rows(r) {
    InitCells(cw, ch, padding);
    OpenEntranceAndExit();
    BreakWalls(0, 0);
    ResetVisited();
  }

  void Render() {
    for (int j = 0; j < cols; j++) {
      for (int i = 0; i < rows; i++) {
        cells[j][i]->Render();
      }
    }
  }

  bool Solve(int i, int j) {
    auto current = cells[j][i];
    current->visited = true;

    if (current == cells[cols - 1][rows - 1]) {
      return true;
    };

    int dir_index = 0;

    for (const auto &dir : DIRS) {
      int next[2] = {i + dir.x, j + dir.y};

      bool is_out =
          (next[0] < 0 || rows <= next[0]) || (next[1] < 0 || cols <= next[1]);

      bool is_wall = current->walls[dir_index];

      if (is_wall || is_out || cells[next[1]][next[0]]->visited) {
        dir_index++;
        continue;
      }

      current->DrawMove(cells[next[1]][next[0]]->center);

      if (Solve(next[0], next[1])) {
        return true;
      } else {
        current->DrawMove(cells[next[1]][next[0]]->center, false);
      }

      dir_index++;
    }

    return false;
  }

 private:
  void ResetVisited() {
    for (int j = 0; j < cols; j++) {
      for (int i = 0; i < rows; i++) {
        cells[j][i]->visited = false;
      }
    }
  }

  void InitCells(int cw, int ch, int padding) {
    for (int j = 0; j < cols; j++) {
      std::vector<std::shared_ptr<Cell>> row;

      for (int i = 0; i < rows; i++) {
        auto c = std::make_shared<Cell>(
            Point(origin.x + (i * cw), origin.y + (j * ch)), cw, ch, padding);
        row.push_back(c);
      }
      cells.push_back(row);
    }
  }

  void OpenEntranceAndExit() {
    for (int i = 0; i < 4; i++) {
      cells[0][0]->walls[i] = false;
      cells[cols - 1][rows - 1]->walls[i] = false;
    }
  }

  void BreakWalls(int i, int j) {
    auto current = cells[j][i];
    current->visited = true;

    std::bitset<4> dirs;

    while (!dirs.all()) {
      int index = rand() % 4;

      if (dirs[index]) {
        continue;
      }

      dirs.set(index);

      Point dir = DIRS[index];
      int next[2] = {i + dir.x, j + dir.y};

      bool is_out =
          (next[0] < 0 || rows <= next[0]) || (next[1] < 0 || cols <= next[1]);

      if ((is_out) || cells[next[1]][next[0]]->visited) {
        continue;
      }

      int opposite_index = (index + 2) % 4;

      current->walls[index] = false;
      auto next_cell = cells[next[1]][next[0]];

      next_cell->walls[opposite_index] = false;

      Line(current->center, next_cell->center, RED).Render();

      BreakWalls(next[0], next[1]);
    }
  }
};

#include "maze.h"
#include "window.h"

int main() {
  std::srand(1025);
  Window w = Window(500, 500);
  w.Init();

  Maze m = Maze(Point(20, 20), 9, 9, 50, 50);
  m.Solve(0, 0);

  w.Update(m);

  return 0;
};

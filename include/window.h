#pragma once
#include "maze.h"
#include "raylib.h"

class Window {
 public:
  int width, height;
  Window(int w, int h) : width(w), height(h){};
  ~Window() {
    //
    CloseWindow();
  };
  void Init();
  void Update(Maze& maze);
};

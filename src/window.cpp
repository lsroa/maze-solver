#include "window.h"

#include "maze.h"
#include "raylib.h"

void Window::Init() {
  InitWindow(width, height, "Maze solver");
  SetTargetFPS(60);
};

void Window::Update(Maze& maze) {
  while (!WindowShouldClose()) {
    BeginDrawing();
    ClearBackground(BLACK);

    maze.Render();

    EndDrawing();
  }
}

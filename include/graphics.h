#pragma once
#include <iostream>

#include "raylib.h"

class Point {
 public:
  int x;
  int y;
  Point() : x(0), y(0) {}
  Point(int x, int y) : x(x), y(y){};
  bool operator==(const Point& other) const {
    return other.x == x && other.y == y;
  }

  friend std::ostream& operator<<(std::ostream& out, const Point& p) {
    out << "Point {";
    out << " x: " + std::to_string(p.x) + ", y: " + std::to_string(p.y) + " }";
    return out;
  }
};

class Line {
  Point points[2];
  Color color;

 public:
  Line(Point a, Point b, Color color = WHITE) : points{a, b}, color(color) {}
  void Render() {
    auto [a, b] = points;
    DrawLine(a.x, a.y, b.x, b.y, color);
  };
};

class Cell {
  int width;
  int height;
  int padding;
  Point origin = Point(0, 0);

 public:
  bool walls[4] = {true, true, true, true};
  Point center = Point(0, 0);
  Cell(Point origin, int w, int h, int padding = 0)
      : width(w), height(h), padding(padding), origin(origin) {
    center = Point(origin.x + (w / 2), origin.y + (h / 2));
  }
  bool visited;
  friend std::ostream& operator<<(std::ostream& out, const Cell& cell) {
    out << "Cell {\n";
    out << "  center: ";
    out << cell.center << std::endl;
    out << "  origin: ";
    out << cell.origin << std::endl;
    out << "  walls: [ ";
    for (int i = 0; i < 4; i++) {
      out << std::to_string(cell.walls[i]) + " ";
    }
    out << "]\n";
    out << "}\n";
    return out;
  }

  void Render() {
    Point points[4] = {
        Point(origin.x + padding, origin.y + padding),
        Point(origin.x + width - padding, origin.y + padding),
        Point(origin.x + width - padding, origin.y + height - padding),
        Point(origin.x + padding, origin.y + height - padding),
    };

    for (int i = 0; i < 4; ++i) {
      if (walls[i]) {
        Line(points[i], points[(i + 1) % 4]).Render();
      }
    }
  }

  void DrawMove(const Point& to, bool undo = true) {
    if (undo) {
      Line(center, to, RED).Render();
    } else {
      Line(center, to, BLUE).Render();
    }
  }
};

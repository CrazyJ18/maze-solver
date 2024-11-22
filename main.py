from tkinter import Tk, BOTH, Canvas


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line():
    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas: Canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y,
            fill=fill_color, width=2
        )


class Window():
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False
    
    def draw_line(self, line: Line, fill_color):
        line.draw(self.canvas, fill_color)


class Cell():
    def __init__(self, x1, x2, y1, y2, win: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
    
    def draw(self, fill_color):
        if self.has_left_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2)),
                fill_color
                )
        if self.has_top_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)),
                fill_color
                )
        if self.has_right_wall:
            self._win.draw_line(
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)),
                fill_color
                )
        if self.has_bottom_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2)),
                fill_color
                )


def main():
    win = Window(800, 600)
    cells: list[Cell] = []
    for x in range(11, 782, 20):
        for y in range(11, 582, 20):
            cells.append(Cell(x, x+17, y, y+17, win))
    for i in range(len(cells)):
        if i % 2 == 0:
            cells[i].has_left_wall = False
        if i // 2 % 2 == 0:
            cells[i].has_top_wall = False
        if i // 4 % 2 == 0:
            cells[i].has_right_wall = False
        if i // 8 % 2 == 0:
            cells[i].has_bottom_wall = False
        cells[i].draw("black")
    win.wait_for_close()


main()
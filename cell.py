from graphics import Line, Point


class Cell():
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False
    
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self._win is None:
            return
        if self.has_left_wall:
            self._win.draw_line(Line(Point(x1, y1), Point(x1, y2)))
        else:
            self._win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "#d9d9d9")
        if self.has_top_wall:
            self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)))
        else:
            self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "#d9d9d9")
        if self.has_right_wall:
            self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        else:
            self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "#d9d9d9")
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)))
        else:
            self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "#d9d9d9")
    
    def draw_move(self, to_cell, undo=False):
        start = self._centerpoint()
        end = to_cell._centerpoint()
        if undo:
            self._win.draw_line(Line(start, end), "gray")
        else:
            self._win.draw_line(Line(start, end), "red")
    
    def _centerpoint(self):
        center_x = self._x2 - (self._x2 - self._x1) // 2
        center_y = self._y2 - (self._y2 - self._y1) // 2
        return Point(center_x, center_y)
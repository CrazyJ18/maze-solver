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
        self.root.title = "Maze"
        self.canvas = Canvas(width=width, height=height)
        self.canvas.pack()
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


def main():
    win = Window(800, 600)
    start = Point(10, 10)
    win.draw_line(Line(start, Point(790, 10)), "red")
    win.draw_line(Line(start, Point(790, 590)), "red")
    win.draw_line(Line(start, Point(10, 590)), "red")
    win.wait_for_close()


main()
from graphics import Window
from cell import Cell


def main():
    win = Window(800, 600)
    cells: list[Cell] = []
    for x in range(11, 782, 20):
        for y in range(11, 582, 20):
            cells.append(Cell(x, x+20, y, y+20, win))
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
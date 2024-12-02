from graphics import Window
from cell import Cell


def main():
    win = Window(800, 600)
    cells: list[Cell] = []
    cells.append(Cell(200, 240, 200, 240, win))
    cells.append(Cell(240, 280, 200, 240, win))
    cells.append(Cell(240, 280, 240, 280, win))
    cells[0].has_right_wall = False
    cells[1].has_left_wall = False
    cells[1].has_bottom_wall = False
    cells[2].has_top_wall = False
    for cell in cells:
        cell.draw()
    cells[0].draw_move(cells[1])
    cells[1].draw_move(cells[2])
    cells[2].draw_move(cells[1], True)
    cells[1].draw_move(cells[0], True)
    win.wait_for_close()


main()
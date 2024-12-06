from graphics import Window
from cell import Cell


def main():
    win = Window(800, 600)
    cells = [Cell(win) for i in range(3)]
    
    cells[0].has_right_wall = False
    cells[1].has_left_wall = False
    cells[1].has_bottom_wall = False
    cells[2].has_top_wall = False
    
    cells[0].draw(200, 200, 240, 240)
    cells[1].draw(240, 200, 280, 240)
    cells[2].draw(240, 240, 280, 280)
    
    cells[0].draw_move(cells[1])
    cells[1].draw_move(cells[2])
    cells[2].draw_move(cells[1], True)
    cells[1].draw_move(cells[0], True)
    
    win.wait_for_close()


main()
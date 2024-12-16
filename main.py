from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)
    
    m = Maze(5, 5, 10, 10, 40, 40, win)
    m._break_entrance_and_exit()
    
    win.wait_for_close()


main()
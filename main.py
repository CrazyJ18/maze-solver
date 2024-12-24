from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)
    
    m = Maze(5, 5, 14, 19, 40, 40, win, 9)
    m.solve()
    
    win.wait_for_close()


main()
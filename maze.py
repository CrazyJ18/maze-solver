from cell import Cell


class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
    
    def _create_cells(self):
        col = [Cell(self._win) for j in range(self._num_rows)]
        self._cells = [col for i in range(self._num_cols)]
        if self._win is None:
            return
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
        
    def _draw_cell(self, i, j):
        cell_x1 = i * self._cell_size_x + self._x1
        cell_x2 = cell_x1 + self._cell_size_x
        cell_y1 = j * self._cell_size_y + self._y1
        cell_y2 = cell_y1 + self._cell_size_y
        self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()
    
    def _animate(self):
        self._win.redraw()
        self._win._root.after(50)
from cell import Cell
import random

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y,
                 win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        if seed is not None:
            random.seed(seed)
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
    
    def _create_cells(self):
        self._cells = []
        for i in range(self._num_cols):
            self._cells.append([])
            for j in range(self._num_rows):
                self._cells[i].append(Cell(self._win))
                self._draw_cell(i, j)
        
    def _draw_cell(self, i, j):
        cell_x1 = i * self._cell_size_x + self._x1
        cell_x2 = cell_x1 + self._cell_size_x
        cell_y1 = j * self._cell_size_y + self._y1
        cell_y2 = cell_y1 + self._cell_size_y
        self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        if self._win is None:
            return
        self._animate()
    
    def _animate(self):
        self._win.redraw()
        self._win._root.after(50)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i > 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1, j))
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit.append((i, j-1))
            if i < len(self._cells) - 1 and not self._cells[i+1][j].visited:
                to_visit.append((i+1, j))
            if j < len(self._cells[i]) - 1 and not self._cells[i][j+1].visited:
                to_visit.append((i, j+1))
            if not to_visit:
                self._draw_cell(i, j)
                return
            next = to_visit.pop(random.randrange(len(to_visit)))
            if i > next[0]:
                self._cells[i][j].has_left_wall = False
                self._cells[next[0]][next[1]].has_right_wall = False
            elif i < next[0]:
                self._cells[i][j].has_right_wall = False
                self._cells[next[0]][next[1]].has_left_wall = False
            elif j > next[1]:
                self._cells[i][j].has_top_wall = False
                self._cells[next[0]][next[1]].has_bottom_wall = False
            else:
                self._cells[i][j].has_bottom_wall = False
                self._cells[next[0]][next[1]].has_top_wall = False
            self._break_walls_r(*next)
    
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
    
    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        curr: Cell = self._cells[i][j]
        curr.visited = True
        if curr is self._cells[-1][-1]:
            return True
        if not curr.has_right_wall:
            next: Cell = self._cells[i+1][j]
            if not next.has_left_wall and not next.visited:
                curr.draw_move(next)
                if self._solve_r(i+1, j):
                    return True
                curr.draw_move(next, True)
        if not curr.has_bottom_wall:
            next: Cell = self._cells[i][j+1]
            if not next.has_top_wall and not next.visited:
                curr.draw_move(next)
                if self._solve_r(i, j+1):
                    return True
                curr.draw_move(next, True)
        if not curr.has_left_wall:
            next: Cell = self._cells[i-1][j]
            if not next.has_right_wall and not next.visited:
                curr.draw_move(next)
                if self._solve_r(i-1, j):
                    return True
                curr.draw_move(next, True)
        if not curr.has_top_wall:
            next: Cell = self._cells[i][j-1]
            if not next.has_bottom_wall and not next.visited:
                curr.draw_move(next)
                if self._solve_r(i, j-1):
                    return True
                curr.draw_move(next, True)
        return False
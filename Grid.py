import sys
from termcolor import colored

# printing variaes
EMPTY = ' '
GATE = colored('#', 'red')
XLINE = colored('-', 'yellow')
YLINE = colored('|', 'yellow')
BEGIN = colored('#', 'green')
END = colored('#', 'green')
CURSOR = colored('*', 'blue')

class Grid:

    # initialize board to empty (val)ues for (col)umns and (row)s
    def __init__(self, row, col):
        self.width = col
        self.height = row
        self.total_length = 0

        # initialize 2D Array to EMPTY
        self._grid = []
        for i in range(self.height + 1):
            self._grid.append([])
            for j in range(self.width + 1):
                self._grid[i].append(EMPTY)

    # set the value to the position in the board
    def set_value(self, value, x, y):
        self._grid[y][x] = value

    # get the value from the position on the board
    def get_value(self, x, y):
        return self._grid[y][x]

    # print the full board to the console
    def print_board(self):
        for row in self._grid:
            for item in row:
                sys.stdout.write(item + '   ')
            print('\n')

    # clear the defined path & Empty
    def clear_path(self):
        for i in range(self.height + 1):
            for j in range(self.width + 1):
                if self._grid[i][j] == CURSOR:
                    self._grid[i][j] = EMPTY

    #
    def add_start_end_gates(self, start_gate, end_gate):
        self.set_value(GATE, start_gate[0], start_gate[1])
        self.set_value(GATE, end_gate[0], end_gate[1])

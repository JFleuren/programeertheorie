from collections import deque
from termcolor import colored

# import classes
from Node import Node

# define board size
board_size_width = 18
board_size_height = 13

# initialize expored array
# explored = []
# self.compass = []

# define destinations array
# x_destinations = []
# y_destinations = []

# set emty x and y coordinates
# x = []
# y = []

# set the solution object
solution = False

# printing variaes
EMPTY = ' '
GATE = colored('#', 'red')
XLINE = colored('-', 'yellow')
YLINE = colored('|', 'yellow')
BEGIN = colored('#', 'green')
END = colored('#', 'green')
CURSOR = colored('*', 'blue')

#
NORTH = 'N'
EAST = 'E'
SOUTH = 'S'
WEST = 'W'

class Bfs_function:

    # standard initializer with board
    def __init__(self, board):
        self.board = board
        self.queue = deque()
        self.path = []
        self.x = []
        self.y = []
        self.index_gate = 0
        self.x_destinations = []
        self.y_destinations = []
        self.explored = []
        self.compass = []

        # gate positions
        gates_x = [12,1,6,10,15,3,12,14,12,8,1,4,11,16,13,16,2,6,9,11,15,1,2,9,1]
        gates_y = [11,1,1,1,1,2,2,2,3,4,5,5,5,5,7,7,8,8,8,8,8,9,10,10,11]

        # netlist start and end separately
        startcoordinates = [23,5,1,15,3,7,23,22,15,20,15,13,19,22,10,11,3,2,3,20,16,19,3,15,6,7,9,22,10]
        endcoordinates = [4,7,0,21,5,13,8,13,17,10,8,18,2,11,4,24,15,20,4,19,9,5,0,5,14,9,13,16,7]

        self.netlist_counter = len(startcoordinates)

        # loopt through all the assigned element in the list
        # and append all the (start & end) locations into the list
        for i in range(0, len(gates_x)):
                 self.explored.append((gates_x[i],gates_y[i]))
                 self.board.set_value(GATE, gates_x[i], gates_y[i])
                 self.compass.append((gates_x[i],gates_y[i]))
                 self.x.append(gates_x[startcoordinates[i]])
                 self.y.append(gates_y[startcoordinates[i]])

                 self.x_destinations.append(gates_x[endcoordinates[i]])
                 self.y_destinations.append(gates_y[endcoordinates[i]])

        # set the first startchilderen
        self.makechildren(self.x[self.index_gate], self.y[self.index_gate])

        # removed the end coordinates [x,y]
        self.explored.pop(endcoordinates[self.index_gate])

    # find and calculate the childeren
    def makechildren(self, x, y):

        children = [(x-1, y, []),(x, y - 1, []),(x, y + 1, []),(x + 1, y, [])]

        for child in children:
            if child[0] >= 0 and child[1] >= 0 and child[0] <= board_size_width and child[1] <= board_size_height:
                # print child
                #print self.explored[-1]
                if not (child[0], child[1]) in self.explored:
                    if child[0] > x:
                        child[2].append(EAST)
                    elif child[0] < x:
                        child[2].append(WEST)
                    elif child[1] > y:
                        child[2].append(NORTH)
                    elif child[1] < y:
                        child[2].append(SOUTH)

                    self.queue.append(child)

                    self.explored.append((child[0], child[1]))
                    self.compass.append(child)

                    self.print_child_state(child)

        if child[0] == self.x_destinations[self.index_gate] and child[1] == self.y_destinations[self.index_gate]:

            self.lookup_next((self.x[self.index_gate], self.y[self.index_gate]), child)

            solution = True
            return solution
        else:
            solution = False
            return solution

    #
    def pop_queue_left(self):
        self.queue.popleft()

    #
    def print_child_state(self, child):
        self.board.set_value(CURSOR, child[0], child[1])
        self.board.print_board()

    #
    def get_start_gate(self):
        return (self.x[0], self.y[0])

    #
    def get_end_gate(self):
        return (self.x_destinations[0], self.y_destinations[0])

    #
    def lookup_next(self, start_child, child):

        while True:

            if child[2][0] == EAST:
                previous_child = (child[0] - 1, child[1])
                self.path.append(previous_child)
                self.board.set_value(XLINE, previous_child[0], previous_child[1])
            elif child[2][0] == WEST:
                previous_child = (child[0] + 1, child[1])
                self.path.append(previous_child)
                self.board.set_value(XLINE, previous_child[0], previous_child[1])
            elif child[2][0] == NORTH:
                previous_child = (child[0], child[1] - 1)
                self.path.append(previous_child)
                self.board.set_value(YLINE, previous_child[0], previous_child[1])
            elif child[2][0] == SOUTH:
                previous_child = (child[0], child[1] + 1)
                self.path.append(previous_child)
                self.board.set_value(YLINE, previous_child[0], previous_child[1])

            for explored_child in self.compass:
                if (explored_child[0], explored_child[1]) == (previous_child[0], previous_child[1]):
                    if (explored_child[0], explored_child[1]) == start_child:

                        return
                    else:
                        child = explored_child

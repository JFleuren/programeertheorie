from collections import deque
from termcolor import colored
import random
# import classes
from Node import Node

# define board size
board_size_width = 18
board_size_height = 13
board_size_depth = 7


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
UP = 'U'
DOWN = 'D'

class Bfs_function:

    # standard initializer with board
    def __init__(self, board):
        self.board = board
        self.queue = deque()
        self.path = []

        self.x = []
        self.y = []
        self.z = []

        self.index_gate = 0

        self.x_destinations = []
        self.y_destinations = []
        self.z_destinations = []

        self.explored = []
        self.compass = []

        # gate positions
        self.gates_x = [12,1,6,10,15,3,12,14,12,8,1,4,11,16,13,16,2,6,9,11,15,1,2,9,1]
        self.gates_y = [11,1,1,1,1,2,2,2,3,4,5,5,5,5,7,7,8,8,8,8,8,9,10,10,11]
        self.gates_z = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        # netlist start and end separately
        # self.startcoordinates = [13,19,23,5,1,15,3,7,3,23,22,15,20,15,22,10,11,3,2,3,20,16,19,3,15,6,7,9,22,10]
        # self.endcoordinates = [18,2,4,7,0,21,5,13,23,8,13,17,10,8,11,4,24,15,20,4,19,9,5,0,5,14,9,13,16,7]

        self.netlist = [(23, 8), (3, 15), (3, 0), (5, 7), (19, 2), (1, 0), (16, 9), (20, 19), (22, 16), (10, 4), (13, 18), (15, 21), (3, 4), (19, 5), (7, 9), (10, 7), (15, 5), (11, 24), (7, 13), (3, 5), (23, 4), (6, 14), (15, 17), (2, 20), (15, 8), (20, 10), (22, 11), (9, 13), (22, 13), (3, 23)]
        random.shuffle(self.netlist)
        self.netlist_counter = len(self.netlist)
        # random.shuffle(self.netlist)
        print self.netlist
        # loopt through all the assigned element in the list
        # and append all the (start & end) locations into the list
        for i in range(0, len(self.gates_x)):
                 self.board.set_value(GATE, self.gates_x[i], self.gates_y[i])
        for i in range(len(self.netlist)):
             self.x.append(self.gates_x[self.netlist[i][0]])
             self.y.append(self.gates_y[self.netlist[i][0]])
             self.z.append(self.gates_z[self.netlist[i][0]])
             self.x_destinations.append(self.gates_x[self.netlist[i][1]])
             self.y_destinations.append(self.gates_y[self.netlist[i][1]])
             self.z_destinations.append(self.gates_z[self.netlist[i][1]])
        # set the first startchilderen
        self.next_solution()

    #
    def next_solution(self):
        for i in range(len(self.gates_x)):
            self.compass.append((self.gates_x[i],self.gates_y[i], self.gates_z[i]))
            self.explored.append((self.gates_x[i],self.gates_y[i], self.gates_z[i]))
                    # set the first startchilderen
        for item in self.path:
            self.explored.append(item)
        self.makechildren(self.x[self.index_gate], self.y[self.index_gate],self.z[self.index_gate])
                    # removed the end coordinates [x,y]

    # find and calculate the childeren
    def makechildren(self, x, y, z):

        children = [(x - 1, y, z, [WEST]), (x, y - 1, z, [SOUTH]), (x, y + 1, z,[NORTH]), (x + 1, y, z, [EAST]), (x , y, z + 1, [UP]), (x , y, z - 1, [DOWN])]

        for child in children:
            # print child
            if child[0] == self.x_destinations[self.index_gate] and child[1] == self.y_destinations[self.index_gate] and child[2] == self.z_destinations[self.index_gate]:

                self.lookup_next((self.x[self.index_gate], self.y[self.index_gate],self.z[self.index_gate]), child)

                solution = True

                return solution

            if child[0] >= 0 and child[1] >= 0 and child[2] >= 0 and child[0] < board_size_width and child[1] < board_size_height and child[2] < board_size_depth:
                if not (child[0], child[1], child[2]) in self.explored:
                    self.queue.append(child)

                    self.explored.append((child[0], child[1],child[2]))
                    self.compass.append(child)
                # else:
                #     print child[0], child[1], child[2], "blocked"

                    # self.print_child_state(child)




    #
    def pop_queue_left(self):
        self.queue.popleft()

    #
    # def print_child_state(self, child):
    #     self.board.set_value(CURSOR, child[0], child[1])
    #     self.board.print_board()

    #
    def get_start_gate(self):
        return (self.x[0], self.y[0])

    #
    def get_end_gate(self):
        return (self.x_destinations[0], self.y_destinations[0])

    #
    def lookup_next(self, start_child, child):

        while True:

            if child[3][0] == EAST:
                previous_child = (child[0] - 1, child[1],child[2])
                self.path.append(previous_child)
                self.board.set_value(XLINE, previous_child[0], previous_child[1])
            elif child[3][0] == WEST:
                previous_child = (child[0] + 1, child[1],child[2])
                self.path.append(previous_child)
                self.board.set_value(XLINE, previous_child[0], previous_child[1])
            elif child[3][0] == NORTH:
                previous_child = (child[0], child[1] - 1,child[2])
                self.path.append(previous_child)
                self.board.set_value(YLINE, previous_child[0], previous_child[1])
            elif child[3][0] == SOUTH:
                previous_child = (child[0], child[1] + 1,child[2])
                self.path.append(previous_child)
                self.board.set_value(YLINE, previous_child[0], previous_child[1])
            elif child[3][0] == UP:
                previous_child = (child[0], child[1], child[2] - 1 )
                self.path.append(previous_child)
            elif child[3][0] == DOWN:
                previous_child = (child[0], child[1], child[2] + 1 )
                self.path.append(previous_child)
            for explored_child in self.compass:
                if (explored_child[0], explored_child[1], explored_child[2]) == (previous_child[0], previous_child[1], previous_child[2]):
                    if (explored_child[0], explored_child[1], explored_child[2]) == start_child:
                        return
                    else:
                        child = explored_child

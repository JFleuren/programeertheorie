# import libs
from collections import deque
import sys
import os
import time
import pygame
import sys


pygame.init()

# import classes
from Grid import Grid
from Bfs_function import Bfs_function

# define board size
board_size_width = 18
board_size_height = 13

# initialize pygame time ticker
clock = pygame.time.Clock()

# define destinations array
xdestinations = []
ydestinations = []
zdestinations = []

# set the solution object
solution = False

# define the Frame Per Seconds
# for animations
# FPS = 100

# Main entrance function
def main():

    # initialize empty board
    board = Grid(13, 18)

    # initialize the bfs function & make the first childs
    # from the start gate & add to the queue
    bfs = Bfs_function(board)

    # loop through the netlist until there are none
    while bfs.netlist_counter >= 0:


        # loop untill
        while True:

            # find the shorest path from the queue
            solution = bfs.makechildren(bfs.queue[0][0], bfs.queue[0][1], bfs.queue[0][2])

            # pop the left element in the queue
            bfs.pop_queue_left()

            # if the solution is found
            if solution == True:
                # clear the queue if found
                bfs.queue.clear()

                # set decrease the netlist counter for the next bfs search
                bfs.netlist_counter -= 1
                print bfs.netlist_counter
                #
                bfs.index_gate += 1

                # delete the explored list
                del bfs.explored[:]

                # make the first childs from the start gate & add to the queue
                bfs.next_solution()

                #
                solution = False

                break

            # clock.tick(FPS)
        #
        # board.clear_path()
        # board.add_start_end_gates((bfs.x[bfs.index_gate - 1], bfs.y[bfs.index_gate - 1]), (bfs.x_destinations[bfs.index_gate  - 1], bfs.y_destinations[bfs.index_gate - 1]))
        # board.print_board()

main()

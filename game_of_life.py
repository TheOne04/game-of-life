import pygame
import sys
import random



def dead_state(w, h):
    board = []

    for i in range(h):
        row = [0 for i in range(w)]
        
        board.append(row)
    return board
            


# Generate random board
def random_state(w, h):
    board = []
    
    for i in range(h):
        row = []
        for j in range(w):
            # modify value to get more or less alive cells
            if random.random() <= 0.5:
                cell = 0
            else:
                cell = 1
                
            row.append(cell)
        board.append(row)
    return board

def lies_inside(board, point):
    row = point[0]
    col = point[1]

    width = len(board[0])-1
    height = len(board)-1

    if (0 <= row <= height) and (0 <= col <= width):
        return True
    else:
        return False
    
def alive_neighbors(board, location):
    # all valid neighbors

    row = location[0]
    col = location[1]
    neighbors = [(row-1, col-1), (row-1, col), (row-1, col+1),
                 (row, col-1), (row, col+1),
                 (row+1, col-1), (row+1, col), (row+1, col+1)]

    # check only valid ones, i.e. not negative and more than len-1
    count = 0
    for neighbor in neighbors:
        if lies_inside(board, neighbor):
            neighbor_row = neighbor[0]
            neighbor_col = neighbor[1]

            if board[neighbor_row][neighbor_col]:
                count += 1
    return count


def next_board_state(initial_state):
    w = len(initial_state[0])
    h = len(initial_state)
    
    next_state = dead_state(w, h)
    for i in range(h):
        for j in range(w):
            alive = alive_neighbors(initial_state, (i , j))
            if initial_state[i][j] == 1:
                if alive < 2:
                    next_state[i][j] = 0
                elif alive == 2 or alive == 3:
                    next_state[i][j] = 1
                elif alive > 3:
                    next_state[i][j] = 0
            else:
                if alive == 3:
                    next_state[i][j] = 1
    return next_state




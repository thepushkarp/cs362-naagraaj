import numpy as np
from copy import deepcopy


class Node:
    def __init__(self, matrix):
        self.matrix = matrix
        self.is_visited = False


def get_position(matrix, value):
    if value < 0 or value > 8:
        raise Exception("Given value is not in the matrix!")
    else:
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                if matrix[row][col] == value:
                    return row, col


def get_matrix(matrix, row, col, move):
    blank_tile = matrix[row][col]
    swap_tile = matrix[move[0]][move[1]]
    matrix[row][col] = swap_tile
    matrix[move[0]][move[1]] = blank_tile
    return matrix


def get_frontier(node: Node):
    print(node.matrix, "\n\n")
    # Check if the node is visited or not, mark visited if not
    if node.is_visited == False:
        node.is_visited = True

    row, col = get_position(node.matrix, 0)
    possible_moves = list()
    if row > 0:
        possible_moves.append((row - 1, col))
    if row < 2:
        possible_moves.append((row + 1, col))
    if col > 0:
        possible_moves.append((row, col - 1))
    if col < 2:
        possible_moves.append((row, col + 1))

    frontier = list()
    for move in possible_moves:
        copy_matrix = deepcopy(node.matrix)
        frontier.append(get_matrix(copy_matrix, row, col, move))

    return frontier


CURR_STATE = np.array([[1, 3, 2], [8, 0, 4], [7, 6, 5]])
frontier = get_frontier(Node(CURR_STATE))

for matrix in frontier:
    print("\n", matrix)
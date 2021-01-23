import numpy as np


def mat_to_dict(matrix):
    """
    Converts goal state to dictionary to get indices easier
    
    Parameters:
    matrix(np.ndarray): A 3x3 numpy array with each cell containing unique elements
    
    Returns:
    mat_dict(dict[int, tuple[int, int]]): A mapping of cell contents to a tuple
    contianing its indices
    """
    mat_dict = {}
    for i in range(matrix.shape[0]):
        row = matrix[i];
        for j in range(matrix.shape[1]):
            value = row[j];
            mat_dict[value] = (i, j)
    return mat_dict


def h1(curr_state, goal_dict):
    """
    Heuristic for calculating the distance of goal state using Manhattan distance
    
    Parameters:
    curr_state(np.ndarray): A 3x3 numpy array with each cell containing unique elements
    goal_dict(dict[int, tuple[int, int]]): A mapping of cell contents to a tuple
    contianing its indices
    
    Returns:
    h(int): Heuristic value
    """
    h = 0
    for i in range(curr_state.shape[0]):
        for j in range(curr_state.shape[1]):
            value = curr_state[i][j]
            x = goal_dict[value][0]
            y = goal_dict[value][1]
            h += abs(i-x) + abs(j-y)
    return h


def h2(curr_state, goal_dict):
    """
    Heuristic for calculating the distance of goal state using number of misplaced tiles
    
    Parameters:
    curr_state(np.ndarray): A 3x3 numpy array with each cell containing unique elements
    goal_dict(dict[int, tuple[int, int]]): A mapping of cell contents to a tuple
    contianing its indices
    
    Returns:
    h(int): Heuristic value
    """
    h = 0
    for i in range(curr_state.shape[0]):
        for j in range(curr_state.shape[1]):
            value = curr_state[i][j]
            x = goal_dict[value][0]
            y = goal_dict[value][1]
            if ((x, y) get_ipython().getoutput("= (i, j)):")
                h += 1
    return h


GOAL_STATE = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
print("Goal State:\n", GOAL_STATE)


goal_dict = mat_to_dict(GOAL_STATE)
print("Goal dict:", goal_dict)


# Change this to test
CURR_STATE = np.array([[2, 3, 0], [1, 8, 4], [7, 6, 5]])
print("Current State:\n", CURR_STATE)


# Heuristic 1
print("Value from h1:", h1(CURR_STATE, goal_dict))


# Heuristic 2
print("Value from h2:", h2(CURR_STATE, goal_dict))




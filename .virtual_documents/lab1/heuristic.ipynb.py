import numpy as np


def h1(curr_state, goal_state):
    """
    Heuristic for calculating the distance of goal state using Manhattan distance
    
    Parameters:
    curr_state(np.ndarray): A 3x3 numpy array with each cell containing unique elements
    goal_state(np.ndarray): A 3x3 numpy array with each cell containing unique elements
    
    Returns:
    h(int): Heuristic value
    """
    goal_indices = np.argsort(goal_state.reshape(-1,1), axis=0)
    curr_indices = np.argsort(curr_state.reshape(-1,1), axis=0)
    x = (abs(goal_indices // 3 - curr_indices // 3))
    y = (abs(goal_indices % 3 - curr_indices % 3))
    h = np.sum(x + y)
    return h


def h2(curr_state, goal_state):
    """
    Heuristic for calculating the distance of goal state using number of misplaced tiles
    
    Parameters:
    curr_state(np.ndarray): A 3x3 numpy array with each cell containing unique elements
    goal_state(np.ndarray): A 3x3 numpy array with each cell containing unique elements
    
    Returns:
    h(int): Heuristic value
    """
    h = np.sum(curr_state == goal_state)
    return h


GOAL_STATE = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
print("Goal State:\n", GOAL_STATE)


# Change this state to test
CURR_STATE = np.array([[2, 3, 0], [1, 8, 4], [7, 6, 5]])
print("Current State:\n", CURR_STATE)


# Heuristic 1
print("Value from h1:", h1(CURR_STATE, GOAL_STATE))


# Heuristic 2
print("Value from h2:", h2(CURR_STATE, GOAL_STATE))




import numpy as np
import random


def generate_instance(goal_state, depth):
    """
    Generates a random instance of the 8-puzzle at the given depth from the goal state
    
    Parameters:
    goal_state(np.ndarray): A 3x3 numpy array with each cell containing unique elements representing the goal state
    depth(int): The depth at which the state is to be generated
    
    Returns:
    curr_state(np.ndarray): A 3x3 numpy array with each cell containing unique elements representing the state at the given depth form, the goal state
    """
    x_prev, y_prev = np.array(np.where(goal_state == 0)).reshape(-1)
    curr_state = np.copy(goal_state)
    visited = np.array([curr_state.reshape(-1)])
    while(depth):
        possible_states = []
        if x_prev > 0:
            possible_states.append([x_prev-1, y_prev])
        if x_prev < 2:
            possible_states.append([x_prev+1, y_prev])
        if y_prev > 0:
            possible_states.append([x_prev, y_prev-1])
        if y_prev < 2:
            possible_states.append([x_prev, y_prev+1])
        x_new, y_new = random.choice(possible_states)
        curr_state[x_new, y_new], curr_state[x_prev, y_prev] = curr_state[x_prev, y_prev], curr_state[x_new, y_new]
        if curr_state.reshape(-1).tolist() not in visited.tolist():
            visited = np.vstack((visited, curr_state.reshape(-1)))
            x_prev, y_prev = x_new, y_new
            depth -= 1
        else:
            curr_state[x_new, y_new], curr_state[x_prev, y_prev] = curr_state[x_prev, y_prev], curr_state[x_new, y_new]
    return curr_state


GOAL_STATE = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
print("Goal State:\n", GOAL_STATE)


print(generate_instance(GOAL_STATE, 5))




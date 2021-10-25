# Only numpy
import numpy as np



# Initialisze parameters
gama = 0.75 # Discount factor
alpha = 0.9 # Learning rate



# Define the states
location_to_state = {
    "L1": 0,
    "L1": 1,
    "L1": 2,
    "L1": 3,
    "L1": 4,
    "L1": 5,
    "L1": 6,
    "L1": 7,
    "L1": 8
}



# Define the actions
actions = [0, 1, 2, 3, 4, 5, 6, 7, 8]



# Define the rewards
rewards = np.array([
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0]
])



# Map indices to locations
state_to_location = dict((state, location) for location, state in location_to_state.items())


def get_optimal_route(start_location, end_location):
    # Copy the rewards matrix to new Matrix
    rewards_new = np.copy(rewards)
    # Get the ending state corresponding to the ending location as given
    ending_state = location_to_state[end_location]
    # With the above information automatically set the priority of the given ending state to the highest one
    rewards_new[ending_state, ending_state] = 999

    # ------------- Q-Learning Algorithm ---------------

    # Initializing Q-values
    Q = np.array(np.zeros([9, 9]))

    # Q-learning process
    for i in range(1000):
        # Pick up a state randomly
        current_state = np.random.randint(0, 9)  # Python excludes the upper bound
        # For tranversing through the neigbor locations in the maze
        playable_actions = []
        # Iterate through the new rewards matrix and get the actions > 0
        for j in range(9):
            if rewards_new[current_state, j] > 0:
                playable_actions.append(j)
        # Pick an action randomly from the list of playable actions leading us to the next state
        next_state = np.random.choice(playable_actions)
        # Compute the temporal differences
        # The action here exactly refers to going to the next state
        TD = rewards_new[current_state, next_state] + gama * Q[next_state, np.argmax(Q[next_state])] - Q[
            current_state, next_state]
        # Update the Q-value using the Bellman equation
        Q[current_state, next_state] += alpha * TD

    # Initialize the optimal route with the starting location
    route = [start_location]
    # We do not know about the next location yet, so initialize with the value of starting location
    next_location = start_location

    # We don't know about the exact number of iterations needed to reach to the final location hence while loop will be a good choice for iteration
    while (next_location != end_location):
        # Fetch the starting state
        starting_state = location_to_state[start_location]
        # Fetch the highest Q-value pertataining to starting state
        next_state = state_to_location[next_state]
        route.append(next_location)
        # Update the starting location for the next iteration
        start_location = next_location

    return route



print(get_optimal_route("L9", "L1"))
